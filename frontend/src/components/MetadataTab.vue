<template>
  <div class="p-6 space-y-6">
    <!-- Title -->
    <div>
      <label class="block text-sm font-semibold text-gray-700 mb-1">Paper Title</label>
      <div class="flex gap-2">
        <input v-model="store.paper.title" type="text"
          placeholder="e.g.: Lane Detection Algorithm Based on Haar Feature Based Coupled Cascade Classifier"
          class="flex-1 px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-300 focus:border-blue-500 outline-none" />
        <AiButton @click="aiTitle" label="AI" :loading="store.aiLoading" />
      </div>
    </div>

    <!-- Authors -->
    <div>
      <div class="flex items-center justify-between mb-2">
        <label class="text-sm font-semibold text-gray-700">Authors</label>
        <button @click="store.addAuthor()"
          class="text-sm bg-blue-100 text-blue-700 px-3 py-1 rounded-lg hover:bg-blue-200">+ Add Author</button>
      </div>
      <div v-for="(author, index) in store.paper.authors" :key="index"
        class="border rounded-lg p-4 mb-3 bg-gray-50 relative">
        <button v-if="store.paper.authors.length > 1" @click="store.removeAuthor(index)"
          class="absolute top-2 right-2 text-red-400 hover:text-red-600 text-lg">✕</button>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs text-gray-500 mb-1">Name</label>
            <input v-model="author.name" placeholder="Full Name" class="w-full px-3 py-1.5 border rounded text-sm" />
          </div>
          <div>
            <label class="block text-xs text-gray-500 mb-1">Email</label>
            <input v-model="author.email" placeholder="email@example.com"
              class="w-full px-3 py-1.5 border rounded text-sm" />
          </div>
          <div>
            <label class="block text-xs text-gray-500 mb-1">Affiliation</label>
            <input v-model="author.affiliation" placeholder="University / Institute"
              class="w-full px-3 py-1.5 border rounded text-sm" />
          </div>
          <div>
            <label class="block text-xs text-gray-500 mb-1">Location</label>
            <input v-model="author.location" placeholder="City, Country"
              class="w-full px-3 py-1.5 border rounded text-sm" />
          </div>
        </div>
      </div>
    </div>

    <!-- Abstract -->
    <div>
      <div class="flex items-center justify-between mb-1">
        <label class="text-sm font-semibold text-gray-700">Abstract</label>
        <AiButton @click="aiAbstract" label="AI Generate" :loading="store.aiLoading" />
      </div>
      <textarea v-model="store.paper.abstract" rows="5"
        placeholder="Write or generate abstract..."
        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-300 focus:border-blue-500 outline-none text-sm resize-y"></textarea>
      <!-- AI Prompt for Abstract -->
      <AiPromptBox section="abstract" :lastText="store.paper.abstract"
        @generated="(text) => store.paper.abstract = text" />
    </div>

    <!-- Keywords -->
    <div>
      <label class="block text-sm font-semibold text-gray-700 mb-1">Keywords</label>
      <div class="flex flex-wrap gap-2 mb-2">
        <span v-for="(kw, i) in store.paper.keywords" :key="i"
          class="inline-flex items-center bg-blue-100 text-blue-800 text-sm px-3 py-1 rounded-full">
          {{ kw }}
          <button @click="store.removeKeyword(i)" class="ml-1 text-blue-500 hover:text-blue-700">✕</button>
        </span>
      </div>
      <div class="flex gap-2">
        <input v-model="newKeyword" placeholder="Add keyword..." @keyup.enter="addKw"
          class="flex-1 px-3 py-1.5 border rounded text-sm" />
        <button @click="addKw" class="px-4 py-1.5 bg-blue-600 text-white rounded text-sm hover:bg-blue-700">Add</button>
      </div>
    </div>

    <!-- Acknowledgment -->
    <div>
      <div class="flex items-center justify-between mb-1">
        <label class="text-sm font-semibold text-gray-700">Acknowledgment</label>
        <AiButton @click="aiAck" label="AI Generate" :loading="store.aiLoading" />
      </div>
      <textarea v-model="store.paper.acknowledgment" rows="3"
        placeholder="Acknowledgment text..."
        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-300 focus:border-blue-500 outline-none text-sm resize-y"></textarea>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { usePaperStore } from '../stores/paper.js'
import AiButton from './AiButton.vue'
import AiPromptBox from './AiPromptBox.vue'

const store = usePaperStore()
const newKeyword = ref('')

function addKw() {
  if (newKeyword.value.trim()) {
    store.addKeyword(newKeyword.value.trim())
    newKeyword.value = ''
  }
}

async function aiTitle() {
  const result = await store.aiGenerate(
    'Generate a concise, descriptive IEEE paper title for this paper. Return only the title text.',
    'title',
    store.paper.title
  )
  if (result) store.paper.title = result.trim()
}

async function aiAbstract() {
  const result = await store.aiGenerate(
    'Generate an IEEE conference paper abstract (150-250 words). Include the problem, proposed method, key results.',
    'abstract',
    store.paper.abstract
  )
  if (result) store.paper.abstract = result.trim()
}

async function aiAck() {
  const result = await store.aiGenerate(
    'Generate an acknowledgment section for this IEEE paper. Mention funding support if applicable.',
    'acknowledgment',
    store.paper.acknowledgment
  )
  if (result) store.paper.acknowledgment = result.trim()
}
</script>
