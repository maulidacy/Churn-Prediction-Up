# Progress Minggu 10 - Modeling dengan Preprocessing

## Deskripsi Progress

Pada minggu ke-10, pengerjaan proyek difokuskan pada tahap **modeling dengan preprocessing**. Tahap ini dilakukan setelah direct modeling, sehingga hasilnya dapat dibandingkan dengan baseline awal pada minggu sebelumnya.

Pada tahap ini, data tidak langsung digunakan dalam kondisi mentah. Dataset diproses terlebih dahulu agar lebih siap digunakan oleh model machine learning. Preprocessing dilakukan dengan memperhatikan urutan yang tepat, yaitu data dibagi terlebih dahulu menjadi data latih dan data uji, kemudian proses preprocessing diterapkan berdasarkan data latih.

Target prediksi pada proyek ini adalah:

- `churn = 0` : pelanggan tidak churn
- `churn = 1` : pelanggan churn

---

## Tujuan Minggu 10

Tujuan pengerjaan pada minggu ke-10 adalah:

1. Melakukan preprocessing data sebelum modeling.
2. Membagi data menjadi data latih dan data uji sebelum preprocessing lanjutan.
3. Membuat fitur baru dari kolom tanggal.
4. Menghapus atau menyesuaikan fitur yang kurang relevan.
5. Menangani data duplikat.
6. Menangani missing value.
7. Menangani outlier pada fitur numerik kontinu.
8. Melakukan encoding pada fitur kategorikal.
9. Melakukan scaling pada fitur numerik.
10. Melatih ulang tiga model yang sama seperti direct modeling.
11. Mengevaluasi hasil model setelah preprocessing.
12. Membandingkan hasil preprocessing dengan hasil direct modeling.

---

## Tahapan yang Dilakukan

### 1. Load Dataset

Dataset dibaca dari folder:

```bash
data/raw/Sales - Marketing customer dataset.csv
```

Setelah dataset dimuat, dilakukan pengecekan awal seperti melihat ukuran dataset dan informasi tipe data.

---

### 2. Handling Duplikasi

Data duplikat dicek terlebih dahulu sebelum proses modeling. Jika terdapat duplikasi, data tersebut dihapus agar tidak mengganggu proses training dan evaluasi.

Pada hasil pengecekan, tidak ditemukan data duplikat pada dataset.

---

### 3. Menentukan Fitur dan Target

Kolom `churn` digunakan sebagai target prediksi.

```python
y = df["churn"]
X = df.drop(columns=["churn"])
```

Seluruh kolom selain `churn` digunakan sebagai fitur awal sebelum dilakukan feature engineering dan preprocessing.

---

### 4. Train-Test Split

Data dibagi menjadi data latih dan data uji dengan proporsi 80:20.

Pembagian dilakukan sebelum preprocessing lanjutan untuk menghindari data leakage. Dengan cara ini, proses seperti imputasi, scaling, dan perhitungan batas outlier hanya belajar dari data latih, bukan dari data uji.

---

### 5. Feature Engineering

Feature engineering dilakukan pada kolom tanggal dan kupon.

Kolom tanggal yang digunakan:

- `signup_date`
- `last_purchase_date`

Dari kolom tersebut dibuat beberapa fitur baru:

- `customer_tenure_days`
- `days_since_last_purchase`
- `signup_month`
- `last_purchase_month`

Selain itu, kolom `coupon_code` diubah menjadi fitur:

- `has_coupon_code`

Fitur `customer_id`, `signup_date`, `last_purchase_date`, dan `coupon_code` kemudian dihapus karena sudah tidak digunakan dalam bentuk aslinya.

---

### 6. Handling Outlier

Outlier ditangani menggunakan metode IQR capping. Capping hanya diterapkan pada fitur numerik kontinu, bukan pada fitur biner seperti `discount_used`, `refund_requested`, `is_premium_user`, dan `has_coupon_code`.

Kolom yang digunakan untuk outlier capping antara lain:

- `age`
- `total_visits`
- `avg_session_time`
- `pages_per_session`
- `email_open_rate`
- `email_click_rate`
- `total_spent`
- `avg_order_value`
- `support_tickets`
- `delivery_delay_days`
- `marketing_spend_per_user`
- `lifetime_value`
- `last_3_month_purchase_freq`
- `customer_tenure_days`
- `days_since_last_purchase`

Batas outlier dihitung dari data latih, kemudian diterapkan pada data latih dan data uji.

---

### 7. Pipeline Preprocessing

Preprocessing dilakukan menggunakan pipeline agar prosesnya lebih rapi dan konsisten.

Untuk fitur numerik:

- missing value diisi menggunakan median,
- fitur numerik di-scaling menggunakan StandardScaler.

