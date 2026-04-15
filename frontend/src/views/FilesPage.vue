<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <main class="max-w-5xl mx-auto px-4 py-8">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-2xl font-bold text-gray-800">File Manager</h1>
          <p class="text-gray-500 text-sm mt-1">Manage images for each paper</p>
        </div>
        <router-link to="/dashboard" class="text-sm text-gray-500 hover:text-gray-800 flex items-center gap-1">
          ← Back to Papers
        </router-link>
      </div>

      <!-- Paper selector if no paperId in route -->
      <div v-if="!currentPaperId" class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Select Paper</label>
        <select v-model="selectedPaperId" @change="onSelectPaper"
          class="w-full max-w-md px-3 py-2 border border-gray-200 rounded-xl text-sm bg-white focus:ring-2 focus:ring-blue-200 outline-none">
          <option value="">— Select a paper —</option>
          <option v-for="p in papers" :key="p.id" :value="p.id">{{ p.title }}</option>
        </select>
      </div>

      <!-- Breadcrumb for specific paper -->
      <div v-if="currentPaperId && paperTitle" class="mb-6 flex items-center gap-2">
        <router-link to="/files" class="text-sm text-blue-600 hover:underline">All Papers</router-link>
        <span class="text-gray-400">/</span>
        <span class="text-sm font-medium text-gray-800">{{ paperTitle }}</span>
        <router-link :to="`/editor/${currentPaperId}`" class="ml-2 text-xs text-blue-500 hover:underline">
          Edit Paper →
        </router-link>
      </div>

      <div v-if="!effectivePaperId" class="text-center py-20 text-gray-400">
        <div class="text-4xl mb-3">🗂️</div>
        <p>Select a paper to manage its images</p>
      </div>

      <div v-else>
        <!-- Upload Zone -->
        <div class="bg-white rounded-2xl border shadow-sm p-6 mb-6">
          <h2 class="font-semibold text-gray-700 mb-4">Upload Images</h2>
          <div
            class="border-2 border-dashed border-gray-300 rounded-xl p-8 text-center hover:border-blue-400 cursor-pointer transition-colors"
            @click="triggerUpload"
            @dragover.prevent @drop.prevent="handleDrop"
          >
            <input ref="fileInput" type="file" accept="image/*" multiple @change="handleFileSelect" class="hidden" />
            <div v-if="uploading" class="text-blue-500">
              <div class="w-8 h-8 border-4 border-blue-200 border-t-blue-500 rounded-full animate-spin mx-auto mb-2"></div>
              Uploading...
            </div>
            <div v-else>
              <div class="text-4xl mb-2">📁</div>
              <p class="text-gray-500 text-sm">Click or drag images here to upload</p>
              <p class="text-gray-400 text-xs mt-1">PNG, JPG, SVG, WebP supported</p>
            </div>
          </div>
        </div>

        <!-- Images Grid -->
        <div class="bg-white rounded-2xl border shadow-sm p-6">
          <div class="flex items-center justify-between mb-4">
            <h2 class="font-semibold text-gray-700">Images ({{ images.length }})</h2>
          </div>

          <div v-if="images.length === 0" class="text-center py-12 text-gray-400">
            <div class="text-4xl mb-3">🖼️</div>
            <p>No images uploaded for this paper yet</p>
          </div>

          <div v-else class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
            <div v-for="img in images" :key="img.id"
              class="group relative rounded-xl overflow-hidden border bg-gray-50 aspect-square">
              <img :src="resolveUrl(img.url)" :alt="img.original_name"
                class="w-full h-full object-cover" />
              <!-- Overlay -->
              <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex flex-col items-center justify-center p-2">
                <p class="text-white text-xs text-center truncate w-full mb-2">{{ img.original_name }}</p>
                <button @click="copyUrl(img)" class="text-xs bg-white/20 hover:bg-white/30 text-white rounded px-2 py-1 mb-1 w-full transition-colors">
                  📋 Copy URL
                </button>
                <button @click="confirmDelete(img)" class="text-xs bg-red-500/80 hover:bg-red-500 text-white rounded px-2 py-1 w-full transition-colors">
                  🗑 Delete
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Delete Confirm -->
    <div v-if="deleteTarget" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-2xl shadow-xl p-6 max-w-sm w-full">
        <h3 class="font-semibold text-gray-800 mb-2">Delete Image?</h3>
        <p class="text-gray-500 text-sm mb-5">"{{ deleteTarget.original_name }}" will be permanently deleted.</p>
        <div class="flex gap-3">
          <button @click="deleteTarget = null" class="flex-1 px-4 py-2.5 border border-gray-200 hover:bg-gray-50 rounded-xl text-sm">Cancel</button>
          <button @click="doDelete()" class="flex-1 px-4 py-2.5 bg-red-600 hover:bg-red-700 text-white rounded-xl text-sm">Delete</button>
        </div>
      </div>
    </div>

    <!-- Toast -->
    <Teleport to="body">
      <div v-if="toastMsg" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-[999]">
        <div class="px-4 py-2.5 rounded-lg shadow-lg text-white text-sm bg-green-600">{{ toastMsg }}</div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api/index.js'
