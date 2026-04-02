<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-lg font-semibold text-gray-800">Paper Preview</h2>
      <button @click="store.exportDocx()"
        class="px-4 py-2 bg-orange-600 text-white rounded-lg hover:bg-orange-700 text-sm font-medium flex items-center gap-2">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        Export DOCX
      </button>
    </div>

    <!-- IEEE Paper Preview -->
    <div class="paper-preview border rounded-lg" ref="previewEl">
      <!-- Title -->
      <h1 class="text-2xl font-bold text-center mb-4 leading-tight" style="font-family: 'Times New Roman', serif;">
        {{ store.paper.title || 'Paper Title' }}
      </h1>

      <!-- Authors -->
      <div class="text-center mb-6">
        <div v-for="(author, i) in store.paper.authors" :key="i" class="mb-2">
          <div class="text-sm" style="font-family: 'Times New Roman', serif;">{{ author.name }}</div>
          <div class="text-xs italic text-gray-600" style="font-family: 'Times New Roman', serif;">
            {{ author.affiliation }}
          </div>
          <div v-if="author.location" class="text-xs italic text-gray-600" style="font-family: 'Times New Roman', serif;">
            {{ author.location }}
          </div>
          <div v-if="author.email" class="text-xs italic text-gray-600" style="font-family: 'Times New Roman', serif;">
            e-mail: {{ author.email }}
          </div>
        </div>
      </div>

      <!-- Abstract -->
      <div v-if="store.paper.abstract" class="mb-4 text-justify" style="font-family: 'Times New Roman', serif; font-size: 9pt;">
        <span class="font-bold italic">Abstract—</span>
        <span class="italic">{{ store.paper.abstract }}</span>
      </div>

      <!-- Keywords -->
      <div v-if="store.paper.keywords.length > 0" class="mb-6 text-justify" style="font-family: 'Times New Roman', serif; font-size: 9pt;">
        <span class="font-bold italic">Keywords—</span>
        <span class="italic">{{ store.paper.keywords.join(', ') }}</span>
      </div>

      <!-- Single-column layout -->
      <div class="space-y-4" style="font-family: 'Times New Roman', serif; font-size: 10pt;">
        <!-- Sections -->
        <div v-for="section in store.paper.sections" :key="section.id" class="mb-4">
          <h2 class="text-center font-bold mb-2 text-sm">
            {{ section.number }}. {{ section.title?.toUpperCase() }}
          </h2>
          <div class="text-justify indent-6 whitespace-pre-wrap text-sm leading-snug">{{ section.content }}</div>

          <!-- Subsections -->
          <div v-for="sub in section.subsections" :key="sub.id" class="mt-3">
            <h3 class="font-bold italic text-sm mb-1">
              {{ sub.letter }}. {{ sub.title }}
            </h3>
            <div class="text-justify indent-6 whitespace-pre-wrap text-sm leading-snug">{{ sub.content }}</div>

            <div v-for="item in sub.numberedItems" :key="item.number" class="mt-2 ml-4">
              <span class="font-bold italic text-sm">{{ item.number }}) {{ item.title }}</span>
              <div class="text-justify indent-6 whitespace-pre-wrap text-sm leading-snug">{{ item.content }}</div>
            </div>
          </div>
        </div>

        <!-- Acknowledgment -->
        <div v-if="store.paper.acknowledgment" class="mb-4">
          <h2 class="text-center font-bold mb-2 text-sm">ACKNOWLEDGMENT</h2>
          <div class="text-justify indent-6 whitespace-pre-wrap text-sm leading-snug">{{ store.paper.acknowledgment }}</div>
        </div>

        <!-- References -->
        <div v-if="store.paper.references.length > 0">
          <h2 class="text-center font-bold mb-2 text-sm">REFERENCES</h2>
          <div v-for="ref in store.paper.references" :key="ref.id"
            class="text-xs leading-snug mb-1 pl-6 -indent-6">
            [{{ ref.id }}] {{ ref.text }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { usePaperStore } from '../stores/paper.js'
const store = usePaperStore()
</script>
