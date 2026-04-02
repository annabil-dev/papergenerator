/**
 * Auth Store — manages JWT token and user state
 */
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '../api/index.js'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('jwt_token') || null)
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))

  const isLoggedIn = computed(() => !!token.value)
  const isAdmin = computed(() => user.value?.role === 'admin')

  function setToken(jwt) {
    token.value = jwt
    localStorage.setItem('jwt_token', jwt)
  }

  function setUser(userData) {
    user.value = userData
    localStorage.setItem('user', JSON.stringify(userData))
  }

  async function fetchMe() {
    if (!token.value) return
    try {
      const res = await api.get('/api/auth/me')
      setUser(res.data)
    } catch {
      logout()
    }
  }

  function loginWithGoogle() {
    // Use relative path when in production (nginx proxies /api/ to backend)
    // Use full backend URL in development
    const backendUrl = import.meta.env.VITE_API_URL || ''
    window.location.href = `${backendUrl}/api/auth/google/login`
  }

  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('jwt_token')
    localStorage.removeItem('user')
  }

  // On store init, refresh user info from API if we have a token
  if (token.value) {
    fetchMe()
  }

  return { token, user, isLoggedIn, isAdmin, setToken, setUser, fetchMe, loginWithGoogle, logout }
})
