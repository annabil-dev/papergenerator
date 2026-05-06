<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 text-white">
    <!-- Navigation -->
    <nav class="flex items-center justify-between px-8 py-5 max-w-7xl mx-auto">
      <div class="flex items-center gap-2">
        <span class="text-2xl">📄</span>
        <span class="text-xl font-bold">PaperGenerator</span>
        <span class="text-xs bg-blue-500/30 text-blue-300 px-2 py-0.5 rounded-full font-medium ml-1">Multi-Journal</span>
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
        Generate Papers for
        <span class="bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">Journal</span>
        <br />or Conference
      </h1>
      <p class="text-xl text-slate-400 max-w-2xl mx-auto mb-10 leading-relaxed">
        Generate publication-ready papers for IEEE, international journals, SINTA-indexed journals, and conferences. Support for robotics, mechatronics, AI, power electronics, PLC automation, and embedded systems. Auto-format with LaTeX formulas, figures, tables, and references — export to DOCX ready for submission.
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

    <!-- Publication Types Section -->
    <section class="max-w-6xl mx-auto px-8 pb-24">
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Supported Publication Types</h2>
      <p class="text-slate-400 text-center mb-12 max-w-2xl mx-auto">Generate papers for various publication venues with proper formatting and citation styles</p>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="bg-gradient-to-br from-indigo-500/10 to-indigo-600/5 border border-indigo-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">📚</div>
          <h3 class="font-semibold mb-1 text-indigo-300">IEEE Journals</h3>
          <p class="text-slate-400 text-xs">TIE, TPEL, RA-L, TMECH, IoT-J, Access, and more. IEEE citation format and conference standards.</p>
        </div>
        <div class="bg-gradient-to-br from-emerald-500/10 to-emerald-600/5 border border-emerald-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🌐</div>
          <h3 class="font-semibold mb-1 text-emerald-300">International Journals</h3>
          <p class="text-slate-400 text-xs">Scopus, Web of Science indexed journals. APA, Vancouver, and custom citation formats supported.</p>
        </div>
        <div class="bg-gradient-to-br from-amber-500/10 to-amber-600/5 border border-amber-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🏆</div>
          <h3 class="font-semibold mb-1 text-amber-300">SINTA Journals</h3>
          <p class="text-slate-400 text-xs">Indonesian SINTA 1-6 indexed journals. Proper formatting for national publication requirements.</p>
        </div>
        <div class="bg-gradient-to-br from-rose-500/10 to-rose-600/5 border border-rose-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🎤</div>
          <h3 class="font-semibold mb-1 text-rose-300">Conferences</h3>
          <p class="text-slate-400 text-xs">International and local conferences. ICRA, IROS, IECON, and other technical conferences.</p>
        </div>
      </div>
    </section>

    <!-- Domains Section -->
    <section class="max-w-6xl mx-auto px-8 pb-24">
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Specialized Domains</h2>
      <p class="text-slate-400 text-center mb-12 max-w-2xl mx-auto">Our AI is trained on 100+ domain-specific topics for accurate technical content generation</p>
      <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="bg-gradient-to-br from-blue-500/10 to-blue-600/5 border border-blue-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">⚙️</div>
          <h3 class="font-semibold mb-1 text-blue-300">Engineering</h3>
          <p class="text-slate-400 text-xs">Mechanical, Electrical, Civil, Chemical, Aerospace, Mechatronics, Robotics, Power Electronics</p>
        </div>
        <div class="bg-gradient-to-br from-purple-500/10 to-purple-600/5 border border-purple-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">💻</div>
          <h3 class="font-semibold mb-1 text-purple-300">Computer Science</h3>
          <p class="text-slate-400 text-xs">AI, Machine Learning, Data Science, Cybersecurity, Cloud Computing, IoT, Blockchain, Networks</p>
        </div>
        <div class="bg-gradient-to-br from-red-500/10 to-red-600/5 border border-red-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🏥</div>
          <h3 class="font-semibold mb-1 text-red-300">Medical & Health</h3>
          <p class="text-slate-400 text-xs">Medicine, Nursing, Cardiology, Oncology, Biomedical Engineering, Public Health, Pharmacology</p>
        </div>
        <div class="bg-gradient-to-br from-green-500/10 to-green-600/5 border border-green-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🔬</div>
          <h3 class="font-semibold mb-1 text-green-300">Natural Sciences</h3>
          <p class="text-slate-400 text-xs">Biology, Chemistry, Physics, Mathematics, Environmental Science, Geology, Genetics</p>
        </div>
        <div class="bg-gradient-to-br from-amber-500/10 to-amber-600/5 border border-amber-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">💰</div>
          <h3 class="font-semibold mb-1 text-amber-300">Business & Finance</h3>
          <p class="text-slate-400 text-xs">Accounting, Finance, Economics, Management, Marketing, Entrepreneurship, Operations</p>
        </div>
        <div class="bg-gradient-to-br from-cyan-500/10 to-cyan-600/5 border border-cyan-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">�</div>
          <h3 class="font-semibold mb-1 text-cyan-300">Social Sciences</h3>
          <p class="text-slate-400 text-xs">Psychology, Sociology, Anthropology, Political Science, Education, Communication, Law</p>
        </div>
        <div class="bg-gradient-to-br from-lime-500/10 to-lime-600/5 border border-lime-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🌾</div>
          <h3 class="font-semibold mb-1 text-lime-300">Agriculture & Environment</h3>
          <p class="text-slate-400 text-xs">Agriculture, Agronomy, Horticulture, Environmental Engineering, Climate Science, Food Science</p>
        </div>
        <div class="bg-gradient-to-br from-pink-500/10 to-pink-600/5 border border-pink-500/20 rounded-xl p-5">
          <div class="text-2xl mb-2">🎨</div>
          <h3 class="font-semibold mb-1 text-pink-300">Arts & Humanities</h3>
          <p class="text-slate-400 text-xs">Literature, Philosophy, History, Linguistics, Architecture, Performing Arts, Religious Studies</p>
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
      <p>© 2026 PaperGenerator · Multi-Journal Academic Paper AI Tool</p>
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
    description: 'Generate complete papers with 4000+ words from a single prompt. AI writes all sections with academic writing style, proper citations, and anti-AI detection strategies.',
  },
  {
    icon: '🌍',
    title: 'Multi-Journal Support',
    description: 'Support for IEEE, international journals, SINTA-indexed journals, and conferences. Auto-adapt formatting to match specific journal or conference requirements.',
  },
  {
    icon: '🧮',
    title: 'LaTeX Formula Generation',
    description: 'Auto-generate mathematical formulas with DOCX-compatible LaTeX syntax. Supports domain-specific equations for control theory, kinematics, machine learning, and power electronics.',
  },
  {
    icon: '🖼️',
    title: 'AI Figure Generation',
    description: 'Generate detailed technical figures with AI prompts. Create block diagrams, circuit schematics, charts, heatmaps, and experimental setup illustrations automatically.',
  },
  {
    icon: '📊',
    title: 'Table & Reference Management',
    description: 'Auto-generate formatted tables with realistic data. Create 20+ references in various formats (IEEE, APA, Vancouver). All data internally consistent across figures, tables, and text.',
  },
  {
    icon: '🎯',
    title: 'Multi-Domain Support',
    description: 'Specialized for robotics, mechatronics, AI/ML, PLC automation, power electronics, embedded systems, and IoT. Domain-specific equations, figures, and terminology.',
  },
  {
    icon: '🏆',
    title: 'SINTA Journal Support',
    description: 'Optimized for Indonesian SINTA-indexed journals with proper formatting and citation styles. Support for SINTA 1-6 indexed journals across various disciplines.',
  },
  {
    icon: '🎤',
    title: 'Conference Paper Support',
    description: 'Generate conference papers with proper formatting for international and local conferences. Abstract, paper length, and presentation-ready content.',
  },
  {
    icon: '🗂️',
    title: 'Paper Management',
    description: 'Organize all your papers in one place. Create, edit, and delete papers. Each paper has its own figures, images, and complete content.',
  },
  {
    icon: '📐',
    title: 'Format Export',
    description: 'Auto-format papers according to journal or conference standards. Export directly to DOCX ready for submission with proper formatting, equations, and figures.',
  },
  {
    icon: '🔒',
    title: 'Secure & Private',
    description: 'Login with Google. Each user only sees their own papers. Your research stays private and secure with user-specific data isolation.',
  },
  {
    icon: '📈',
    title: 'Admin Dashboard',
    description: 'Track API token usage per user. View all papers. Monitor traffic and token consumption with detailed analytics for system management.',
  },
]
</script>
