<template>
  <div class="py-2">
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-lg font-semibold text-gray-800">Figures</h2>
      <button @click="store.addFigure()"
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium transition-colors">
        + Add Figure
      </button>
    </div>

    <div v-if="store.paper.figures.length === 0" class="text-center py-16 text-gray-400">
      <div class="text-5xl mb-3">🖼️</div>
      <p class="text-sm">No figures yet. Click "+ Add Figure" to add one.</p>
    </div>

    <div class="space-y-6">
      <div v-for="(fig, index) in store.paper.figures" :key="fig.id || index"
        class="bg-white border rounded-2xl overflow-hidden shadow-sm">

        <!-- Figure Header -->
        <div class="flex items-center justify-between px-5 py-3 bg-gray-50 border-b">
          <span class="font-semibold text-blue-700">Fig. {{ index + 1 }}</span>
          <div class="flex items-center gap-2">
            <label class="flex items-center gap-1.5 cursor-pointer select-none text-sm text-gray-600">
              <input type="checkbox" v-model="fig.hasImage" class="w-4 h-4 rounded border-gray-300 text-blue-600" />
              Include image
            </label>
            <button @click="store.removeFigure(index)" class="text-red-400 hover:text-red-600 text-sm transition-colors">✕ Remove</button>
          </div>
        </div>

        <div class="p-5 space-y-4">

          <!-- 1. Caption -->
          <div>
            <label class="block text-xs font-medium text-gray-500 mb-1.5">Image Title / Caption</label>
            <input v-model="fig.caption"
              :placeholder="`Fig. ${index + 1}. Description of the figure...`"
              class="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 outline-none" />
          </div>

          <!-- 2. Image Preview -->
          <div>
            <div
              class="rounded-xl border-2 border-dashed overflow-hidden flex items-center justify-center bg-gray-50 min-h-[200px] relative cursor-pointer group"
              :class="fig.hasImage !== false ? 'border-gray-200 hover:border-blue-400' : 'border-gray-100 opacity-60'"
              @click="fig.hasImage !== false && triggerUpload(index)"
              @dragover.prevent @drop.prevent="fig.hasImage !== false && handleDrop($event, index)"
            >
              <input type="file" :ref="el => fileInputs[index] = el" accept="image/*"
                @change="handleFileChange($event, index)" class="hidden" />

              <!-- Has image -->
              <template v-if="resolveUrl(fig.url) && fig.hasImage !== false">
                <img :src="resolveUrl(fig.url)" class="max-h-64 max-w-full object-contain rounded-lg" alt="Figure" />
                <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors flex items-center justify-center">
                  <span class="opacity-0 group-hover:opacity-100 text-white text-xs font-medium bg-black/60 px-3 py-1 rounded-full transition-opacity">
                    Click to replace
                  </span>
                </div>
              </template>

              <!-- No image yet -->
              <div v-else-if="fig.hasImage !== false" class="text-center p-8">
                <div class="text-4xl mb-2">📷</div>
                <p class="text-sm font-medium text-blue-600">Please upload image</p>
                <p class="text-xs text-gray-400 mt-1">Click here or drag &amp; drop</p>
              </div>

              <!-- Image excluded -->
              <div v-else class="text-center p-8 text-gray-300">
                <div class="text-3xl mb-2">🚫</div>
                <p class="text-xs">No image in export</p>
              </div>
            </div>
          </div>

          <!-- 3. Image Path: dropdown + upload -->
          <div>
            <label class="block text-xs font-medium text-gray-500 mb-1.5">Image Path</label>
            <div class="flex gap-2">
              <select
                class="flex-1 px-3 py-2 border border-gray-200 rounded-lg text-sm bg-white outline-none focus:ring-2 focus:ring-blue-200 focus:border-blue-400"
                @change="onSelectImage($event, index)"
                :value="fig.filename || ''"
              >
                <option value="">— Select uploaded image —</option>
                <option v-for="img in store.paperImages" :key="img.id" :value="img.filename">
                  {{ img.original_name }}
                </option>
              </select>
              <label
                class="px-3 py-2 bg-blue-50 hover:bg-blue-100 text-blue-600 rounded-lg text-sm cursor-pointer shrink-0 transition-colors flex items-center gap-1 font-medium"
                title="Upload new image">
                📤 Upload
                <input type="file" accept="image/*" class="hidden"
                  @change="handleUploadBtn($event, index)" />
              </label>
            </div>
            <p v-if="fig.filename" class="mt-1.5 text-xs text-green-700 bg-green-50 rounded px-2 py-1">
              📷 {{ getImageName(fig.filename) }}
            </p>
          </div>

          <!-- 4. AI Image Prompt -->
          <div>
            <label class="block text-xs font-medium text-gray-500 mb-1.5">AI Image Prompt (for generation)</label>
            <textarea v-model="fig.aiPrompt" rows="2"
              placeholder="Describe the image for AI generation, e.g. Block diagram of the PLC control system..."
              class="w-full px-3 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 outline-none resize-y" />
          </div>

          <!-- Insert tag hint -->
          <div class="bg-blue-50 rounded-lg px-3 py-2 text-xs text-blue-600">
            <strong>Insert in section content:</strong>
            <code class="ml-2 bg-blue-100 px-1.5 py-0.5 rounded font-mono">[FIGURE:figure-{{ index + 1 }}]</code>
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
const BASE = import.meta.env.VITE_API_URL || ''

function resolveUrl(url) {
  if (!url) return ''
  return url.startsWith('http') ? url : `${BASE}${url}`
}

function getImageName(filename) {
  return store.paperImages.find(i => i.filename === filename)?.original_name || filename
}

function onSelectImage(e, idx) {
  const filename = e.target.value
  const fig = store.paper.figures[idx]
  if (!fig) return
  if (!filename) { fig.filename = ''; fig.url = ''; return }
  const img = store.paperImages.find(i => i.filename === filename)
  if (img) { fig.filename = img.filename; fig.url = img.url }
}

function triggerUpload(idx) {
  fileInputs[idx]?.click()
}

async function handleFileChange(e, idx) {
  const file = e.target.files?.[0]
  if (file) {
    await store.uploadImage(idx, file)
    e.target.value = ''
  }
}

async function handleUploadBtn(e, idx) {
  const file = e.target.files?.[0]
  if (file) {
    await store.uploadImage(idx, file)
    e.target.value = ''
  }
}

async function handleDrop(e, idx) {
  const file = e.dataTransfer.files?.[0]
  if (file?.type.startsWith('image/')) await store.uploadImage(idx, file)
}
</script>
