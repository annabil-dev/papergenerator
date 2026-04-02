<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white">
    <!-- Navigation -->
    <nav class="flex items-center justify-between px-8 py-5 max-w-7xl mx-auto">
      <div class="flex items-center gap-2">
        <span class="text-2xl">📄</span>
        <span class="text-xl font-bold">PaperGenerator</span>
        <span class="text-xs bg-blue-500/30 text-blue-300 px-2 py-0.5 rounded-full font-medium ml-1">IEEE</span>
      </div>
      <button
        @click="auth.loginWithGoogle()"
        class="flex items-center gap-2 px-5 py-2.5 bg-white text-gray-800 rounded-full font-medium hover:bg-gray-100 transition-colors shadow-lg text-sm"
      >
        <GoogleIcon class="w-4 h-4" />
        Sign in with Google
      </button>
    </nav>

    <!-- Hero -->
    <section class="max-w-5xl mx-auto px-8 pt-20 pb-24 text-center">
      <div class="inline-flex items-center gap-2 text-blue-400 text-sm font-medium bg-blue-500/10 border border-blue-500/20 rounded-full px-4 py-1.5 mb-6">
        <span class="w-1.5 h-1.5 bg-blue-400 rounded-full animate-pulse"></span>
        AI-Powered Academic Paper Writing
      </div>
      <h1 class="text-5xl md:text-6xl font-extrabold mb-6 leading-tight">
        Write IEEE Papers
        <span class="bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">10x Faster</span>
        <br />with AI
      </h1>
      <p class="text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
        Generate complete IEEE-format academic papers with AI, manage your research, organize figures,
        and export directly to DOCX — all in one place.
      </p>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <button
          @click="auth.loginWithGoogle()"
          class="flex items-center justify-center gap-3 px-8 py-4 bg-white text-gray-800 rounded-xl font-semibold hover:bg-gray-100 transition-all shadow-2xl text-base"
        >
          <GoogleIcon class="w-5 h-5" />
          Get Started with Google
        </button>
        <a href="#features" class="flex items-center justify-center gap-2 px-8 py-4 border border-slate-600 rounded-xl text-slate-300 hover:border-slate-400 hover:text-white transition-colors text-base">
          Learn More →
        </a>
      </div>
    </section>

    <!-- Feature Cards -->
    <section id="features" class="max-w-6xl mx-auto px-8 pb-24">
      <h2 class="text-3xl font-bold text-center mb-12 text-white">Everything you need to write great papers</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div v-for="feature in features" :key="feature.title"
          class="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/8 transition-colors">
          <div class="text-3xl mb-4">{{ feature.icon }}</div>
          <h3 class="text-lg font-semibold mb-2">{{ feature.title }}</h3>
          <p class="text-slate-400 text-sm leading-relaxed">{{ feature.description }}</p>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="max-w-3xl mx-auto px-8 pb-24 text-center">
      <div class="bg-gradient-to-r from-blue-600/20 to-cyan-600/20 border border-blue-500/30 rounded-3xl p-12">
        <h2 class="text-3xl font-bold mb-4">Ready to write your paper?</h2>
        <p class="text-slate-400 mb-8">Join researchers using AI to accelerate their academic writing.</p>
        <button
          @click="auth.loginWithGoogle()"
          class="inline-flex items-center gap-3 px-8 py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-semibold transition-colors shadow-lg"
        >
          <GoogleIcon class="w-5 h-5" />
          Start Writing for Free
        </button>
      </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-white/10 py-8 text-center text-slate-500 text-sm">
      <p>© 2026 PaperGenerator · IEEE Academic Paper AI Tool</p>
    </footer>
  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth.js'

const auth = useAuthStore()

// Google icon as inline component
const GoogleIcon = {
  template: `<svg viewBox="0 0 24 24" fill="currentColor" class="text-current">
    <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
    <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
    <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/>
    <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
  </svg>`
}

const features = [
  {
    icon: '⚡',
    title: 'AI Paper Generation',
    description: 'Generate complete IEEE papers from a single prompt. AI writes sections, fills in content, creates references and equations.',
  },
  {
    icon: '🗂️',
    title: 'Paper Management',
    description: 'Organize all your papers in one place. Create, edit, and delete papers. Each paper has its own figures and images.',
  },
  {
    icon: '🖼️',
    title: 'Smart Image Management',
    description: 'Upload images per paper. Select images from dropdowns when editing figures. Toggle to include or exclude images from export.',
  },
  {
    icon: '📐',
    title: 'IEEE Format',
    description: 'Auto-format papers according to IEEE conference paper standards. Export to DOCX ready for submission.',
  },
  {
    icon: '🔒',
    title: 'Secure & Private',
    description: 'Login with Google. Each user only sees their own papers. Your research stays private and secure.',
  },
  {
    icon: '📊',
    title: 'Admin Dashboard',
    description: 'Track API token usage per user. View all papers. Monitor traffic and token consumption with detailed analytics.',
  },
]
</script>
