<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />

    <!-- Sticky Toolbar -->
    <div class="bg-white border-b sticky top-[57px] z-30 shadow-sm">
      <div class="px-4 lg:px-8 py-2 flex items-center justify-between gap-2 flex-wrap">
        <!-- Left: breadcrumb + title -->
        <div class="flex items-center gap-2 min-w-0">
          <router-link to="/dashboard"
            class="flex items-center gap-1 text-sm text-gray-500 hover:text-gray-800 px-2 py-1.5 rounded hover:bg-gray-100 shrink-0 transition-colors">
            ← Papers
          </router-link>
          <span class="text-gray-200">|</span>
          <span class="text-sm text-gray-600 font-medium truncate max-w-xs lg:max-w-md">
            {{ store.paper.title || 'Untitled Paper' }}
          </span>
          <span v-if="autoSaving" class="text-xs text-blue-400 animate-pulse shrink-0 ml-1">Saving...</span>
          <span v-else-if="savedOk" class="text-xs text-green-500 shrink-0 ml-1">✓ Saved</span>
        </div>

        <!-- Right: tabs + action buttons -->
        <div class="flex items-center gap-1 flex-wrap">
          <button v-for="tab in tabs" :key="tab.id"
            @click="activeTab = tab.id"
            :class="['px-3 py-1.5 rounded-lg text-xs font-medium transition-colors',
              activeTab === tab.id ? 'bg-blue-100 text-blue-700' : 'text-gray-500 hover:bg-gray-100']">
            {{ tab.label }}
          </button>
          <div class="w-px h-5 bg-gray-200 mx-1 shrink-0"></div>
          <button @click="store.downloadJson()"
            class="px-3 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-medium transition-colors">
            💾 Save
          </button>
          <label class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-600 text-xs cursor-pointer transition-colors">
            📂 Load
            <input type="file" accept=".json" class="hidden" @change="onUploadJson" />
          </label>
          <button @click="store.exportDocx()" :disabled="store.loading"
            class="px-3 py-1.5 bg-orange-500 hover:bg-orange-600 text-white rounded-lg text-xs font-medium disabled:opacity-50 transition-colors">
            📄 DOCX
          </button>
        </div>
      </div>
    </div>

    <!-- Full-width content area -->
    <div class="px-4 lg:px-8 py-6">

      <!-- TAB: EDITOR -->
      <div v-show="activeTab === 'editor'" class="space-y-4">

        <!-- AI Generate -->
        <div class="bg-white rounded-xl shadow-sm border-t-4 border-t-purple-500 p-5">
          <h2 class="font-semibold text-gray-700 mb-3 flex items-center gap-2">⚡ Generate with AI</h2>
          <div class="flex gap-3">
            <textarea v-model="aiPrompt" rows="2"
              placeholder="e.g. Real-Time Hand Gesture Recognition for PLC Control using MediaPipe..."
              class="flex-1 px-4 py-2.5 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-purple-200 focus:border-purple-400 outline-none resize-none"
              :disabled="store.aiLoading" @keydown.ctrl.enter="generateAI"></textarea>
            <button @click="generateAI" :disabled="store.aiLoading || !aiPrompt.trim()"
              class="self-end px-5 py-2.5 bg-purple-600 hover:bg-purple-700 text-white rounded-lg text-sm font-medium disabled:opacity-50 whitespace-nowrap transition-colors">
              {{ store.aiLoading ? 'Processing...' : 'Generate' }}
            </button>
          </div>
        </div>

        <!-- Title -->
        <div class="card border-l-4 border-l-blue-500">
          <label class="label">Title</label>
          <input v-model="store.paper.title" class="input" placeholder="Paper title..." />
        </div>

        <!-- Authors (drag-and-drop) -->
        <div class="card border-l-4 border-l-blue-500">
          <div class="flex items-center justify-between mb-3">
            <label class="label !mb-0">Authors</label>
            <button @click="store.addAuthor()" class="btn-add">+ Author</button>
          </div>
          <draggable :list="store.paper.authors" :item-key="stableKey" animation="150" handle=".author-drag" class="space-y-2">
            <template #item="{ element: author, index: i }">
              <div class="bg-gray-50 border rounded-lg p-3 flex gap-2 items-start">
                <span class="author-drag cursor-grab active:cursor-grabbing text-gray-300 hover:text-gray-500 select-none text-xl leading-tight pt-1">⠿</span>
                <div class="flex-1">
                  <div class="flex justify-between mb-2">
                    <span class="text-xs text-gray-400 font-medium">Author {{ i + 1 }}</span>
                    <button v-if="store.paper.authors.length > 1" @click="store.removeAuthor(i)"
                      class="text-xs text-red-400 hover:text-red-600">✕</button>
                  </div>
                  <div class="grid grid-cols-2 gap-2">
                    <input v-model="author.name" class="input-sm" placeholder="Name" />
                    <input v-model="author.email" class="input-sm" placeholder="Email" />
                    <input v-model="author.affiliation" class="input-sm col-span-2" placeholder="Affiliation" />
                    <input v-model="author.location" class="input-sm col-span-2" placeholder="Location" />
                  </div>
                </div>
              </div>
            </template>
          </draggable>
        </div>

        <!-- Abstract -->
        <div class="card border-l-4 border-l-blue-500">
          <label class="label">Abstract</label>
          <textarea v-model="store.paper.abstract" rows="5" class="input" placeholder="Paper abstract..."></textarea>
        </div>

        <!-- Keywords -->
        <div class="card border-l-4 border-l-blue-500">
          <label class="label">Keywords</label>
          <div class="flex flex-wrap gap-1.5 mb-2">
            <span v-for="(kw, i) in store.paper.keywords" :key="i"
              class="bg-blue-50 text-blue-700 px-2 py-0.5 rounded text-sm flex items-center gap-1">
              {{ kw }}
              <button @click="store.removeKeyword(i)" class="text-blue-400 hover:text-blue-600 text-xs">✕</button>
            </span>
          </div>
          <div class="flex gap-2">
            <input v-model="newKeyword" class="input-sm flex-1" placeholder="Add keyword..." @keyup.enter="addKw" />
            <button @click="addKw" class="btn-add">Add</button>
          </div>
        </div>

        <!-- Sections (drag-and-drop) -->
        <draggable :list="store.paper.sections" :item-key="stableKey" animation="150" handle=".section-drag" class="space-y-4">
          <template #item="{ element: section, index: sIdx }">
            <div class="card border-l-4 border-l-green-500">
              <!-- Section Header -->
              <div class="flex items-center justify-between mb-3">
                <div class="flex items-center gap-2 flex-1 min-w-0">
                  <span class="section-drag cursor-grab active:cursor-grabbing text-gray-300 hover:text-gray-500 select-none text-xl leading-tight shrink-0">⠿</span>
                  <span class="text-xs font-bold text-green-600 bg-green-50 px-2 py-0.5 rounded shrink-0">
                    Section {{ toRoman(sIdx + 1) }}
                  </span>
                  <input v-model="section.title" class="input-sm flex-1 font-semibold min-w-0"
                    placeholder="Section Title (e.g. INTRODUCTION)" />
                </div>
                <button @click="store.removeSection(sIdx)"
                  class="text-xs text-red-400 hover:text-red-600 px-2 py-1 ml-2 shrink-0">✕</button>
              </div>

              <!-- Section content (DnD inside ContentList) -->
              <ContentList :items="section.content" :store="store" />
              <div class="flex gap-2 mt-3 flex-wrap">
                <button @click="store.addContent(section.content, 'text')" class="btn-content">+ Text</button>
                <button @click="store.addContent(section.content, 'gambar')" class="btn-content">+ Image</button>
                <button @click="store.addContent(section.content, 'tabel')" class="btn-content">+ Table</button>
                <button @click="store.addContent(section.content, 'rumus')" class="btn-content">+ Formula</button>
              </div>

              <!-- Subsections (drag-and-drop) -->
              <draggable :list="section.subsections" :item-key="stableKey" animation="150" handle=".sub-drag" class="space-y-3 mt-4">
                <template #item="{ element: sub, index: subIdx }">
                  <div class="ml-4 border-l-2 border-blue-200 pl-4">
                    <div class="flex items-center justify-between mb-2">
                      <div class="flex items-center gap-2 flex-1 min-w-0">
                        <span class="sub-drag cursor-grab active:cursor-grabbing text-gray-300 hover:text-gray-500 select-none shrink-0">⠿</span>
                        <span class="text-xs font-bold text-blue-500 bg-blue-50 px-1.5 py-0.5 rounded shrink-0">
                          {{ String.fromCharCode(65 + subIdx) }}
                        </span>
                        <input v-model="sub.title" class="input-sm flex-1 font-medium min-w-0"
                          placeholder="Subsection Title" />
                      </div>
                      <button @click="store.removeSubsection(sIdx, subIdx)"
                        class="text-xs text-red-400 hover:text-red-600 px-2 py-1 ml-2 shrink-0">✕</button>
                    </div>
                    <!-- Subsection content (DnD inside ContentList) -->
                    <ContentList :items="sub.content" :store="store" />
                    <div class="flex gap-2 mt-2 flex-wrap">
                      <button @click="store.addContent(sub.content, 'text')" class="btn-content text-xs">+ Text</button>
                      <button @click="store.addContent(sub.content, 'gambar')" class="btn-content text-xs">+ Image</button>
                      <button @click="store.addContent(sub.content, 'tabel')" class="btn-content text-xs">+ Table</button>
                      <button @click="store.addContent(sub.content, 'rumus')" class="btn-content text-xs">+ Formula</button>
                    </div>
                  </div>
                </template>
              </draggable>

              <button @click="store.addSubsection(sIdx)"
                class="mt-3 w-full py-2 border border-dashed border-blue-300 rounded-lg text-blue-500 hover:bg-blue-50 text-sm transition-colors">
                + Add Subsection
              </button>
            </div>
          </template>
        </draggable>

        <button @click="store.addSection()"
          class="w-full py-3 border-2 border-dashed border-gray-300 rounded-xl text-gray-400 hover:border-green-400 hover:text-green-600 transition text-sm">
          + Add Section
        </button>

        <!-- References (drag-and-drop) -->
        <div class="card border-l-4 border-l-red-400">
          <div class="flex items-center justify-between mb-3">
            <label class="label !mb-0">References</label>
            <button @click="store.addReference()" class="btn-add">+ Reference</button>
          </div>
          <draggable :list="store.paper.references" :item-key="(_, i) => i" animation="150" handle=".ref-drag" class="space-y-1.5">
            <template #item="{ element: ref, index: i }">
              <div class="flex gap-2 items-center">
                <span class="ref-drag cursor-grab active:cursor-grabbing text-gray-300 hover:text-gray-500 select-none shrink-0">⠿</span>
                <span class="text-[11px] text-gray-400 w-7 text-right shrink-0">[{{ i + 1 }}]</span>
                <input :value="ref" @input="store.paper.references[i] = $event.target.value"
                  class="input-sm flex-1 text-xs" placeholder="Reference text..." />
                <button @click="store.removeReference(i)" class="text-red-300 hover:text-red-500 text-xs shrink-0">✕</button>
              </div>
            </template>
          </draggable>
        </div>

        <div class="h-20"></div>
      </div>

      <!-- TAB: JOURNAL -->
      <div v-show="activeTab === 'journal'">
        <JournalTab />
      </div>

      <!-- TAB: FIGURES -->
      <div v-show="activeTab === 'figures'">
        <FiguresTab />
      </div>

      <!-- TAB: PREVIEW (single column) -->
      <div v-show="activeTab === 'preview'">
        <PreviewTab />
      </div>
    </div>

    <!-- Toast -->
    <Teleport to="body">
      <div v-if="store.toast.show" class="fixed bottom-6 left-1/2 -translate-x-1/2 z-[999]">
        <div :class="['px-4 py-2.5 rounded-lg shadow-lg text-white text-sm font-medium',
          store.toast.type === 'success' ? 'bg-green-600' :
          store.toast.type === 'error' ? 'bg-red-600' : 'bg-blue-600']">
          {{ store.toast.message }}
        </div>
      </div>
    </Teleport>

    <!-- Loading Overlay -->
    <Teleport to="body">
      <div v-if="store.loading || store.aiLoading" class="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
        <div class="bg-white rounded-xl p-8 shadow-2xl text-center max-w-sm mx-4">
          <div class="w-10 h-10 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mx-auto mb-4"></div>
          <p class="text-sm text-gray-700 font-medium">
            {{ store.aiLoading ? store.aiLoadingMessage || 'AI sedang memproses...' : 'Processing...' }}
          </p>
          <p v-if="store.aiLoading" class="text-xs text-gray-400 mt-2">This may take 3–15 minutes.</p>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import draggable from 'vuedraggable'
