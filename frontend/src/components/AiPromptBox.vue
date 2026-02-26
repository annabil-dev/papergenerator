<template>
  <div class="mt-2 border rounded-lg bg-gray-50 p-3">
    <div class="flex items-center gap-2 mb-2">
      <svg class="w-4 h-4 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
      </svg>
      <span class="text-xs font-medium text-gray-600">AI Prompt — edit this {{ section }}</span>
    </div>
    <div class="flex gap-2">
      <input v-model="prompt" type="text"
        :placeholder="`e.g.: Rewrite to be more formal, Add more detail about methodology...`"
        class="flex-1 px-3 py-1.5 border rounded text-sm focus:ring-2 focus:ring-purple-200 focus:border-purple-400 outline-none"
        @keyup.enter="generate" :disabled="loading" />
      <button @click="generate"
        :disabled="loading || !prompt.trim()"
        class="px-4 py-1.5 bg-purple-600 text-white rounded text-sm hover:bg-purple-700 disabled:opacity-50 flex items-center gap-1">
        <span v-if="loading" class="spinner !w-3 !h-3"></span>
        <span>Send</span>
      </button>
    </div>
    <p class="text-xs text-gray-400 mt-1">Sends current text + your prompt to AI. Result will replace current content.</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { usePaperStore } from '../stores/paper.js'

const props = defineProps({
  section: { type: String, required: true },
  lastText: { type: String, default: '' }
})

const emit = defineEmits(['generated'])
const store = usePaperStore()
const prompt = ref('')
const loading = ref(false)

async function generate() {
  if (!prompt.value.trim()) return
  loading.value = true
  try {
    const result = await store.aiGenerate(prompt.value, props.section, props.lastText)
    if (result) {
      emit('generated', result.trim())
      prompt.value = ''
    }
  } finally {
    loading.value = false
  }
}
</script>
