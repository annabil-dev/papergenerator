<template>
  <div class="min-h-screen bg-slate-900 flex items-center justify-center">
    <div class="text-center text-white">
      <div class="text-4xl mb-4 animate-spin">⚙️</div>
      <p class="text-slate-400">{{ statusMsg }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '../stores/auth.js'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const statusMsg = ref('Completing sign-in...')

onMounted(async () => {
  const token = route.query.token

  if (!token) {
    statusMsg.value = 'Sign-in failed — no token received.'
    setTimeout(() => router.push('/login?error=auth_failed'), 2000)
    return
  }

  // Store the token
  auth.setToken(token)

  // Fetch user info
  try {
    await auth.fetchMe()
    statusMsg.value = `Welcome back, ${auth.user?.name || 'user'}!`
    setTimeout(() => router.push('/dashboard'), 800)
  } catch {
    statusMsg.value = 'Failed to load user info.'
    setTimeout(() => router.push('/login?error=auth_failed'), 2000)
  }
})
</script>
