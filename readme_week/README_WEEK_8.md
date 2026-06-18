# Progress Minggu 8 - Project Setup dan EDA

## Deskripsi Progress

Pada minggu ke-8, pengerjaan proyek difokuskan pada setup awal project dan Exploratory Data Analysis (EDA). Tahap ini dilakukan untuk memahami kondisi awal dataset sebelum masuk ke proses modeling.

Dataset yang digunakan adalah Sales and Marketing Customer Dataset dengan target prediksi `churn`.

Keterangan target:

- `churn = 0` : pelanggan tidak churn
- `churn = 1` : pelanggan churn

---

## Tujuan Minggu 8

Tujuan pengerjaan pada minggu ke-8 adalah:

1. Menyiapkan struktur folder project.
2. Menambahkan dataset ke folder `data/raw`.
3. Membaca dan memahami struktur awal dataset.
4. Mengecek ukuran dataset, tipe data, dan statistik deskriptif.
5. Mengecek data duplikat.
6. Menghitung dan memvisualisasikan missing value.
7. Melihat distribusi target `churn`.
8. Membuat heatmap korelasi fitur numerik.
9. Menganalisis fitur pemasaran dan transaksi pelanggan.

---

## Tahapan yang Dilakukan

### 1. Setup Project

Struktur folder project mulai disiapkan agar pengerjaan lebih rapi dan mudah dilanjutkan ke tahap modeling.

Folder yang digunakan antara lain:

```bash
data/raw
notebooks
outputs/figures
outputs/reports
progress
```

Dataset disimpan pada folder:

```bash
data/raw/Sales - Marketing customer dataset.csv
```

---

### 2. Load Dataset

Dataset dibaca menggunakan Pandas. Setelah data berhasil dimuat, dilakukan pengecekan awal dengan menampilkan 5 baris pertama dataset.

Tahap ini dilakukan untuk memastikan bahwa dataset dapat dibaca dengan benar dan kolom-kolom yang dibutuhkan tersedia.

---

### 3. Informasi Dataset

Pengecekan informasi dataset dilakukan untuk melihat:

- jumlah baris dan kolom,
- nama kolom,
- tipe data setiap kolom,
- jumlah data non-null pada setiap kolom.

Berdasarkan hasil pengecekan, dataset memiliki:

- 15.000 baris data
- 30 kolom

---

### 4. Statistik Deskriptif

Statistik deskriptif digunakan untuk melihat gambaran umum dari data numerik, seperti nilai rata-rata, standar deviasi, nilai minimum, dan maksimum.

Selain itu, statistik deskriptif untuk data kategorikal juga dilihat untuk memahami jumlah kategori dan kategori yang paling sering muncul.

---

### 5. Pengecekan Duplikasi

Pengecekan duplikasi dilakukan untuk melihat apakah terdapat data yang tercatat lebih dari satu kali.

Hasil pengecekan menunjukkan bahwa tidak terdapat data duplikat pada dataset.

---

### 6. Missing Value

Missing value dihitung untuk melihat kolom mana saja yang memiliki data kosong.

Beberapa kolom yang memiliki missing value adalah:

| Kolom | Persentase Missing Value |
|---|---:|
| `coupon_code` | 40,89% |
| `age` | 8,00% |
| `total_spent` | 7,00% |
| `gender` | 4,92% |
| `satisfaction_score` | 4,68% |

Hasil ini menunjukkan bahwa beberapa kolom perlu ditangani pada tahap preprocessing sebelum model final dibuat.

---

### 7. Distribusi Target Churn

Distribusi target `churn` dianalisis untuk melihat perbandingan pelanggan yang churn dan tidak churn.

Hasil distribusi target:

| Churn | Keterangan | Jumlah Data | Persentase |
|---|---|---:|---:|
| 0 | Tidak Churn | 12.702 | 84,68% |
| 1 | Churn | 2.298 | 15,32% |

Dari hasil tersebut, terlihat bahwa jumlah pelanggan tidak churn lebih dominan dibandingkan pelanggan churn. Hal ini perlu diperhatikan karena dapat memengaruhi performa model klasifikasi.

---

### 8. Korelasi Fitur Numerik

Heatmap korelasi dibuat untuk melihat hubungan antar fitur numerik. Selain itu, korelasi fitur numerik terhadap target `churn` juga dianalisis.

Beberapa fitur yang perlu diperhatikan dari hasil korelasi terhadap `churn` antara lain:

- `satisfaction_score`
- `total_spent`
- `support_tickets`

Fitur tersebut dapat menjadi perhatian pada tahap modeling karena berhubungan dengan perilaku dan pengalaman pelanggan.

---

### 9. Analisis Fitur Pemasaran dan Transaksi

Pada dataset ini, analisis pemasaran disesuaikan dengan kolom yang tersedia, seperti:

- `acquisition_channel`
- `marketing_spend_per_user`
- `total_spent`
- `avg_order_value`
- `lifetime_value`
- `email_open_rate`
- `email_click_rate`

Analisis dilakukan untuk melihat gambaran awal hubungan antara aktivitas pemasaran, transaksi pelanggan, dan status churn.

---

## Output Minggu 8

Output yang dihasilkan pada minggu ke-8:

```bash
notebooks/01_eda.ipynb
outputs/figures/missing_values.png
outputs/figures/churn_distribution.png
outputs/figures/correlation_heatmap.png
outputs/figures/churn_numeric_correlation.png
outputs/figures/acquisition_channel_distribution.png
outputs/figures/churn_by_acquisition_channel.png
outputs/figures/lifetime_value_by_churn.png
outputs/figures/marketing_spend_by_churn.png
progress/week_1.md
```

---

## Kesimpulan Minggu 8

Pada minggu ke-8, tahap setup project dan EDA sudah dilakukan. Dataset berhasil dimuat dan dianalisis untuk memahami kondisi awal data.

Hasil EDA menunjukkan bahwa dataset memiliki beberapa missing value, distribusi target churn yang tidak seimbang, serta beberapa fitur numerik yang memiliki hubungan dengan churn pelanggan.

Tahap ini belum masuk ke proses modeling. Hasil dari EDA digunakan sebagai dasar untuk menentukan kebutuhan preprocessing dan menjadi acuan sebelum membangun model pada tahap berikutnya.

---

## Pemahaman

Minggu ke-8 berfungsi sebagai tahap awal untuk memahami data. Pada tahap ini saya belum membangun model, tetapi fokus pada pengecekan kondisi dataset, distribusi target, missing value, korelasi fitur numerik, serta analisis awal fitur pemasaran dan transaksi.

Hasil dari tahap ini menjadi dasar untuk melanjutkan ke direct modeling pada minggu berikutnya.
