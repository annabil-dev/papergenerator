<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header -->
    <header class="bg-gradient-to-r from-blue-700 to-blue-900 text-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <h1 class="text-xl font-bold">Paper Generator</h1>
          <span class="text-xs bg-blue-600 px-2 py-0.5 rounded">IEEE Format</span>
        </div>
        <div class="flex items-center gap-2">
          <!-- New -->
          <button @click="store.newPaper()"
            class="px-3 py-1.5 bg-gray-600 hover:bg-gray-500 rounded text-sm flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 4v16m8-8H4" />
            </svg>
            New
          </button>

          <!-- Upload JSON -->
          <label class="px-3 py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-sm flex items-center gap-1 cursor-pointer">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
            Upload JSON
            <input type="file" accept=".json" class="hidden" @change="onUploadJson" />
          </label>

          <!-- Save JSON -->
          <button @click="store.downloadJson()"
            class="px-3 py-1.5 bg-green-600 hover:bg-green-500 rounded text-sm flex items-center gap-1">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            Save JSON
          </button>

          <button @click="store.exportDocx()"
            class="px-3 py-1.5 bg-orange-600 hover:bg-orange-500 rounded text-sm flex items-center gap-1"
            :disabled="store.loading">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            Export DOCX
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 py-4">
      <!-- AI Full Paper Generator -->
      <div class="bg-white rounded-xl shadow-sm border mb-4 p-4">
        <div class="flex items-center gap-2 mb-3">
          <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          <h2 class="text-lg font-semibold text-gray-800">Generate Full Paper with AI</h2>
        </div>
        <div class="flex gap-2">
          <input v-model="fullPaperPrompt" type="text" placeholder="Enter topic, e.g.: Lane Detection Algorithm Based on Haar Feature Based Coupled Cascade Classifier"
            class="flex-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-purple-300 focus:border-purple-500 outline-none text-sm"
            @keyup.enter="generateFullPaper" :disabled="store.aiLoading" />
          <button @click="generateFullPaper"
            class="px-6 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 disabled:opacity-50 flex items-center gap-2 text-sm font-medium"
            :disabled="store.aiLoading || !fullPaperPrompt.trim()">
            <span v-if="store.aiLoading" class="spinner"></span>
            <span v-else>🤖 Generate</span>
          </button>
        </div>
      </div>

      <!-- Tabs -->
      <div class="flex gap-1 mb-4 bg-white rounded-xl shadow-sm border p-1 overflow-x-auto">
        <button v-for="tab in tabs" :key="tab.id"
          @click="store.activeTab = tab.id"
          :class="[
            'px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all',
            store.activeTab === tab.id
              ? 'bg-blue-600 text-white shadow-sm'
              : 'text-gray-600 hover:bg-gray-100'
          ]">
          {{ tab.label }}
        </button>
      </div>

      <!-- Tab Content -->
      <div class="bg-white rounded-xl shadow-sm border">
        <MetadataTab v-if="store.activeTab === 'metadata'" />
        <SectionsTab v-if="store.activeTab === 'sections'" />
        <FiguresTab v-if="store.activeTab === 'figures'" />
        <TablesTab v-if="store.activeTab === 'tables'" />
        <EquationsTab v-if="store.activeTab === 'equations'" />
        <ReferencesTab v-if="store.activeTab === 'references'" />
        <PreviewTab v-if="store.activeTab === 'preview'" />
      </div>
    </div>

    <!-- Toast — z-[60] so it appears above the loading overlay (z-50) -->
    <div v-if="store.toast.show" class="toast" style="z-index:9999; right:auto; bottom:24px; left:50%; transform:translateX(-50%)">
      <div :class="[
        'px-4 py-3 rounded-lg shadow-lg text-white text-sm flex items-center gap-2',
        store.toast.type === 'success' ? 'bg-green-600' :
        store.toast.type === 'error' ? 'bg-red-600' : 'bg-blue-600'
      ]">
        <span>{{ store.toast.message }}</span>
      </div>
    </div>

    <!-- DOCX Export Overlay -->
    <div v-if="store.loading" class="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-8 shadow-2xl flex flex-col items-center gap-4 min-w-72 max-w-sm w-full mx-4">
        <div class="w-12 h-12 border-4 border-orange-200 border-t-orange-500 rounded-full animate-spin"></div>
        <span class="text-sm text-gray-700 text-center font-medium">Generating DOCX...</span>
        <div class="w-full bg-gray-100 rounded-full h-1.5 overflow-hidden">
          <div class="h-full bg-orange-400 rounded-full animate-pulse" style="width: 70%"></div>
        </div>
        <p class="text-xs text-gray-400 text-center">Harap tunggu, sedang membuat dokumen Word.</p>
      </div>
    </div>

    <!-- AI Loading Overlay — z-50, shows live progress message -->
    <div v-if="store.aiLoading" class="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-8 shadow-2xl flex flex-col items-center gap-4 min-w-72 max-w-sm w-full mx-4">
        <div class="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
        <span class="text-sm text-gray-700 text-center font-medium">
          {{ store.aiLoadingMessage || 'AI sedang memproses...' }}
        </span>
        <div class="w-full bg-gray-100 rounded-full h-1.5 overflow-hidden">
          <div class="h-full bg-blue-500 rounded-full animate-pulse" style="width: 85%"></div>
        </div>
        <p class="text-xs text-gray-400 text-center">
          Proses ini membutuhkan 3–7 menit.<br>Halaman ini akan diperbarui otomatis.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { usePaperStore } from './stores/paper.js'
import MetadataTab from './components/MetadataTab.vue'
import SectionsTab from './components/SectionsTab.vue'
import FiguresTab from './components/FiguresTab.vue'
import TablesTab from './components/TablesTab.vue'
import EquationsTab from './components/EquationsTab.vue'
import ReferencesTab from './components/ReferencesTab.vue'
import PreviewTab from './components/PreviewTab.vue'

const store = usePaperStore()
const fullPaperPrompt = ref('')

function onUploadJson(event) {
  const file = event.target.files?.[0]
  if (file) {
    store.uploadJson(file)
    event.target.value = ''  // reset so same file can be re-uploaded
  }
}

const tabs = [
  { id: 'metadata', label: '📝 Title & Authors' },
  { id: 'sections', label: '📄 Sections' },
  { id: 'figures', label: '🖼️ Figures' },
  { id: 'tables', label: '📊 Tables' },
  { id: 'equations', label: '📐 Equations' },
  { id: 'references', label: '📚 References' },
  { id: 'preview', label: '👁️ Preview' }
]

async function generateFullPaper() {
  if (!fullPaperPrompt.value.trim()) return
  await store.aiGenerateFullPaper(fullPaperPrompt.value)
}

onMounted(() => {
  store.loadPaperList()
})
</script>
