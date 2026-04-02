/**
 * Axios API client with JWT auth interceptor
 */
import axios from 'axios'

// In production (nginx proxy), VITE_API_URL is empty → use relative paths
// In development, VITE_API_URL points to http://localhost:1001 directly
const API_BASE_URL = import.meta.env.VITE_API_URL !== undefined
  ? import.meta.env.VITE_API_URL
  : 'http://localhost:1001'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 0, // No timeout for long AI operations
})

// Attach JWT token to every request automatically
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('jwt_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Redirect to login on 401
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('jwt_token')
      localStorage.removeItem('user')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api
