<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-lg font-semibold text-gray-800">Figures</h2>
      <button @click="store.addFigure()"
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium">
        + Add Figure
      </button>
    </div>

    <p class="text-sm text-gray-500 mb-4">
      Upload images and add captions. Reference figures in section content using
      <code class="bg-gray-100 px-1 rounded">[FIGURE:figure-1]</code>
    </p>

    <div v-if="store.paper.figures.length === 0"
      class="text-center py-12 text-gray-400">
      <svg class="w-12 h-12 mx-auto mb-3 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
      </svg>
      <p>No figures yet. Add a figure to include images in your paper.</p>
    </div>

    <div v-for="(fig, index) in store.paper.figures" :key="fig.id"
      class="border rounded-xl p-4 mb-4 bg-gray-50">
      <div class="flex items-start justify-between mb-3">
        <span class="text-sm font-semibold text-blue-700">{{ fig.id }}</span>
        <button @click="store.removeFigure(index)"
          class="text-red-400 hover:text-red-600 text-sm">✕ Remove</button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Image Upload -->
        <div>
          <label class="block text-xs text-gray-500 mb-1">Image</label>
          <div class="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center hover:border-blue-400 cursor-pointer transition-colors"
            @click="triggerUpload(index)"
            @dragover.prevent @drop.prevent="handleDrop($event, index)">
            <input type="file" :ref="el => fileInputs[index] = el" accept="image/*"
              @change="handleFileChange($event, index)" class="hidden" />
            <div v-if="fig.url">
              <img :src="fig.url" class="max-h-40 mx-auto rounded" alt="Figure" />
              <p class="text-xs text-gray-400 mt-1">Click to replace</p>
            </div>
            <div v-else>
              <svg class="w-8 h-8 mx-auto text-gray-300 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              <p class="text-sm text-gray-400">Click or drag image here</p>
            </div>
          </div>
        </div>

        <!-- Caption -->
        <div>
          <label class="block text-xs text-gray-500 mb-1">Caption</label>
          <input v-model="fig.caption" placeholder="Fig. 1. Algorithm Flow"
            class="w-full px-3 py-1.5 border rounded text-sm mb-2" />
          <div class="bg-blue-50 rounded p-2">
            <p class="text-xs text-blue-600">
              <strong>Usage in sections:</strong><br>
              Insert <code class="bg-blue-100 px-1 rounded">{{ `[FIGURE:${fig.id}]` }}</code> in section content to place this figure.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { usePaperStore } from '../stores/paper.js'

const store = usePaperStore()
const fileInputs = reactive({})

function triggerUpload(index) {
  fileInputs[index]?.click()
}

async function handleFileChange(event, index) {
  const file = event.target.files?.[0]
  if (file) {
    await store.uploadImage(index, file)
  }
}

async function handleDrop(event, index) {
  const file = event.dataTransfer.files?.[0]
  if (file && file.type.startsWith('image/')) {
    await store.uploadImage(index, file)
  }
}
</script>
