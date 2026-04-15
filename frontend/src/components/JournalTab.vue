<template>
  <div class="max-w-3xl">
    <div class="bg-white rounded-2xl border shadow-sm p-6">
      <h2 class="text-lg font-semibold text-gray-800">Journal</h2>
      <p class="text-sm text-gray-500 mt-1">
        Choose the target journal template for DOCX export.
      </p>

      <div class="mt-5">
        <label class="block text-sm font-medium text-gray-700 mb-2">Export format</label>
        <select
          v-model="store.paper.journal"
          class="w-full max-w-md px-3 py-2 border border-gray-200 rounded-xl text-sm bg-white focus:ring-2 focus:ring-blue-200 outline-none"
          :disabled="store.journalsLoading"
        >
          <option v-if="store.journalsLoading" value="">Loading templates...</option>
          <option v-for="j in store.availableJournals" :key="j" :value="j">
            {{ j }}
          </option>
        </select>

        <p class="text-xs text-gray-400 mt-3">
          This selection controls which template generator is used when you click DOCX export.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { usePaperStore } from '../stores/paper.js'

const store = usePaperStore()

onMounted(() => {
  store.fetchJournals()
})
</script>
