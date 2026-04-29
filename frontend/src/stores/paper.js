import { defineStore } from 'pinia'
import { ref, computed, watch } from 'vue'
import axios from 'axios'
import api from '../api/index.js'

const API_BASE = '/api'
axios.defaults.timeout = 0

// ─── Cookie helpers ────────────────────────────────────────────────────────
const COOKIE_PAPER   = 'pg_paper'
const COOKIE_JOB     = 'pg_job'
const COOKIE_MAX_AGE = 60 * 60 * 24 * 7 // 7 days in seconds

function setCookie(name, value, maxAge = COOKIE_MAX_AGE) {
  document.cookie = `${name}=${encodeURIComponent(value)}; max-age=${maxAge}; path=/; SameSite=Lax`
}

function getCookie(name) {
  const match = document.cookie.split('; ').find(r => r.startsWith(name + '='))
  return match ? decodeURIComponent(match.split('=').slice(1).join('=')) : null
}

function deleteCookie(name) {
  document.cookie = `${name}=; max-age=0; path=/`
}

// ─── Standalone helpers (needed before store init) ────────────────────────
function createEmptyPaper() {
  return {
    journal: 'IEEE',
    title: '',
    authors: [{ name: '', affiliation: '', location: '', email: '' }],
    abstract: '',
    keywords: [],
    sections: [],
    references: [],
    figures: []
  }
}

function normContent(content) {
  if (!content) return []
  if (typeof content === 'string') return content.trim() ? [{ id: 'text', text: content }] : []
  if (!Array.isArray(content)) return []
  return content.map(item => {
    if (typeof item === 'string') return { id: 'text', text: item }
    return { ...item }
  })
}

function fromPaperJsonRaw(json) {
  const p = createEmptyPaper()
  p.journal = (json.journal || json.template || 'IEEE')
  p.title = json.title || ''
  p.authors = (json.authors || []).length ? json.authors : [{ name: '', affiliation: '', location: '', email: '' }]
  p.abstract = json.abstract || ''
  p.keywords = json.keywords || []

  const sKeys = Object.keys(json).filter(k => /^section\d+$/.test(k))
    .sort((a, b) => parseInt(a.replace('section', '')) - parseInt(b.replace('section', '')))

  if (sKeys.length) {
    for (const sKey of sKeys) {
      const sData = json[sKey]
      const sec = { title: sData.title || '', content: normContent(sData.content), subsections: [] }
      const subKeys = Object.keys(sData).filter(k => new RegExp(`^${sKey}[a-z]$`).test(k)).sort()
      for (const sk of subKeys) {
        sec.subsections.push({ title: sData[sk].title || '', content: normContent(sData[sk].content) })
      }
      p.sections.push(sec)
    }
  } else if (Array.isArray(json.sections)) {
    for (const sec of json.sections) {
      const s = { title: sec.title || '', content: normContent(sec.content), subsections: [] }
      for (const sub of (sec.subsections || [])) {
        s.subsections.push({ title: sub.title || '', content: normContent(sub.content) })
      }
      p.sections.push(s)
    }
  }

  if (json.references) {
    if (typeof json.references === 'object' && !Array.isArray(json.references) && json.references.content) {
      p.references = json.references.content || []
    } else if (Array.isArray(json.references)) {
      p.references = json.references.map(r => typeof r === 'string' ? r : (r.text || ''))
    }
  }
  return p
}

