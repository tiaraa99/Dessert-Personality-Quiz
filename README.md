## 🍰 **Dessert Personality Quiz**

**Dessert Personality Quiz** adalah sebuah aplikasi kuis kepribadian berbasis web yang dibuat menggunakan framework **Flask (Python)**. Aplikasi ini mengidentifikasi tipe kepribadian pengguna berdasarkan jawaban mereka terhadap tiga pertanyaan pilihan ganda, lalu mencocokkannya dengan karakter-karakter unik yang diilustrasikan sebagai makanan penutup (dessert).

### 🔧 **Fungsi Utama Aplikasi**

1. **Halaman Utama (`/`)**
   Menyambut pengguna dan memperkenalkan kuis kepribadian.

2. **Halaman Kuis (`/quiz`)**
   Menyediakan 3 pertanyaan dengan pilihan jawaban (A–D) yang merepresentasikan kepribadian berbeda.

3. **Halaman Hasil (`/result`)**
   Memproses pilihan pengguna, menentukan hasil kepribadian berdasarkan peta data (`mapping.json`), dan menampilkan karakter dessert yang paling cocok beserta deskripsinya.

### ⚙️ **Cara Kerja Sistem**

* Jawaban dari pengguna dikonversi menjadi kode seperti "1A", "2C", dan sebagainya.
* Kode tersebut digunakan untuk mengambil daftar karakter dari file `mapping.json`.
* Karakter dengan jumlah kemunculan terbanyak dianggap sebagai hasil akhir.
* Hasil kepribadian ditampilkan dalam bentuk nama karakter dan deskripsi personal yang menggambarkan kepribadian pengguna.

### 🤖 **Struktur Agen Cerdas**

Aplikasi ini mencerminkan arsitektur **agen cerdas sederhana**, dengan elemen-elemen sebagai berikut:

* **Agent (Agen)**: Backend `Flask` yang memproses dan menganalisis hasil.
* **Sensor**: Form HTML yang menangkap input pengguna.
* **Aktuator**: Tampilan hasil berupa karakter kepribadian.
* **Environment (Lingkungan)**: Pengguna dan browser tempat aplikasi dijalankan.

### 📁 **Struktur File**

* `app.py`: Logika utama aplikasi, rute Flask, dan pemrosesan hasil.
* `mapping.json`: Peta jawaban terhadap karakter kepribadian.
* `templates/`: (Diasumsikan) berisi file HTML seperti `home.html`, `quiz.html`, dan `result.html`.

### 🍩 **Karakter Kepribadian (Dessert Personalities)**

Setiap hasil digambarkan sebagai karakter makanan penutup yang unik:

* 🍮 **Pudding Calm** – Tenang, reflektif, misterius.
* 🍓 **Strawberry Pop** – Ramah, positif, suka bersosialisasi.
* 🍫 **Dark Choco Deep** – Penuh pemikiran, intens, emosional.
* 🍪 **Cookie Crackle** – Ceria, spontan, penghibur suasana.
* 🍰 **Cheesecake Core** – Stabil, dewasa, penuh wibawa.
* 🥥 **Coconut Chill** – Santai, cuek, intuitif.
