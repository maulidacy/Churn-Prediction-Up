# Progress Minggu 9 - Direct Modeling

## Deskripsi Progress

Pada minggu ke-9, pengerjaan proyek difokuskan pada tahap Direct Modeling sebagai tahap kedua dari alur pengerjaan proyek prediksi churn pelanggan.

Tahap ini dilakukan untuk membangun model baseline awal sebelum dilakukan preprocessing penuh dan hyperparameter tuning. Hasil dari tahap ini digunakan sebagai pembanding untuk melihat apakah preprocessing dan tuning pada tahap berikutnya dapat meningkatkan performa model.

Target prediksi pada proyek ini adalah:

- `churn = 0` : pelanggan tidak churn
- `churn = 1` : pelanggan churn

---

## Tujuan Minggu 9

Tujuan pengerjaan pada minggu ke-9 adalah:

1. Menentukan fitur prediktor dan target.
2. Menggunakan kolom `churn` sebagai target prediksi.
3. Menggunakan seluruh kolom selain `churn` sebagai fitur awal.
4. Membagi dataset menjadi data latih dan data uji.
5. Melatih tiga model machine learning sebagai baseline.
6. Mengevaluasi performa model menggunakan metrik klasifikasi.
7. Menyimpan hasil evaluasi dan confusion matrix.

---

## Tahapan yang Dilakukan

### 1. Load Dataset

Dataset dibaca dari folder:

```bash
data/raw/Sales - Marketing customer dataset.csv
```

Setelah dataset dimuat, dilakukan pengecekan awal seperti:

- melihat 5 baris pertama data,
- melihat jumlah baris dan kolom,
- melihat informasi tipe data setiap kolom.

---

### 2. Menentukan Fitur dan Target

Kolom `churn` digunakan sebagai target prediksi.

```python
y = df["churn"]
X = df.drop(columns=["churn"])
```

Seluruh kolom selain `churn` digunakan sebagai fitur prediktor pada tahap direct modeling.

---

### 3. Konversi Teknis Minimum

Dataset masih memiliki kolom kategorikal, kolom tanggal berbentuk object, dan missing value. Agar data dapat digunakan oleh model scikit-learn, dilakukan konversi teknis minimum.

Tahapan yang dilakukan:

- Missing value pada kolom kategorikal diisi dengan `"Missing"`.
- Missing value pada kolom numerik diisi dengan `-1`.
- Kolom kategorikal diubah menjadi numerik menggunakan `pd.get_dummies()`.

Tahap ini belum dianggap sebagai preprocessing penuh karena belum dilakukan:

- handling outlier,
- scaling,
- feature selection,
- penghapusan fitur tidak relevan secara mendalam,
- hyperparameter tuning.

Preprocessing lengkap akan dilakukan pada tahap berikutnya.

---

### 4. Train-Test Split

Dataset dibagi menjadi data latih dan data uji dengan proporsi 80:20.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X_direct,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

Parameter `stratify=y` digunakan agar proporsi kelas churn dan tidak churn tetap seimbang pada data latih dan data uji.

---

## Model yang Digunakan

Pada minggu ke-9 digunakan tiga model machine learning sesuai kategori model pada tugas.

### 1. Logistic Regression

Logistic Regression digunakan sebagai model konvensional. Model ini dipilih sebagai baseline karena sederhana dan umum digunakan untuk kasus klasifikasi biner.

### 2. Random Forest Classifier

Random Forest digunakan sebagai model ensemble bagging. Model ini bekerja dengan membangun banyak decision tree dan menggabungkan hasil prediksinya.

### 3. Voting Classifier

Voting Classifier digunakan sebagai model ensemble gabungan. Pada tahap ini, Voting Classifier menggabungkan beberapa model dasar untuk menghasilkan prediksi akhir.

Model dasar yang digunakan pada Voting Classifier:

- Logistic Regression
- Decision Tree Classifier
- Gaussian Naive Bayes

---

## Evaluasi Model

Metrik evaluasi yang digunakan pada minggu ke-9:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Pada kasus churn, F1-Score dan Recall penting untuk diperhatikan karena target churn memiliki distribusi kelas yang tidak seimbang. Accuracy saja belum cukup untuk menilai performa model karena model bisa terlihat baik meskipun kurang mampu mendeteksi pelanggan yang benar-benar churn.

---

## Output Minggu 9

Output yang dihasilkan pada minggu ke-9:

```bash
notebooks/02_direct_modeling.ipynb
outputs/reports/direct_modeling_results.csv
outputs/figures/confusion_matrix_direct_logistic_regression.png
outputs/figures/confusion_matrix_direct_random_forest.png
outputs/figures/confusion_matrix_direct_voting_classifier.png
progress/week_2.md
```

---

## Hasil Evaluasi Sementara

| No | Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---:|---:|---:|---:|
| 1 | Logistic Regression | 0.836000 | 0.289474 | 0.047826 | 0.082090 |
| 2 | Random Forest Classifier | 0.846667 | 0.500000 | 0.008696 | 0.017094 |
| 3 | Voting Classifier | 0.842333 | 0.465241 | 0.189130 | 0.268934 |

Berdasarkan hasil direct modeling, Voting Classifier menjadi model baseline terbaik sementara karena memiliki nilai F1-Score paling tinggi dibandingkan dua model lainnya.

Meskipun Random Forest memiliki accuracy paling tinggi, recall dan F1-Score untuk kelas churn masih sangat rendah. Oleh karena itu, accuracy saja belum cukup untuk menentukan model terbaik pada kasus churn.

---

## Kesimpulan Minggu 9

Pada minggu ke-9, tahap direct modeling telah dilakukan untuk membangun baseline awal model prediksi churn pelanggan.

Tiga model yang digunakan adalah Logistic Regression, Random Forest Classifier, dan Voting Classifier. Model dilatih menggunakan data yang sudah melalui konversi teknis minimum agar dapat dijalankan oleh scikit-learn.

Hasil evaluasi menunjukkan bahwa Voting Classifier memiliki F1-Score terbaik sementara pada tahap direct modeling. Namun, hasil ini belum menjadi model final karena belum dilakukan preprocessing penuh dan hyperparameter tuning.

Hasil dari tahap ini akan digunakan sebagai pembanding untuk tahap berikutnya, yaitu modeling dengan preprocessing.

---

## Pemahaman

Minggu ke-9 berfungsi sebagai tahap baseline modeling. Pada tahap ini saya mulai membangun model awal untuk melihat performa dasar sebelum data diproses lebih lanjut.

Direct modeling penting karena menjadi pembanding awal. Dengan adanya baseline ini, peningkatan performa pada tahap preprocessing dan hyperparameter tuning nantinya dapat dilihat dengan lebih jelas.

Intinya, hasil minggu ke-9 belum menjadi model final, tetapi menjadi dasar pembanding untuk proses modeling berikutnya.
