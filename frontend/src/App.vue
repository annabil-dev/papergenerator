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
          <!-- Saved Papers Dropdown -->
          <div class="relative" ref="dropdownRef">
            <button @click="showPaperList = !showPaperList"
              class="px-3 py-1.5 bg-blue-600 hover:bg-blue-500 rounded text-sm flex items-center gap-1">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
              </svg>
              Papers
            </button>
            <div v-if="showPaperList"
              class="absolute right-0 top-full mt-1 w-72 bg-white rounded-lg shadow-xl z-50 text-gray-800 border">
              <div class="p-2 border-b flex justify-between items-center">
                <span class="text-sm font-semibold">Saved Papers</span>
                <button @click="store.newPaper(); showPaperList = false"
                  class="text-xs bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600">+ New</button>
              </div>
              <div class="max-h-60 overflow-y-auto">
                <div v-if="store.savedPapers.length === 0" class="p-3 text-sm text-gray-400 text-center">
                  No saved papers
                </div>
                <div v-for="p in store.savedPapers" :key="p.id"
                  class="flex items-center justify-between px-3 py-2 hover:bg-gray-50 cursor-pointer border-b last:border-0"
                  @click="store.loadPaper(p.id); showPaperList = false">
                  <div class="flex-1 min-w-0">
                    <div class="text-sm font-medium truncate">{{ p.title || 'Untitled' }}</div>
                    <div class="text-xs text-gray-400">{{ new Date(p.modified).toLocaleDateString() }}</div>
                  </div>
                  <button @click.stop="store.deletePaper(p.id)"
                    class="ml-2 text-red-400 hover:text-red-600 text-xs">✕</button>
                </div>
              </div>
            </div>
          </div>

          <button @click="store.savePaper()"
            class="px-3 py-1.5 bg-green-600 hover:bg-green-500 rounded text-sm flex items-center gap-1"
            :disabled="store.loading">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
            </svg>
            Save
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

    <!-- Toast -->
    <div v-if="store.toast.show" class="toast">
      <div :class="[
        'px-4 py-3 rounded-lg shadow-lg text-white text-sm flex items-center gap-2',
        store.toast.type === 'success' ? 'bg-green-600' :
        store.toast.type === 'error' ? 'bg-red-600' : 'bg-blue-600'
      ]">
        <span>{{ store.toast.message }}</span>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="store.aiLoading" class="fixed inset-0 bg-black/30 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 shadow-2xl flex flex-col items-center gap-3">
        <div class="w-10 h-10 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin"></div>
        <span class="text-sm text-gray-600">AI is generating content...</span>
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
const showPaperList = ref(false)

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