function toRomanNum(num) {
  const map = [[1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],[100,'C'],[90,'XC'],[50,'L'],[40,'XL'],[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']]
  let r = ''
  for (const [v, s] of map) { while (num >= v) { r += s; num -= v } }
  return r
}

// ─── Paper Store ──────────────────────────────────────────────────────────
export const usePaperStore = defineStore('paper', () => {
  // Restore paper from cookie on init (if available)
  const _cookieJson = (() => { try { const r = getCookie(COOKIE_PAPER); return r ? JSON.parse(r) : null } catch { return null } })()
  const paper = ref(_cookieJson ? fromPaperJsonRaw(_cookieJson) : createEmptyPaper())

  // Current paper DB id (null = unsaved new paper)
  const currentPaperId = ref(null)
  // Paper images for the current paper
  const paperImages = ref([])

  const loading = ref(false)
  const aiLoading = ref(false)
  const aiLoadingMessage = ref('')
  const toast = ref({ show: false, message: '', type: 'info' })

  const availableJournals = ref([])
  const journalsLoading = ref(false)

  async function fetchJournals() {
    if (availableJournals.value.length) return availableJournals.value
    journalsLoading.value = true
    try {
      const res = await api.get(`${API_BASE}/journals`, { timeout: 10000 })
      availableJournals.value = (res.data?.journals || []).filter(Boolean)
      if (!availableJournals.value.length) availableJournals.value = ['IEEE']
    } catch {
      // Fallback (minimal) — backend should normally provide the full list
      availableJournals.value = ['IEEE', 'MEV', 'ULTIMACOMP']
    } finally {
      journalsLoading.value = false
    }

    const current = (paper.value.journal || 'IEEE')
    if (availableJournals.value.length && !availableJournals.value.includes(current)) {
      paper.value.journal = availableJournals.value[0]
    }
    return availableJournals.value
  }

  // ─── Auto-save paper to cookie on every deep change ───────────────────
  watch(paper, (val) => {
    try { setCookie(COOKIE_PAPER, JSON.stringify(toPaperJson())) } catch { /* ignore */ }
  }, { deep: true })

  function showToast(message, type = 'info') {
    toast.value = { show: true, message, type }
    setTimeout(() => { toast.value.show = false }, 3500)
  }

  // ─── Auto Numbering ────────────────────────────────────────────────────
  const numbering = computed(() => {
    let imgNum = 1, tblNum = 1, eqNum = 1
    const map = new Map()
    function walk(items) {
      for (const item of (items || [])) {
        if (item.id === 'gambar') map.set(item, { num: imgNum++, label: `${imgNum - 1}` })
        else if (item.id === 'tabel') map.set(item, { num: tblNum++, label: toRomanNum(tblNum - 1) })
        else if (item.id === 'rumus') map.set(item, { num: eqNum++, label: `${eqNum - 1}` })
      }
    }
    for (const sec of paper.value.sections) {
      walk(sec.content)
      for (const sub of (sec.subsections || [])) walk(sub.content)
    }
    return map
  })

  function getItemNumber(item) { return numbering.value.get(item) || {} }

  // ─── Convert TO paper.json format ──────────────────────────────────────
  function toPaperJson() {
    const p = paper.value
    const json = { journal: p.journal || 'IEEE', title: p.title, authors: p.authors, abstract: p.abstract, keywords: p.keywords }
    let imgNum = 1, tblNum = 1, eqNum = 1

    function numContent(items) {
      return (items || []).map(item => {
        const c = { ...item }
        if (item.id === 'gambar') c.ImageNumber = String(imgNum++)
        if (item.id === 'tabel') c.TableNumber = toRomanNum(tblNum++)
        if (item.id === 'rumus') c.FormulaNumber = String(eqNum++)
        return c
      })
    }

    p.sections.forEach((sec, sIdx) => {
      const sKey = `section${sIdx + 1}`
      const sObj = { title: sec.title, content: numContent(sec.content) }
      ;(sec.subsections || []).forEach((sub, subIdx) => {
        const subKey = `${sKey}${String.fromCharCode(97 + subIdx)}`
        sObj[subKey] = { title: sub.title, content: numContent(sub.content) }
      })
      json[sKey] = sObj
    })

    json.references = {
      number: toRomanNum(p.sections.length + 1),
      title: 'REFERENCES',
      content: p.references
    }
    return json
  }

  // ─── Convert FROM paper.json or legacy format ─────────────────────────
  function fromPaperJson(json) { return fromPaperJsonRaw(json) }

  // ─── CRUD: Sections ───────────────────────────────────────────────────
  function addSection() {
    paper.value.sections.push({ title: '', content: [{ id: 'text', text: '' }], subsections: [] })
  }
  function removeSection(idx) { paper.value.sections.splice(idx, 1) }

  function addSubsection(sIdx) {
    paper.value.sections[sIdx].subsections.push({ title: '', content: [{ id: 'text', text: '' }] })
  }
  function removeSubsection(sIdx, subIdx) { paper.value.sections[sIdx].subsections.splice(subIdx, 1) }

  function addContent(container, type) {
    const items = {
      text: { id: 'text', text: '' },
      gambar: { id: 'gambar', Title: '', Path: '', Prompt: '' },
      tabel: { id: 'tabel', Title: '', Headers: ['Col 1', 'Col 2'], Rows: [['', '']] },
      rumus: { id: 'rumus', latex: '' }
    }
    if (items[type]) container.push({ ...items[type] })
  }
  function removeContent(container, idx) { container.splice(idx, 1) }
  function moveContent(container, idx, dir) {
    const newIdx = idx + dir
    if (newIdx < 0 || newIdx >= container.length) return
    const tmp = container[idx]
    container.splice(idx, 1)
    container.splice(newIdx, 0, tmp)
  }

  // ─── CRUD: Authors ────────────────────────────────────────────────────
  function addAuthor() { paper.value.authors.push({ name: '', affiliation: '', location: '', email: '' }) }
  function removeAuthor(idx) { if (paper.value.authors.length > 1) paper.value.authors.splice(idx, 1) }

  // ─── CRUD: Keywords ───────────────────────────────────────────────────
  function addKeyword(kw) { if (kw && !paper.value.keywords.includes(kw)) paper.value.keywords.push(kw) }
  function removeKeyword(idx) { paper.value.keywords.splice(idx, 1) }

  // ─── CRUD: References ─────────────────────────────────────────────────
  function addReference() { paper.value.references.push('') }
  function removeReference(idx) { paper.value.references.splice(idx, 1) }

  // ─── CRUD: Figure helpers ──────────────────────────────────────────────
  function addFigure() {
    if (!paper.value.figures) paper.value.figures = []
    paper.value.figures.push({ caption: '', hasImage: false, filename: '', url: '' })
  }
  function removeFigure(idx) { paper.value.figures.splice(idx, 1) }

  // ─── CRUD: Table helpers ──────────────────────────────────────────────
  function addTableRow(item) { item.Rows.push(new Array(item.Headers.length).fill('')) }
  function removeTableRow(item, rIdx) { item.Rows.splice(rIdx, 1) }
  function addTableCol(item) { item.Headers.push(`Col ${item.Headers.length + 1}`); item.Rows.forEach(r => r.push('')) }
  function removeTableCol(item, cIdx) {
    if (item.Headers.length > 1) { item.Headers.splice(cIdx, 1); item.Rows.forEach(r => r.splice(cIdx, 1)) }
  }

  // ─── Import / Export ──────────────────────────────────────────────────
  function newPaper() {
    paper.value = createEmptyPaper()
    deleteCookie(COOKIE_PAPER)
    deleteCookie(COOKIE_JOB)
    showToast('New paper created', 'success')
  }

  function uploadJson(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader()
      reader.onload = (e) => {
        try {
          const data = JSON.parse(e.target.result)
          paper.value = fromPaperJsonRaw(data)
          showToast('Paper loaded from JSON!', 'success')
          resolve(true)
        } catch (err) { showToast('Invalid JSON: ' + err.message, 'error'); reject(err) }
      }
      reader.readAsText(file)
    })
  }

  function downloadJson() {
    const data = JSON.stringify(toPaperJson(), null, 2)
    const blob = new Blob([data], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${(paper.value.title || 'paper').replace(/[^a-zA-Z0-9_\-]/g, '_').slice(0, 60)}.json`
    document.body.appendChild(a); a.click(); a.remove()
    URL.revokeObjectURL(url)
    showToast('JSON downloaded!', 'success')
  }

  async function exportDocx() {
    try {
      loading.value = true
      const journal = (paper.value.journal || 'IEEE').trim() || 'IEEE'
      const res = await api.post(`${API_BASE}/export`, { journal, paper: toPaperJson() }, { responseType: 'blob' })
      const url = window.URL.createObjectURL(new Blob([res.data]))
      const a = document.createElement('a')
      a.href = url
      a.download = `${journal}_${(paper.value.title || 'paper').replace(/[^a-zA-Z0-9_\-]/g, '_').slice(0, 60)}.docx`
      document.body.appendChild(a); a.click(); a.remove()
      window.URL.revokeObjectURL(url)
      showToast('DOCX exported!', 'success')
    } catch (err) {
      showToast('Export failed: ' + (err.response?.data?.error || err.message), 'error')
    } finally { loading.value = false }
  }

  // ─── AI ───────────────────────────────────────────────────────────────

  /** Shared polling loop — used by both new generation and resume-after-refresh */
  async function _pollJob(jobId, t0) {
    while (true) {
      await new Promise(r => setTimeout(r, 3000))
      const el = Math.round((Date.now() - t0) / 1000)
      const m = Math.floor(el / 60), s = el % 60
      aiLoadingMessage.value = `AI sedang membuat paper... (${m > 0 ? m + 'm ' : ''}${s}s)`
      let poll
      try { poll = await api.get(`${API_BASE}/job/${jobId}`, { timeout: 10000 }) } catch { continue }
      if (poll.data.status === 'done') {
        paper.value = fromPaperJsonRaw(poll.data.paper)
        deleteCookie(COOKIE_JOB)
        showToast('Paper berhasil dibuat!', 'success')
        return true
      }
      if (poll.data.status === 'error') throw new Error(poll.data.error || 'Failed')
      if (Date.now() - t0 > 25 * 60 * 1000) throw new Error('Timeout: > 25 menit')
    }
  }

  async function aiGenerateFullPaper(prompt, { topic, style, pdfTexts } = {}) {
    try {
      aiLoading.value = true
      aiLoadingMessage.value = 'Menghubungi AI...'
      const payload = { prompt }
      if (topic) payload.topic = topic
      if (style) payload.style = style
      if (pdfTexts && pdfTexts.length) payload.pdf_texts = pdfTexts
      const startRes = await api.post(`${API_BASE}/generate-full`, payload, { timeout: 15000 })
      if (!startRes.data?.job_id) throw new Error(startRes.data?.error || 'No job_id')
      const jobId = startRes.data.job_id
      setCookie(COOKIE_JOB, JSON.stringify({ jobId, t0: Date.now() }), 60 * 30)
      return await _pollJob(jobId, Date.now())
    } catch (err) {
      showToast('AI Error: ' + err.message, 'error')
      return false
    } finally { aiLoading.value = false; aiLoadingMessage.value = '' }
  }

  /**
   * Call this on app mount. If a job was in-flight when the page was refreshed,
   * resume polling and restore the result automatically.
   */
  async function resumePendingJob() {
    const raw = getCookie(COOKIE_JOB)
    if (!raw) return
    let jobInfo
    try { jobInfo = JSON.parse(raw) } catch { deleteCookie(COOKIE_JOB); return }
    const { jobId, t0 } = jobInfo || {}
    if (!jobId || !t0) { deleteCookie(COOKIE_JOB); return }
    if (Date.now() - t0 > 25 * 60 * 1000) { deleteCookie(COOKIE_JOB); return }
    try {
      const check = await api.get(`${API_BASE}/job/${jobId}`, { timeout: 8000 })
      if (check.data.status === 'error' || !check.data.status) { deleteCookie(COOKIE_JOB); return }
      if (check.data.status === 'done') {
        paper.value = fromPaperJsonRaw(check.data.paper)
        deleteCookie(COOKIE_JOB)
        showToast('Paper dipulihkan dari proses sebelumnya!', 'success')
        return
      }
    } catch { deleteCookie(COOKIE_JOB); return }

    aiLoading.value = true
    aiLoadingMessage.value = 'Melanjutkan proses AI...'
    try {
      await _pollJob(jobId, t0)
    } catch (err) {
      showToast('AI Error (resumed): ' + err.message, 'error')
    } finally { aiLoading.value = false; aiLoadingMessage.value = '' }
  }

  // ─── DB Save/Load ─────────────────────────────────────────────────────
  async function savePaperToDb() {
    try {
      loading.value = true
      const paperData = { ...toPaperJson(), id: currentPaperId.value || undefined }
      const res = await api.post(`${API_BASE}/papers`, paperData)
      if (res.data.id && !currentPaperId.value) {
        currentPaperId.value = res.data.id
      }
      showToast('Paper saved!', 'success')
      return res.data.id
    } catch (err) {
      showToast('Save failed: ' + (err.response?.data?.error || err.message), 'error')
      return null
    } finally { loading.value = false }
  }

  async function loadPaperFromDb(paperId) {
    try {
      loading.value = true
      const res = await api.get(`${API_BASE}/papers/${paperId}`)
      paper.value = fromPaperJsonRaw(res.data)
      currentPaperId.value = paperId
      // Load paper images
      await loadPaperImages(paperId)
      return true
    } catch (err) {
      showToast('Load failed: ' + (err.response?.data?.error || err.message), 'error')
      return false
    } finally { loading.value = false }
  }

  async function loadPaperImages(paperId) {
    try {
      const res = await api.get(`${API_BASE}/papers/${paperId}/images`)
      paperImages.value = res.data.images || []
    } catch { paperImages.value = [] }
  }

  async function uploadImage(figureIndex, file) {
    try {
      if (!currentPaperId.value) {
        // Must save paper first to get an ID
        const id = await savePaperToDb()
        if (!id) return
      }
      const formData = new FormData()
      formData.append('file', file)
      const res = await api.post(`${API_BASE}/papers/${currentPaperId.value}/images`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      const img = res.data.image
      paperImages.value.push(img)
      // Auto-assign to figure if figureIndex is provided
      if (figureIndex !== undefined && paper.value.figures?.[figureIndex]) {
        paper.value.figures[figureIndex].filename = img.filename
        paper.value.figures[figureIndex].url = img.url
      }
      showToast('Image uploaded!', 'success')
      return img
    } catch (err) {
      showToast('Upload failed: ' + (err.response?.data?.error || err.message), 'error')
      return null
    }
  }

  async function deletePaperImage(imageId) {
    try {
      await api.delete(`${API_BASE}/papers/${currentPaperId.value}/images/${imageId}`)
      paperImages.value = paperImages.value.filter(img => img.id !== imageId)
      showToast('Image deleted', 'success')
    } catch (err) {
      showToast('Delete failed: ' + (err.response?.data?.error || err.message), 'error')
    }
  }

  // ─── Helpers ──────────────────────────────────────────────────────────
  function toRoman(num) { return toRomanNum(num) }

  return {
    paper, loading, aiLoading, aiLoadingMessage, toast,
    currentPaperId, paperImages,
    availableJournals, journalsLoading, fetchJournals,
    numbering, getItemNumber, toPaperJson, fromPaperJson,
    addSection, removeSection, addSubsection, removeSubsection,
    addContent, removeContent, moveContent,
    addAuthor, removeAuthor, addKeyword, removeKeyword,
    addReference, removeReference,
    addFigure, removeFigure,
    addTableRow, removeTableRow, addTableCol, removeTableCol,
    newPaper, uploadJson, downloadJson, exportDocx,
    aiGenerateFullPaper, resumePendingJob,
    savePaperToDb, loadPaperFromDb, loadPaperImages,
    uploadImage, deletePaperImage,
    showToast, toRoman,
    apiGet: (url) => api.get(url),
    apiUploadPdfs: (formData) => api.post(`${API_BASE}/upload-pdfs`, formData, { headers: { 'Content-Type': 'multipart/form-data' } }),
  }
})
