<template>
  <div class="p-6">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-lg font-semibold text-gray-800">Tables</h2>
      <button @click="store.addTable()"
        class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium">
        + Add Table
      </button>
    </div>

    <p class="text-sm text-gray-500 mb-4">
      Create tables with headers and rows. Reference in sections with
      <code class="bg-gray-100 px-1 rounded">[TABLE:table-1]</code>
    </p>

    <div v-if="store.paper.tables.length === 0"
      class="text-center py-12 text-gray-400">
      <svg class="w-12 h-12 mx-auto mb-3 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
      </svg>
      <p>No tables yet.</p>
    </div>

    <div v-for="(table, tIdx) in store.paper.tables" :key="table.id"
      class="border rounded-xl mb-6 overflow-hidden">

      <!-- Table Header -->
      <div class="bg-gray-50 px-4 py-3 flex items-center justify-between border-b">
        <span class="text-sm font-semibold text-gray-700">{{ table.id }}</span>
        <button @click="store.removeTable(tIdx)"
          class="text-red-400 hover:text-red-600 text-sm">✕ Remove</button>
      </div>

      <div class="p-4 space-y-3">
        <!-- Caption -->
        <div>
          <label class="block text-xs text-gray-500 mb-1">Caption</label>
          <input v-model="table.caption"
            placeholder="TABLE I. STATISTICAL ANALYSIS"
            class="w-full px-3 py-1.5 border rounded text-sm" />
        </div>

        <!-- Table Editor -->
        <div class="overflow-x-auto">
          <table class="min-w-full border text-sm">
            <thead>
              <tr class="bg-blue-50">
                <th v-for="(header, cIdx) in table.headers" :key="cIdx"
                  class="border px-2 py-1 relative">
                  <input v-model="table.headers[cIdx]" class="w-full bg-transparent text-center font-semibold text-sm focus:outline-none" />
                  <button v-if="table.headers.length > 1"
                    @click="store.removeTableColumn(tIdx, cIdx)"
                    class="absolute -top-1 -right-1 text-red-400 hover:text-red-600 text-xs bg-white rounded-full w-4 h-4 flex items-center justify-center shadow">✕</button>
                </th>
                <th class="border px-1 py-1 w-8">
                  <button @click="store.addTableColumn(tIdx)"
                    class="text-green-600 hover:text-green-800 text-lg font-bold">+</button>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, rIdx) in table.rows" :key="rIdx">
                <td v-for="(cell, cIdx) in row" :key="cIdx" class="border px-1 py-1">
                  <input v-model="table.rows[rIdx][cIdx]"
                    class="w-full bg-transparent text-center text-sm focus:outline-none focus:bg-blue-50 px-1" />
                </td>
                <td class="border px-1 py-1 text-center">
                  <button @click="store.removeTableRow(tIdx, rIdx)"
                    class="text-red-400 hover:text-red-600 text-xs">✕</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <button @click="store.addTableRow(tIdx)"
          class="text-sm text-blue-600 hover:text-blue-700 font-medium">+ Add Row</button>

        <div class="bg-blue-50 rounded p-2">
          <p class="text-xs text-blue-600">
            <strong>Usage:</strong> Insert <code class="bg-blue-100 px-1 rounded">{{ `[TABLE:${table.id}]` }}</code> in section content.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { usePaperStore } from '../stores/paper.js'
const store = usePaperStore()
</script>