Untuk fitur kategorikal:

- missing value diisi menggunakan nilai yang paling sering muncul,
- fitur kategorikal diubah menjadi numerik menggunakan OneHotEncoder.

Pipeline preprocessing juga disimpan ke folder `models`.

---

## Model yang Digunakan

Model yang digunakan pada minggu ke-10 sama seperti tahap direct modeling agar hasilnya dapat dibandingkan secara adil.

### 1. Logistic Regression

Digunakan sebagai model konvensional untuk klasifikasi biner.

### 2. Random Forest Classifier

Digunakan sebagai model ensemble bagging.

### 3. Voting Classifier

Digunakan sebagai model ensemble gabungan dari beberapa model dasar.

Model dasar pada Voting Classifier:

- Logistic Regression
- Decision Tree Classifier
- Gaussian Naive Bayes

---

## Evaluasi Model

Metrik evaluasi yang digunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Pada kasus churn, F1-Score dan Recall tetap diperhatikan karena jumlah pelanggan churn lebih sedikit dibandingkan pelanggan tidak churn.

---

## Hasil Evaluasi Minggu 10

| No | Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---:|---:|---:|---:|
| 1 | Logistic Regression | 0.846000 | 0.493056 | 0.154348 | 0.235099 |
| 2 | Random Forest Classifier | 0.844333 | 0.480663 | 0.189130 | 0.271451 |
| 3 | Voting Classifier | 0.847333 | 0.505376 | 0.204348 | 0.291022 |

Berdasarkan hasil evaluasi, **Voting Classifier** menjadi model terbaik sementara pada skenario preprocessing karena memiliki nilai F1-Score tertinggi.

---

## Perbandingan dengan Direct Modeling

Hasil preprocessing juga dibandingkan dengan hasil direct modeling.

| Skenario | Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---:|---:|---:|---:|
| Direct Modeling | Logistic Regression | 0.836000 | 0.289474 | 0.047826 | 0.082090 |
| Direct Modeling | Random Forest | 0.846667 | 0.500000 | 0.008696 | 0.017094 |
| Direct Modeling | Voting Classifier | 0.842333 | 0.465241 | 0.189130 | 0.268934 |
| Preprocessing | Logistic Regression | 0.846000 | 0.493056 | 0.154348 | 0.235099 |
| Preprocessing | Random Forest | 0.844333 | 0.480663 | 0.189130 | 0.271451 |
| Preprocessing | Voting Classifier | 0.847333 | 0.505376 | 0.204348 | 0.291022 |

Dari hasil tersebut, preprocessing memberikan peningkatan terutama pada F1-Score beberapa model. Voting Classifier tetap menjadi model terbaik sementara berdasarkan F1-Score.

---

## Output Minggu 10

Output yang dihasilkan pada minggu ke-10:

```bash
notebooks/03_preprocessing_modeling.ipynb
data/processed/churn_cleaned.csv
outputs/reports/outlier_summary_preprocessing.csv
outputs/reports/preprocessing_modeling_results.csv
outputs/reports/model_results_partial.csv
outputs/reports/feature_importance_preprocessing_random_forest.csv
outputs/figures/confusion_matrix_preprocessing_logistic_regression.png
outputs/figures/confusion_matrix_preprocessing_random_forest.png
outputs/figures/confusion_matrix_preprocessing_voting_classifier.png
outputs/figures/feature_importance_preprocessing_random_forest.png
models/preprocessing_pipeline.pkl
models/best_preprocessing_model.pkl
```

---

## Kesimpulan Minggu 10

Pada minggu ke-10, tahap modeling dengan preprocessing sudah dilakukan. Data diproses melalui feature engineering, handling duplikasi, handling outlier, missing value, encoding, dan scaling.

Tiga model yang sama seperti direct modeling dilatih ulang menggunakan data hasil preprocessing. Berdasarkan hasil evaluasi, Voting Classifier menjadi model terbaik sementara pada skenario preprocessing dengan F1-Score sebesar 0.291022.

Hasil ini belum menjadi model final karena masih akan dilanjutkan ke tahap hyperparameter tuning dan perbandingan seluruh skenario.

---

## Pemahaman Singkat

Minggu ke-10 berfungsi untuk melihat pengaruh preprocessing terhadap performa model. Tahap ini penting karena data mentah belum sepenuhnya siap untuk digunakan oleh model machine learning.

Preprocessing dilakukan setelah train-test split agar tidak terjadi data leakage. Dengan begitu, model diuji pada data yang benar-benar belum digunakan dalam proses preprocessing maupun training.

Hasil dari minggu ke-10 akan menjadi pembanding untuk tahap berikutnya, yaitu hyperparameter tuning.