import { usePaperStore } from '../stores/paper.js'
import AppHeader from '../components/AppHeader.vue'
import ContentList from '../components/ContentList.vue'
import FiguresTab from '../components/FiguresTab.vue'
import JournalTab from '../components/JournalTab.vue'
import PreviewTab from '../components/PreviewTab.vue'

const store = usePaperStore()
const route = useRoute()
const router = useRouter()

const activeTab = ref('editor')
const aiPrompt = ref('')
const newKeyword = ref('')
const autoSaving = ref(false)
const savedOk = ref(false)

const tabs = [
  { id: 'editor', label: '📝 Editor' },
  { id: 'journal', label: '📚 Journal' },
  { id: 'figures', label: '🖼️ Figures' },
  { id: 'preview', label: '👁 Preview' },
]

// ─── Stable drag-and-drop keys ───────────────────────────────────────────
const keyMap = new WeakMap()
let __kc = 0
function stableKey(obj) {
  if (typeof obj !== 'object' || !obj) return String(obj)
  if (!keyMap.has(obj)) keyMap.set(obj, String(++__kc))
  return keyMap.get(obj)
}

// ─── Auto-save (debounced 1.8s) ──────────────────────────────────────────
let autoSaveTimer = null
watch(() => store.paper, async () => {
  if (!store.paper.title?.trim() && !store.currentPaperId) return
  clearTimeout(autoSaveTimer)
  autoSaveTimer = setTimeout(async () => {
    autoSaving.value = true
    savedOk.value = false
    const id = await store.savePaperToDb()
    autoSaving.value = false
    if (id) {
      savedOk.value = true
      if (route.name === 'editor-new') {
        router.replace({ name: 'editor', params: { paperId: id } })
      }
      setTimeout(() => { savedOk.value = false }, 2500)
    }
  }, 1800)
}, { deep: true })

