<template>
  <button @click="$emit('click')"
    :disabled="loading"
    class="px-3 py-1.5 bg-purple-100 text-purple-700 rounded-lg hover:bg-purple-200 text-xs font-medium flex items-center gap-1 disabled:opacity-50 transition-all">
    <span v-if="loading" class="spinner !w-3 !h-3 !border-purple-400 !border-t-purple-700"></span>
    <svg v-else class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
    </svg>
    {{ label }}
  </button>
</template>

<script setup>
defineProps({
  label: { type: String, default: 'AI' },
  loading: { type: Boolean, default: false }
})
defineEmits(['click'])
</script>
