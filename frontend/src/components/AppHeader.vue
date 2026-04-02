<template>
  <header class="bg-white shadow-sm border-b sticky top-0 z-40">
    <div class="w-full px-4 lg:px-8 py-3 flex items-center justify-between">
      <!-- Logo + Nav -->
      <div class="flex items-center gap-6">
        <router-link to="/dashboard" class="flex items-center gap-2 text-gray-800 hover:text-blue-600 transition-colors">
          <span class="text-lg">📄</span>
          <span class="font-semibold">PaperGenerator</span>
        </router-link>
        <nav class="hidden md:flex items-center gap-1 text-sm">
          <router-link to="/dashboard" class="px-3 py-1.5 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-gray-900 transition-colors" active-class="bg-blue-50 text-blue-700">
            Papers
          </router-link>
          <router-link to="/files" class="px-3 py-1.5 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-gray-900 transition-colors" active-class="bg-blue-50 text-blue-700">
            Files
          </router-link>
          <router-link v-if="auth.isAdmin" to="/admin" class="px-3 py-1.5 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-gray-900 transition-colors" active-class="bg-purple-50 text-purple-700">
            Admin
          </router-link>
        </nav>
      </div>

      <!-- User Menu -->
      <div class="flex items-center gap-3">
        <div class="relative" ref="menuRef">
          <button @click="menuOpen = !menuOpen"
            class="flex items-center gap-2 px-3 py-1.5 rounded-xl hover:bg-gray-100 transition-colors text-sm text-gray-700">
            <img v-if="auth.user?.avatar_url" :src="auth.user.avatar_url" class="w-7 h-7 rounded-full" alt="avatar" />
            <span v-else class="w-7 h-7 rounded-full bg-blue-500 flex items-center justify-center text-white text-xs font-bold">
              {{ auth.user?.name?.[0]?.toUpperCase() || 'U' }}
            </span>
            <span class="hidden md:inline font-medium">{{ auth.user?.name || 'User' }}</span>
            <span class="text-gray-400">▾</span>
          </button>

          <!-- Dropdown -->
          <div v-if="menuOpen" class="absolute right-0 top-full mt-1 w-52 bg-white border border-gray-100 rounded-xl shadow-lg overflow-hidden z-50">
            <div class="px-4 py-3 border-b border-gray-50">
              <p class="text-sm font-medium text-gray-800">{{ auth.user?.name }}</p>
              <p class="text-xs text-gray-400">{{ auth.user?.email }}</p>
              <span v-if="auth.isAdmin" class="text-xs bg-purple-100 text-purple-700 px-1.5 py-0.5 rounded mt-1 inline-block">Admin</span>
            </div>
            <router-link to="/dashboard" @click="menuOpen = false" class="flex items-center gap-2 px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              📄 My Papers
            </router-link>
            <router-link to="/files" @click="menuOpen = false" class="flex items-center gap-2 px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              🗂️ Files
            </router-link>
            <router-link v-if="auth.isAdmin" to="/admin" @click="menuOpen = false" class="flex items-center gap-2 px-4 py-2.5 text-sm text-gray-700 hover:bg-gray-50 transition-colors">
              📊 Admin
            </router-link>
            <div class="border-t border-gray-50">
              <button @click="doLogout" class="w-full flex items-center gap-2 px-4 py-2.5 text-sm text-red-600 hover:bg-red-50 transition-colors">
                🚪 Sign Out
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth.js'

const auth = useAuthStore()
const router = useRouter()
const menuOpen = ref(false)
const menuRef = ref(null)

function doLogout() {
  auth.logout()
  router.push('/login')
}

function handleOutsideClick(e) {
  if (menuRef.value && !menuRef.value.contains(e.target)) {
    menuOpen.value = false
  }
}

onMounted(() => document.addEventListener('click', handleOutsideClick))
onUnmounted(() => document.removeEventListener('click', handleOutsideClick))
</script>