onUnmounted(() => clearTimeout(autoSaveTimer))

// ─── Init ─────────────────────────────────────────────────────────────────
onMounted(async () => {
  const paperId = route.params.paperId
  if (paperId) {
    await store.loadPaperFromDb(paperId)
  } else {
    // New paper — always start blank
    store.newPaper()
    store.currentPaperId = null
  }
})

// ─── Methods ──────────────────────────────────────────────────────────────
function toRoman(num) { return store.toRoman(num) }

function onUploadJson(e) {
  const file = e.target.files?.[0]
  if (file) { store.uploadJson(file); e.target.value = '' }
}

function addKw() {
  if (newKeyword.value.trim()) {
    store.addKeyword(newKeyword.value.trim())
    newKeyword.value = ''
  }
}

async function generateAI() {
  if (!aiPrompt.value.trim()) return
  await store.aiGenerateFullPaper(aiPrompt.value)
}
</script>

<style scoped>
.card { @apply bg-white rounded-xl shadow-sm border p-5; }
.label { @apply block text-sm font-medium text-gray-600 mb-1.5; }
.input { @apply w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 outline-none; }
.input-sm { @apply px-2.5 py-1.5 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 outline-none; }
.btn-add { @apply px-3 py-1 bg-blue-50 hover:bg-blue-100 text-blue-600 rounded-lg text-xs font-medium transition-colors; }
.btn-content { @apply px-2.5 py-1 bg-gray-100 hover:bg-gray-200 text-gray-600 rounded text-xs transition-colors; }
</style>