import AppHeader from '../components/AppHeader.vue'

const route = useRoute()
const router = useRouter()
const BASE = import.meta.env.VITE_API_URL || ''

const papers = ref([])
const selectedPaperId = ref('')
const images = ref([])
const uploading = ref(false)
const deleteTarget = ref(null)
const fileInput = ref(null)
const toastMsg = ref('')
const paperTitle = ref('')

const currentPaperId = computed(() => route.params.paperId || null)
const effectivePaperId = computed(() => currentPaperId.value || selectedPaperId.value)

function onSelectPaper() {
  if (!selectedPaperId.value) return
  router.push(`/files/${selectedPaperId.value}`)
}

function resolveUrl(url) {
  return url?.startsWith('http') ? url : `${BASE}${url}`
}

function showToast(msg) {
  toastMsg.value = msg
  setTimeout(() => { toastMsg.value = '' }, 2500)
}

async function loadPapers() {
  try {
    const res = await api.get('/api/papers')
    papers.value = res.data.papers || []
  } catch {}
}

async function loadImages() {
  const pid = effectivePaperId.value
  if (!pid) return
  try {
    const res = await api.get(`/api/papers/${pid}/images`)
    images.value = res.data.images || []
    if (currentPaperId.value) {
      const paper = papers.value.find(p => p.id === currentPaperId.value)
      paperTitle.value = paper?.title || 'Paper'
    }
  } catch {}
}

function triggerUpload() { fileInput.value?.click() }

async function handleFileSelect(e) {
  const files = Array.from(e.target.files || [])
  if (files.length) await uploadFiles(files)
  e.target.value = ''
}

async function handleDrop(e) {
  const files = Array.from(e.dataTransfer.files || []).filter(f => f.type.startsWith('image/'))
  if (files.length) await uploadFiles(files)
}

async function uploadFiles(files) {
  const pid = effectivePaperId.value
  if (!pid) return
  uploading.value = true
  for (const file of files) {
    try {
      const fd = new FormData()
      fd.append('file', file)
      const res = await api.post(`/api/papers/${pid}/images`, fd, { headers: { 'Content-Type': 'multipart/form-data' } })
      images.value.push(res.data.image)
    } catch (e) {
      console.error('Upload failed', e)
    }
  }
  uploading.value = false
  showToast(`${files.length} image(s) uploaded!`)
}

function confirmDelete(img) { deleteTarget.value = img }

async function doDelete() {
  if (!deleteTarget.value) return
  const pid = effectivePaperId.value
  try {
    await api.delete(`/api/papers/${pid}/images/${deleteTarget.value.id}`)
    images.value = images.value.filter(i => i.id !== deleteTarget.value.id)
    showToast('Image deleted')
  } catch {}
  deleteTarget.value = null
}

function copyUrl(img) {
  const url = resolveUrl(img.url)
  navigator.clipboard.writeText(url).then(() => showToast('URL copied!')).catch(() => {})
}

onMounted(async () => {
  await loadPapers()
  if (currentPaperId.value) {
    const paper = papers.value.find(p => p.id === currentPaperId.value)
    paperTitle.value = paper?.title || 'Paper'
    await loadImages()
  }
})

watch(effectivePaperId, async (pid, prev) => {
  if (!pid || pid === prev) return
  await loadImages()
})
</script>
