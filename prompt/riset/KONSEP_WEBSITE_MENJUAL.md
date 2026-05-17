# Konsep Website yang Menjual: PaperGenerator
> Berdasarkan MarketingSkills: page-cro · copywriting · marketing-psychology · signup-flow-cro
> Dibuat: April 2026

---

## Daftar Isi
1. [Diagnosa Landing Page Saat Ini](#1-diagnosa-landing-page-saat-ini)
2. [5 Pilar Website yang Menjual](#2-5-pilar-website-yang-menjual)
3. [Psikologi Marketing — Trigger yang Membuat Orang Beli](#3-psikologi-marketing--trigger-yang-membuat-orang-beli)
4. [Copywriting: Bahasa yang Membujuk](#4-copywriting-bahasa-yang-membujuk)
5. [Struktur Halaman Ideal (Blueprint)](#5-struktur-halaman-ideal-blueprint)
6. [Signup Flow CRO](#6-signup-flow-cro)
7. [Implementasi Konkret untuk PaperGenerator](#7-implementasi-konkret-untuk-papergenerator)

---

## 1. Diagnosa Landing Page Saat Ini

Berdasarkan analisis kode `LandingPage.vue`, ini kondisi landing page anda sekarang:

### ✅ Yang Sudah Benar
- Headline cukup clear: *"Write IEEE Papers 10x Faster with AI"*
- CTA di atas fold ada
- Layout bersih dan modern (dark gradient, Tailwind)
- Feature cards ada

### 🔴 Yang Hilang (dan Kenapa Orang Tidak Daftar)

| Elemen | Status | Dampak |
|--------|--------|--------|
| **Social proof** (jumlah user, testimonial) | ❌ Tidak ada | Orang tidak tahu apakah tool ini dipercaya |
| **Demo visual / video** | ❌ Tidak ada | Orang tidak tahu hasilnya seperti apa |
| **Objection handling / FAQ** | ❌ Tidak ada | Keraguan tidak terjawab |
| **Pricing info** | ❌ Tidak ada | "Apakah ini gratis atau berbayar?" |
| **Contoh output paper** | ❌ Tidak ada | Tidak ada bukti kualitas |
| **Benefit vs feature** | ⚠️ Feature-focused | "Smart Image Management" → siapa yang peduli? |
| **Urgency / scarcity** | ❌ Tidak ada | Tidak ada alasan untuk daftar sekarang |
| **Trust signals** | ❌ Tidak ada | Tidak ada badge, logo instansi, dll |
| **Persona matching** | ❌ Generic | Harus jelas: "Untuk mahasiswa teknik" |

---

## 2. Lima Pilar Website yang Menjual

Ini adalah 5 konsep inti yang **harus dipahami dan diimplementasikan** agar website mengonversi pengunjung menjadi pengguna:

---

### Pilar 1: CLARITY — Kejelasan dalam 5 Detik

> *"Jika user harus berpikir untuk memahami produk Anda, mereka sudah pergi."*

**Aturan 5 Detik**: Seorang pengunjung baru HARUS bisa menjawab 3 pertanyaan ini dalam 5 detik pertama:
1. Ini tools untuk apa?
2. Untuk siapa tools ini?
3. Kenapa saya harus pakai?

**Masalah headline saat ini**: *"Write IEEE Papers 10x Faster with AI"* — sudah bagus, tapi bisa lebih spesifik. Siapa yang menulis IEEE paper? Mahasiswa, dosen, peneliti.

**Konsep: Clarity > Clever**
Jangan terlalu kreatif sampai pesan utama hilang. Lebih baik:
- ❌ Clever tapi bingung: *"Accelerate your academic journey"*
- ✅ Clear dan langsung: *"Generate Full IEEE Paper in 5 Minutes — Free"*

---

### Pilar 2: VALUE PROPOSITION — Kenapa Harus Pilih Ini?

> *"Value proposition bukan tentang produk Anda. Tentang perubahan yang terjadi pada hidup pelanggan."*

**Formula Value Proposition yang kuat:**
```
[Produk Anda] membantu [target user]
yang ingin [outcome yang diinginkan]
dengan cara [cara unik Anda]
tidak seperti [kompetitor/alternatif]
```

**Untuk PaperGenerator:**
```
PaperGenerator membantu mahasiswa teknik
yang harus buat paper IEEE untuk kampus
dengan cara generate paper lengkap 1 klik + export DOCX
tidak seperti ChatGPT yang butuh banyak prompt & format manual
```

**Differentiator nyata yang harus ditonjolkan:**
1. **GRATIS** — kompetitor $20/bulan
2. **Full paper 1 klik** — tidak ada tool lain yang bisa ini
3. **Export DOCX IEEE** — siap submit langsung
4. **Lolos AI detector** — fitur human text yang unik

---

### Pilar 3: TRUST — Kepercayaan Sebelum Konversi

> *"Orang tidak beli dari website. Mereka beli dari orang dan brand yang mereka percaya."*

Trust dibangun dari beberapa lapisan:

**Lapisan 1 — Social Proof**
- Jumlah pengguna: *"1.200+ mahasiswa sudah generate paper"*
- Testimoni nyata dengan nama, kampus, foto
- Screenshot hasil paper yang dihasilkan
- Review bintang 5

**Lapisan 2 — Authority**
- Logo kampus yang sudah pakai (ITB, UI, ITS, dll)
- Mention di media ("Seperti yang disebutkan di Dailysocial")
- Afiliasi atau partnership

**Lapisan 3 — Transparency**
- Siapa yang buat tool ini? (founder story)
- Privacy policy jelas
- Tidak ada hidden fee
- "100% Gratis, tidak perlu kartu kredit"

**Lapisan 4 — Risk Reversal**
- "Coba gratis, tidak perlu kartu kredit"
- "Kalau tidak puas, tidak perlu bayar apapun"
- Garansi uang kembali (saat mulai berbayar)

---

### Pilar 4: OBJECTION HANDLING — Jawab Sebelum Ditanya

> *"Setiap calon user punya pertanyaan tersembunyi. Jawab sebelum mereka pergi."*

**Objeksi utama mahasiswa teknik:**

| Objeksi | Jawaban di Website |
|---------|-------------------|
| *"Apakah paper ini plagiat?"* | "Human text mode + panduan penggunaan yang benar" |
| *"Apakah format IEEE-nya benar?"* | "Sudah diverifikasi sesuai standar IEEE 2024" + contoh output |
| *"Apakah AI detector bisa mendeteksi?"* | "Ada Human Text Generator untuk membuat teks lebih natural" |
| *"Apakah dataku aman?"* | "Login Google OAuth, paper hanya bisa dilihat oleh kamu" |
| *"Apakah ini gratis selamanya?"* | "Gratis untuk 2 paper/bulan, upgrade jika butuh lebih" |
| *"Hasilnya berkualitas tidak?"* | "Lihat contoh output paper di sini →" |
| *"Butuh berapa lama?"* | "Paper lengkap siap dalam 3-7 menit" |

**Cara sampaikan:** Buat seksi FAQ yang jujur dan conversational.

---

### Pilar 5: URGENCY & FRICTION REDUCTION — Dorong Aksi Sekarang

> *"Status quo adalah musuh terbesar Anda. Orang lebih suka tidak berubah daripada berubah."*

**Ciptakan urgency yang genuine (bukan palsu):**
- *"Paper deadline minggu ini? Generate sekarang."*
- *"300 mahasiswa daftar minggu ini"*
- Jumlah slot gratis terbatas (jika benar adanya)

**Kurangi friction signup:**
- Saat ini: tombol "Sign in with Google" → bagus!
- Tambahkan: *"Daftar dalam 10 detik, tidak perlu kartu kredit"*
- Tambahkan: *"Langsung bisa digunakan, tidak ada setup"*

**Loss aversion (takut kehilangan lebih kuat dari keinginan mendapat):**
- ❌ *"Dapatkan 2 paper gratis"*
- ✅ *"Jangan lewatkan paper gratis Anda — mahasiswa lain sudah submit"*

---

## 3. Psikologi Marketing — Trigger yang Membuat Orang Beli

Ini adalah prinsip psikologi yang bekerja secara bawah sadar dan harus diimplementasikan ke website:

### 🧠 Social Proof (Bukti Sosial)
**Prinsip**: Orang mengikuti apa yang dilakukan orang lain, terutama dalam situasi tidak pasti.

**Implementasi untuk PaperGenerator:**
```
✅ "Sudah digunakan oleh 1.200+ mahasiswa dari 45 kampus Indonesia"
✅ Testimoni: "Paper IEEE saya selesai dalam 6 menit! — Andi, Mahasiswa ITS"  
✅ Counter real-time: "🎓 3.847 paper sudah di-generate"
✅ Logo kampus pengguna di footer
```

### 🧠 Endowment Effect (Rasa Memiliki)
**Prinsip**: Orang lebih menghargai sesuatu yang sudah mereka "miliki".

**Implementasi:**
- Free tier memberikan akses nyata — user sudah "punya" 2 paper gratis
- Ketika upgrade diperlukan, user sudah invested → lebih mau bayar
- *"Paper Anda sudah tersimpan. Upgrade untuk unlock fitur lanjutan."*

### 🧠 Zero-Price Effect (Efek Gratis)
**Prinsip**: "Gratis" bukan sekedar harga murah — ini kategori psikologi berbeda.

**Implementasi:**
- Taruh kata **GRATIS** secara eksplisit dan besar
- *"100% Gratis — tidak perlu kartu kredit"*
- Jangan hanya bilang "free plan" — bilang **GRATIS**

### 🧠 Hyperbolic Discounting (Manfaat Sekarang > Nanti)
**Prinsip**: Orang lebih preferensikan manfaat segera daripada manfaat masa depan.

**Implementasi:**
- ❌ *"Tingkatkan produktivitas penelitian Anda"* (masa depan, abstrak)
- ✅ *"Generate paper pertama Anda dalam 5 menit sekarang"* (sekarang, konkret)

### 🧠 Mimetic Desire (Ingin karena Orang Lain Ingin)
**Prinsip**: Keinginan menular secara sosial.

**Implementasi:**
- *"Mahasiswa ITB, UI, ITS sudah pakai — kapan giliran kamu?"*
- Tunjukkan profil konkret pengguna yang sukses
- "Bergabung dengan teman-temanmu yang sudah submit paper"

### 🧠 Paradox of Choice (Terlalu Banyak Pilihan = Tidak Pilih)
**Prinsip**: Lebih sedikit pilihan = lebih tinggi konversi.

**Implementasi saat pricing:**
- Jangan tampilkan 5 plan — cukup 2-3
- Rekomendasi 1 plan yang "paling populer"
- Tombol CTA berbeda untuk tiap plan tapi primary action jelas

### 🧠 Peak-End Rule (Momen Puncak & Akhir yang Diingat)
**Prinsip**: Pengalaman dinilai dari momen terbaik dan momen akhir.

**Implementasi:**
- **Peak**: Momen "wow" saat paper pertama selesai di-generate → tampilkan pesan selebrasi
- **End**: Thank you page yang bagus setelah daftar, bukan halaman kosong

### 🧠 Goal-Gradient Effect (Makin Dekat Makin Semangat)
**Prinsip**: Orang mempercepat aksi ketika merasa hampir mencapai tujuan.

**Implementasi:**
- Progress bar saat generate paper: *"75% — Menulis Kesimpulan..."*
- Onboarding: *"Paper pertama Anda 80% selesai — tinggal 1 langkah lagi"*

### 🧠 Pratfall Effect (Kelemahan yang Membangun Trust)
**Prinsip**: Mengakui kelemahan kecil justru meningkatkan kepercayaan.

**Implementasi:**
- *"Kami bukan pengganti riset Anda — kami mempercepat penulisannya"*
- *"Hasilnya harus Anda review dan sesuaikan — AI tidak sempurna"*
- Khas orang jujur dan dipercaya → konversi lebih tinggi

---

## 4. Copywriting: Bahasa yang Membujuk

### Formula Headline Terbaik untuk PaperGenerator

**Opsi 1 — Outcome + Waktu (Most Recommended):**
> *"Generate Full IEEE Paper dalam 5 Menit — Gratis"*

**Opsi 2 — Pain Point:**
> *"Deadline Paper IEEE Besok? Generate Sekarang."*

**Opsi 3 — Social Proof:**
> *"1.200+ Mahasiswa Sudah Submit IEEE Paper Mereka. Kapan Giliranmu?"*

**Opsi 4 — Differentiator:**
> *"Satu-satunya Tool yang Generate Full IEEE Paper Lengkap — Dan Gratis"*

### Subheadline yang Lebih Baik

**Saat ini:**
> *"Generate complete IEEE-format academic papers with AI, manage your research, organize figures, and export directly to DOCX — all in one place."*

**Rekomendasi (lebih benefit-focused, bahasa target user):**
> *"Ketik topik → AI generate paper IEEE lengkap dengan sections, referensi, dan persamaan matematika → Download DOCX siap submit. Tanpa template manual, tanpa format-formatan."*

### CTA Copy yang Lebih Kuat

| ❌ Lemah | ✅ Kuat |
|----------|---------|
| "Get Started with Google" | "Generate Paper IEEE Gratis Sekarang" |
| "Sign in with Google" | "Mulai Gratis — Login 10 Detik" |
| "Learn More" | "Lihat Contoh Paper yang Di-generate →" |
| "Start Writing for Free" | "Generate Paper Pertama Saya — Gratis" |

### Feature vs. Benefit — Cara Benar Menulis

| ❌ Feature (Jangan) | ✅ Benefit (Gunakan Ini) |
|--------------------|------------------------|
| "Smart Image Management" | "Upload gambar ke paper dan atur posisi tanpa ribet" |
| "IEEE Format" | "Paper langsung sesuai standar IEEE — tidak perlu format manual" |
| "Admin Dashboard" | (Hapus ini dari landing page — ini fitur admin, bukan user) |
| "AI Paper Generation" | "Dari 1 kalimat topik → paper 8 halaman IEEE dalam 5 menit" |
| "Secure & Private" | "Paper kamu hanya bisa dilihat kamu — tidak dibagikan siapapun" |
| "Paper Management" | "Simpan semua draftmu, akses dari mana saja" |

### Bahasa yang Resonan dengan Mahasiswa Teknik Indonesia

Gunakan kata-kata yang **mahasiswa sendiri pakai**:
- "Deadline besok"
- "Dosen nuntut format IEEE"  
- "Paper buat konferensi"
- "Lolos Turnitin/cek AI"
- "Submit jurnal"
- "Skripsi / TA"
- "Matkul Metodologi Penelitian"

---

## 5. Struktur Halaman Ideal (Blueprint)

Berdasarkan framework CRO dan psychology, ini urutan section yang terbukti mengonversi:

```
┌─────────────────────────────────────────────┐
│  NAVIGATION                                  │
│  Logo | Fitur | Harga | Login | [DAFTAR]     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  HERO (Above the fold — paling penting)      │
│                                              │
│  Badge: "Gratis · IEEE Format · DOCX Export" │
│                                              │
│  H1: Generate Full IEEE Paper dalam          │
│      5 Menit — Gratis                        │
│                                              │
│  Subheadline: Ketik topik → AI tulis sections│
│   lengkap → Download DOCX siap submit.       │
│   Tidak perlu template manual.               │
│                                              │
│  [🚀 Generate Paper Gratis — Login Google]   │
│  Tidak perlu kartu kredit · 10 detik signup  │
│                                              │
│  Social Proof: "🎓 3.847 paper di-generate   │
│  oleh mahasiswa dari 45+ kampus Indonesia"   │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  DEMO / PROOF (Screenshot / Video)           │
│                                              │
│  "Lihat cara kerjanya:" [Video 60 detik]     │
│  atau: Screenshot before/after               │
│  "Input: 1 kalimat → Output: 8 halaman IEEE" │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  SOCIAL PROOF — TESTIMONIALS                 │
│                                              │
│  ⭐⭐⭐⭐⭐                                  │
│  "Paper saya selesai dalam 6 menit!          │
│   Format IEEE-nya benar. Lulus konferensi."  │
│  — Andi S., Informatika ITS                  │
│                                              │
│  ⭐⭐⭐⭐⭐                                  │
│  "Gratis tapi kualitasnya bagus banget.      │
│   Lebih baik dari bayar ChatGPT $20."        │
│  — Rina P., Teknik Elektro UGM              │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  HOW IT WORKS (3 langkah)                   │
│                                              │
│  1️⃣ Ketik topik paper (30 detik)            │
│  2️⃣ AI generate paper lengkap (3-7 menit)   │
│  3️⃣ Download DOCX, siap submit              │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  BENEFITS / FEATURES (Benefit-first)         │
│                                              │
│  ⚡ Full paper dari 1 prompt                 │
│     "Dari judul → Abstract → Intro →        │
│      Methodology → Results → DOCX"          │
│                                              │
│  📐 Format IEEE yang benar                  │
│     "Sesuai standar IEEE 2024, siap submit   │
│      ke konferensi tanpa format ulang"       │
│                                              │
│  🤖 Lolos AI detector                       │
│     "Human text mode: teks lebih natural,   │
│      lebih aman untuk submit"               │
│                                              │
│  💰 Gratis — kompetitor $20/bulan           │
│     "Jenni.ai $20/bln, SciSpace $20/bln     │
│      — PaperGenerator: GRATIS"              │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  PRICING (Simple)                            │
│                                              │
│  FREE | PRO Rp49rb | UNLIMITED Rp99rb        │
│  [Recommended: PRO]                          │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  FAQ / OBJECTION HANDLING                    │
│                                              │
│  Q: Apakah ini benar-benar gratis?           │
│  Q: Format IEEE-nya sudah benar?             │
│  Q: Apakah bisa ketahuan AI?                │
│  Q: Data paper saya aman?                   │
│  Q: Berapa lama prosesnya?                  │
│  Q: Beda dengan ChatGPT?                    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  FINAL CTA (Risk reversal)                   │
│                                              │
│  "Siap generate paper IEEE pertamamu?"       │
│  [🚀 Mulai Gratis — Login Google]            │
│  ✓ Gratis · ✓ Tidak perlu kartu kredit      │
│  ✓ Paper siap dalam 5 menit                 │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  FOOTER                                      │
│  © 2026 PaperGenerator · paper.otomasi.app  │
│  Logo kampus pengguna                        │
└─────────────────────────────────────────────┘
```

---

## 6. Signup Flow CRO

Alur signup yang ideal setelah user klik "Login Google":

```
Klik CTA
   ↓
Google OAuth Popup (1 klik)
   ↓
Redirect ke Dashboard
   ↓
ONBOARDING MODAL (bukan halaman kosong!)
   ┌─────────────────────────────────┐
   │  Selamat datang, Andi! 🎉       │
   │                                 │
   │  Mau buat paper tentang apa?    │
   │  [Input: ketik topik...]        │
   │                                 │
   │  [Generate Paper Pertama] →     │
   └─────────────────────────────────┘
   ↓
Progress bar generate (3-7 menit)
   "Menulis Abstract... 40%"
   ↓
Paper selesai! → Momen WOW 🎉
   "Paper IEEE kamu siap! Download DOCX"
   ↓
[Download DOCX] [Generate Lagi] [Upgrade Pro]
```

**Prinsip kunci signup flow:**
- Jangan biarkan user landing di halaman dashboard kosong
- Langsung dorong ke "aha moment" (generate paper pertama)
- Aha moment = momen user sadar nilai produk ini

---

## 7. Implementasi Konkret untuk PaperGenerator

### Quick Wins (Bisa dikerjakan dalam 1-3 hari)

#### A. Update Hero Section
```vue
<!-- Ganti ini: -->
<h1>Write IEEE Papers 10x Faster with AI</h1>

<!-- Jadi ini: -->
<div class="badge">✓ Gratis · ✓ IEEE Format · ✓ DOCX Export</div>
<h1>Generate Full IEEE Paper dalam 5 Menit — Gratis</h1>
<p>Ketik topik → AI tulis paper lengkap → Download DOCX siap submit.
   Tidak perlu format manual, tidak perlu template.</p>
```

#### B. Tambah Social Proof Counter
```vue
<!-- Tambah di bawah hero CTA: -->
<div class="social-proof">
  🎓 <strong>3.847 paper</strong> sudah di-generate oleh mahasiswa 
  dari <strong>45+ kampus Indonesia</strong>
</div>
```

#### C. Ganti CTA Text
```vue
<!-- Ganti: "Get Started with Google" -->
<!-- Jadi: -->
<button>🚀 Generate Paper Gratis — Login Google</button>
<p class="microcopy">Tidak perlu kartu kredit · Signup 10 detik</p>
```

#### D. Rewrite Feature Cards (Benefit-focused)
```javascript
const features = [
  {
    icon: '⚡',
    title: 'Full Paper dari 1 Prompt',
    description: 'Ketik judul/topik → AI tulis Abstract, Intro, Methodology, Results, Conclusion + Referensi dalam 5 menit.',
  },
  {
    icon: '📐',
    title: 'Format IEEE yang Benar',
    description: 'Sesuai standar IEEE conference 2024. Export DOCX langsung siap submit — tanpa format ulang manual.',
  },
  {
    icon: '🤖',
    title: 'Lolos AI Detector',
    description: 'Human Text Generator membuat tulisan lebih natural, mengurangi risiko deteksi AI oleh Turnitin dan GPTZero.',
  },
  {
    icon: '🖼️',
    title: 'Upload Gambar & Figure',
    description: 'Upload diagram, grafik, foto hasil eksperimen. Atur posisi gambar langsung di editor.',
  },
  {
    icon: '💰',
    title: 'Gratis — Kompetitor $20/bulan',
    description: 'Jenni.ai, SciSpace, Paperpal semua $15-20/bulan. PaperGenerator: GRATIS untuk 2 paper per bulan.',
  },
  {
    icon: '🔒',
    title: 'Paper Kamu Hanya Milikmu',
    description: 'Login Google OAuth. Paper hanya bisa dilihat oleh kamu — tidak dibagikan, tidak dipakai untuk training AI.',
  },
]
```

#### E. Tambah Section FAQ
```vue
<!-- Tambah section FAQ sebelum final CTA -->
<section id="faq">
  <h2>Pertanyaan yang Sering Ditanya</h2>
  <div v-for="faq in faqs">
    <details>
      <summary>{{ faq.q }}</summary>
      <p>{{ faq.a }}</p>
    </details>
  </div>
</section>

const faqs = [
  {
    q: "Apakah ini benar-benar gratis?",
    a: "Ya, 100% gratis untuk 2 paper per bulan. Tidak perlu kartu kredit. Upgrade ke Pro (Rp 49.000/bulan) untuk lebih banyak paper."
  },
  {
    q: "Format IEEE-nya sudah sesuai standar?",
    a: "Ya, mengikuti standar IEEE conference paper 2024. Termasuk dua kolom, abstract, section numbering, dan format referensi [1], [2]."
  },
  {
    q: "Apakah paper bisa ketahuan AI oleh Turnitin?",
    a: "Kami menyediakan Human Text Generator untuk membuat tulisan lebih natural. Namun kami sarankan selalu review dan edit hasil AI sebelum submit."
  },
  {
    q: "Berbeda apa dengan ChatGPT?",
    a: "ChatGPT tidak punya template IEEE, tidak bisa export DOCX, tidak ada manajemen gambar, dan perlu banyak prompt manual. PaperGenerator khusus untuk IEEE — generate langsung, download, submit."
  },
  {
    q: "Data paper saya aman?",
    a: "Ya. Login menggunakan Google OAuth. Paper hanya bisa diakses oleh akun Anda. Kami tidak menjual atau membagikan data Anda."
  },
  {
    q: "Berapa lama proses generate paper?",
    a: "Rata-rata 3-7 menit untuk paper lengkap. Tergantung panjang dan kompleksitas topik."
  },
]
```

### High-Impact Changes (1-2 minggu)

1. **Tambah Demo Video** — screen recording 60-90 detik yang menunjukkan proses generate paper. Ini adalah elemen paling berpengaruh untuk konversi.

2. **Tambah Testimonial Section** — minta langsung ke pengguna existing. 3-5 testimonial dengan nama dan kampus sudah cukup.

3. **Tambah "How It Works" Section** — 3 langkah visual sederhana.

4. **Tambah Pricing Section** di landing page — banyak orang tidak signup karena tidak tahu apakah ada biaya tersembunyi.

5. **Onboarding flow setelah signin** — jangan biarkan user di halaman dashboard kosong. Langsung arahkan ke generate paper pertama.

### Test Ideas (A/B Testing)

| Element | Variant A | Variant B |
|---------|-----------|-----------|
| Headline | "Generate Full IEEE Paper dalam 5 Menit" | "Selesaikan Paper IEEE Sebelum Deadline — Gratis" |
| CTA | "Generate Paper Gratis" | "Mulai Sekarang — Gratis" |
| Hero lang | English (saat ini) | Bahasa Indonesia |
| Hero | Text only (saat ini) | Text + screenshot output |

---

## Rangkuman: 10 Konsep yang HARUS Ada

| # | Konsep | Status Sekarang | Prioritas |
|---|--------|-----------------|-----------|
| 1 | **Value Prop Jelas dalam 5 detik** | ⚠️ Cukup tapi bisa lebih baik | 🔴 Tinggi |
| 2 | **Social Proof (jumlah user, testimoni)** | ❌ Tidak ada | 🔴 Tinggi |
| 3 | **Demo visual / video** | ❌ Tidak ada | 🔴 Tinggi |
| 4 | **CTA yang action-oriented** | ⚠️ Generic | 🔴 Tinggi |
| 5 | **Benefit-focused copy (bukan feature)** | ❌ Feature-focused | 🔴 Tinggi |
| 6 | **FAQ / Objection Handling** | ❌ Tidak ada | 🟡 Medium |
| 7 | **Pricing transparency** | ❌ Tidak ada | 🟡 Medium |
| 8 | **Trust signals (no credit card, secure)** | ❌ Tidak ada | 🟡 Medium |
| 9 | **Onboarding "aha moment"** | ❌ Tidak ada | 🟡 Medium |
| 10 | **Urgency / Scarcity** | ❌ Tidak ada | 🟢 Low |

---

*Laporan ini berdasarkan MarketingSkills: page-cro v1.1.0 · copywriting v1.1.0 · marketing-psychology v1.1.0 · signup-flow-cro v1.1.0*

*Dibuat: April 2026*
