<template>
  <draggable :list="items" :item-key="stableKey" animation="150" handle=".content-drag" class="space-y-2">
    <template #item="{ element: item, index: idx }">
    <div class="bg-white border rounded-lg p-3 relative group">

      <!-- Item header -->
      <div class="flex items-center justify-between mb-1.5">
        <div class="flex items-center gap-1.5">
          <span class="content-drag cursor-grab active:cursor-grabbing text-gray-300 hover:text-gray-500 select-none text-base leading-none px-0.5">⠿</span>
          <span class="text-[10px] font-semibold uppercase tracking-wide px-1.5 py-0.5 rounded"
            :class="badgeClass(item.id)">
            {{ badgeLabel(item, idx) }}
          </span>
        </div>
        <button @click="store.removeContent(items, idx)"
          class="text-red-300 hover:text-red-500 text-xs px-1 opacity-60 group-hover:opacity-100">✕</button>
      </div>

      <!-- TEXT -->
      <template v-if="item.id === 'text'">
        <textarea v-model="item.text" rows="4"
          class="w-full px-2.5 py-2 border border-gray-200 rounded text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 outline-none resize-y font-serif"
          placeholder="Write text content... Use [1], [2] for citations."></textarea>
      </template>

      <!-- IMAGE / GAMBAR -->
      <template v-else-if="item.id === 'gambar'">
        <div class="space-y-2">
          <input v-model="item.Title" class="w-full px-2.5 py-1.5 border border-gray-200 rounded text-sm outline-none focus:border-blue-400"
            placeholder="Image Title / Caption" />
          <div class="flex gap-2">
            <select
              class="flex-1 px-2.5 py-1.5 border border-gray-200 rounded text-sm bg-white outline-none focus:border-blue-400"
              @change="onSelectContentImage($event, item)">
              <option value="">— Select image —</option>
              <option v-for="img in store.paperImages" :key="img.id" :value="img.filename">
                {{ img.original_name }}
              </option>
            </select>
            <label class="px-2.5 py-1.5 bg-blue-50 hover:bg-blue-100 text-blue-600 rounded text-xs cursor-pointer shrink-0 flex items-center gap-1 font-medium">
              📤
              <input type="file" accept="image/*" class="hidden" @change="uploadContentImage($event, item)" />
            </label>
          </div>
          <p v-if="item.Path" class="text-xs text-green-700 bg-green-50 rounded px-2 py-1">📷 {{ item.Path }}</p>
          <textarea v-model="item.Prompt" rows="2"
            class="w-full px-2.5 py-1.5 border border-gray-200 rounded text-xs outline-none focus:border-blue-400 resize-y text-gray-600"
            placeholder="AI Image Prompt (for generation)"></textarea>
        </div>
      </template>

      <!-- TABLE / TABEL -->
      <template v-else-if="item.id === 'tabel'">
        <div class="space-y-2">
          <input v-model="item.Title" class="w-full px-2.5 py-1.5 border border-gray-200 rounded text-sm outline-none focus:border-blue-400"
            placeholder="Table Title" />
          <div class="overflow-x-auto">
            <table class="w-full text-xs border-collapse">
              <thead>
                <tr>
                  <th v-for="(h, ci) in item.Headers" :key="ci"
                    class="border border-gray-200 bg-gray-50 p-0 relative">
                    <input :value="h" @input="item.Headers[ci] = $event.target.value"
                      class="w-full px-2 py-1.5 text-xs font-semibold bg-transparent outline-none text-center" />
                    <button v-if="item.Headers.length > 1"
                      @click="store.removeTableCol(item, ci)"
                      class="absolute -top-2 -right-2 bg-red-400 text-white rounded-full w-4 h-4 text-[10px] leading-none opacity-0 group-hover:opacity-100">✕</button>
                  </th>
                  <th class="w-8">
                    <button @click="store.addTableCol(item)"
                      class="text-blue-400 hover:text-blue-600 text-xs">+</button>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(row, ri) in item.Rows" :key="ri">
                  <td v-for="(cell, ci) in row" :key="ci" class="border border-gray-200 p-0">
                    <input :value="cell" @input="item.Rows[ri][ci] = $event.target.value"
                      class="w-full px-2 py-1 text-xs bg-transparent outline-none" />
                  </td>
                  <td class="w-8 text-center">
                    <button @click="store.removeTableRow(item, ri)"
                      class="text-red-300 hover:text-red-500 text-[10px]">✕</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <button @click="store.addTableRow(item)"
            class="text-xs text-blue-500 hover:text-blue-700">+ Add Row</button>
        </div>
      </template>

      <!-- FORMULA / RUMUS -->
      <template v-else-if="item.id === 'rumus'">
        <input v-model="item.latex" class="w-full px-2.5 py-1.5 border border-gray-200 rounded text-sm font-mono outline-none focus:border-blue-400"
          placeholder="LaTeX formula, e.g. T_{total} \approx \max(T_{cap}, T_{inf}, T_{modbus})" />
        <div v-if="item.latex" class="mt-1.5 text-xs text-gray-400 font-mono bg-gray-50 px-2 py-1 rounded">
          Preview: {{ item.latex }}
        </div>
      </template>
    </div>
    </template>
  </draggable>
</template>

<script setup>
import draggable from 'vuedraggable'
import { usePaperStore } from '../stores/paper.js'

const props = defineProps({
  items: { type: Array, required: true },
  store: { type: Object, required: true }
})

const store = usePaperStore()

const keyMap = new WeakMap()
let __kc = 0
function stableKey(obj) {
  if (typeof obj !== 'object' || !obj) return String(obj)
  if (!keyMap.has(obj)) keyMap.set(obj, String(++__kc))
  return keyMap.get(obj)
}

function badgeClass(id) {
  const map = {
    text: 'bg-gray-100 text-gray-500',
    gambar: 'bg-amber-50 text-amber-600',
    tabel: 'bg-emerald-50 text-emerald-600',
    rumus: 'bg-violet-50 text-violet-600'
  }
  return map[id] || 'bg-gray-100 text-gray-500'
}

function badgeLabel(item, idx) {
  const nums = store.getItemNumber(item)
  if (item.id === 'gambar') return `Fig. ${nums.label || '?'}`
  if (item.id === 'tabel') return `Table ${nums.label || '?'}`
  if (item.id === 'rumus') return `Eq. (${nums.label || '?'})`
  return 'Text'
}

function onSelectContentImage(e, item) {
  const filename = e.target.value
  if (!filename) { item.Path = ''; return }
  const img = store.paperImages.find(i => i.filename === filename)
  if (img) item.Path = img.filename
}

async function uploadContentImage(e, item) {
  const file = e.target.files?.[0]
  if (!file) return
  const img = await store.uploadImage(undefined, file)
  if (img) item.Path = img.filename
  e.target.value = ''
}
</script>
