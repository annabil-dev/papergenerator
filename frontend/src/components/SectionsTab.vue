<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-lg font-semibold text-gray-800">Paper Sections</h2>
      <button @click="store.addSection()"
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium">
        + Add Section
      </button>
    </div>

    <div v-if="store.paper.sections.length === 0"
      class="text-center py-12 text-gray-400">
      <svg class="w-12 h-12 mx-auto mb-3 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
      <p>No sections yet. Add a section or generate a full paper.</p>
    </div>

    <!-- Sections List -->
    <div v-for="(section, sIdx) in store.paper.sections" :key="section.id"
      class="border rounded-xl mb-4 overflow-hidden">

      <!-- Section Header -->
      <div class="bg-blue-50 px-4 py-3 flex items-center justify-between cursor-pointer"
        @click="toggleSection(sIdx)">
        <div class="flex items-center gap-2">
          <svg :class="['w-4 h-4 transition-transform', expandedSections[sIdx] ? 'rotate-90' : '']"
            fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
          <span class="font-bold text-blue-800">{{ section.number }}.</span>
          <input v-model="section.title" placeholder="Section Title (e.g. INTRODUCTION)"
            class="bg-transparent font-semibold text-blue-900 focus:outline-none focus:bg-white px-2 py-0.5 rounded"
            @click.stop />
        </div>
        <div class="flex items-center gap-2">
          <AiButton @click.stop="aiSection(sIdx)" label="AI" :loading="store.aiLoading" />
          <button @click.stop="store.addSubsection(sIdx)"
            class="text-xs bg-green-100 text-green-700 px-2 py-1 rounded hover:bg-green-200">+ Sub</button>
          <button @click.stop="store.removeSection(sIdx)"
            class="text-xs text-red-400 hover:text-red-600">✕ Remove</button>
        </div>
      </div>

      <!-- Section Content -->
      <div v-show="expandedSections[sIdx]" class="p-4 space-y-4">
        <div>
          <label class="block text-xs text-gray-500 mb-1">Section Content</label>
          <textarea v-model="section.content" rows="6"
            placeholder="Write section content... Use [1], [2] for citations. Use $$formula$$ for equations."
            class="w-full px-3 py-2 border rounded-lg text-sm focus:ring-2 focus:ring-blue-200 outline-none resize-y font-serif"></textarea>
          <AiPromptBox :section="section.title || 'section'" :lastText="section.content"
            @generated="(text) => section.content = text" />
        </div>

        <!-- Subsections -->
        <div v-for="(sub, subIdx) in section.subsections" :key="sub.id"
          class="border-l-4 border-blue-300 pl-4 ml-2 space-y-3">

          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="font-semibold text-blue-700 text-sm">{{ sub.letter }}.</span>
              <input v-model="sub.title" placeholder="Subsection Title"
                class="font-medium text-sm bg-transparent focus:outline-none focus:bg-white px-2 py-0.5 rounded border-b border-gray-200" />
            </div>
            <div class="flex items-center gap-2">
              <AiButton @click="aiSubsection(sIdx, subIdx)" label="AI" :loading="store.aiLoading" />
              <button @click="store.addNumberedItem(sIdx, subIdx)"
                class="text-xs bg-purple-100 text-purple-700 px-2 py-1 rounded hover:bg-purple-200"># Item</button>
              <button @click="store.removeSubsection(sIdx, subIdx)"
                class="text-xs text-red-400 hover:text-red-600">✕</button>
            </div>
          </div>

          <textarea v-model="sub.content" rows="4"
            placeholder="Subsection content..."
            class="w-full px-3 py-2 border rounded text-sm focus:ring-2 focus:ring-blue-200 outline-none resize-y font-serif"></textarea>
          <AiPromptBox :section="sub.title || 'subsection'" :lastText="sub.content"
            @generated="(text) => sub.content = text" />

          <!-- Numbered Items (like "1) Weak Classifier Design") -->
          <div v-for="(item, itemIdx) in sub.numberedItems" :key="itemIdx"
            class="border-l-4 border-purple-200 pl-3 ml-2 space-y-2">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-sm font-semibold text-purple-700">{{ item.number }})</span>
                <input v-model="item.title" placeholder="Item Title"
                  class="text-sm bg-transparent focus:outline-none focus:bg-white px-2 py-0.5 rounded border-b border-gray-200" />
              </div>
              <div class="flex items-center gap-1">
                <AiButton @click="aiNumberedItem(sIdx, subIdx, itemIdx)" label="AI" :loading="store.aiLoading" />
                <button @click="store.removeNumberedItem(sIdx, subIdx, itemIdx)"
                  class="text-xs text-red-400 hover:text-red-600">✕</button>
              </div>
            </div>
            <textarea v-model="item.content" rows="3"
              placeholder="Item content..."
              class="w-full px-3 py-2 border rounded text-sm focus:ring-2 focus:ring-purple-200 outline-none resize-y font-serif"></textarea>
            <AiPromptBox :section="item.title || 'item'" :lastText="item.content"
              @generated="(text) => item.content = text" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { usePaperStore } from '../stores/paper.js'
import AiButton from './AiButton.vue'
import AiPromptBox from './AiPromptBox.vue'

const store = usePaperStore()
const expandedSections = reactive({})

function toggleSection(idx) {
  expandedSections[idx] = !expandedSections[idx]
}

async function aiSection(sIdx) {
  const section = store.paper.sections[sIdx]
  const result = await store.aiGenerate(
    `Write the content for section "${section.number}. ${section.title}" of this IEEE conference paper. Write detailed, formal academic content with citations [1], [2] etc.`,
    section.title || 'section',
    section.content
  )
  if (result) section.content = result.trim()
}

async function aiSubsection(sIdx, subIdx) {
  const sub = store.paper.sections[sIdx].subsections[subIdx]
  const parentTitle = store.paper.sections[sIdx].title
  const result = await store.aiGenerate(
    `Write the content for subsection "${sub.letter}. ${sub.title}" under section "${parentTitle}". Write detailed academic content.`,
    sub.title || 'subsection',
    sub.content
  )
  if (result) sub.content = result.trim()
}

async function aiNumberedItem(sIdx, subIdx, itemIdx) {
  const item = store.paper.sections[sIdx].subsections[subIdx].numberedItems[itemIdx]
  const result = await store.aiGenerate(
    `Write the content for "${item.number}) ${item.title}". Write formal academic content with technical detail.`,
    item.title || 'item',
    item.content
  )
  if (result) item.content = result.trim()
}
</script>
