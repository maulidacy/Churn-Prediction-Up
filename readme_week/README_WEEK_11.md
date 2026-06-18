# Progress Minggu 11 - Hyperparameter Tuning dan Feature Selection

## Deskripsi Progress

Pada minggu ke-11, pengerjaan proyek difokuskan pada tahap **Hyperparameter Tuning dan Feature Selection**. Tahap ini dilakukan setelah direct modeling dan modeling dengan preprocessing.

Tujuan utama pada minggu ini adalah mencari konfigurasi parameter yang lebih optimal dari model yang sudah digunakan sebelumnya, kemudian mengevaluasi kembali performanya pada data uji.

Target prediksi pada proyek ini tetap menggunakan kolom `churn`.

Keterangan target:

- `churn = 0` : pelanggan tidak churn
- `churn = 1` : pelanggan churn

---

## Tujuan Minggu 11

Tujuan pengerjaan pada minggu ke-11 adalah:

1. Melakukan feature importance untuk melihat fitur yang berpengaruh.
2. Melakukan feature selection agar model menggunakan fitur yang lebih relevan.
3. Menyusun ruang pencarian hyperparameter untuk setiap model.
4. Melakukan hyperparameter tuning menggunakan RandomizedSearchCV.
5. Menggunakan Stratified K-Fold cross-validation pada proses tuning.
6. Mendapatkan best estimator dan best parameters.
7. Mengevaluasi model hasil tuning menggunakan data uji.
8. Menyimpan hasil tuning, selected features, dan model terbaik.

---

## Tahapan yang Dilakukan

### 1. Load Dataset

Dataset dibaca dari folder:

```bash
data/raw/Sales - Marketing customer dataset.csv
```

Dataset yang digunakan masih sama seperti tahap sebelumnya agar hasil antar skenario dapat dibandingkan secara adil.

---

### 2. Train-Test Split

Data dibagi menjadi data latih dan data uji dengan proporsi 80:20.

Hasil pembagian data:

- Data latih: 12.000 data
- Data uji: 3.000 data

Pembagian data dilakukan sebelum preprocessing dan tuning untuk menghindari data leakage. Data uji hanya digunakan pada evaluasi akhir setelah proses tuning selesai.

---

### 3. Feature Engineering

Pada tahap ini dilakukan feature engineering dari kolom tanggal dan coupon code.

Fitur baru yang dibuat:

- `customer_tenure_days`
- `days_since_last_purchase`
- `signup_month`
- `last_purchase_month`
- `has_coupon_code`

Kolom yang tidak digunakan secara langsung:

- `customer_id`
- `signup_date`
- `last_purchase_date`
- `coupon_code`

Kolom tersebut dihapus karena sudah tidak digunakan secara langsung atau sudah diwakili oleh fitur baru.

---

### 4. Handling Outlier

Outlier ditangani menggunakan metode IQR capping.

Capping hanya diterapkan pada kolom numerik kontinu, bukan pada kolom biner. Kolom seperti `discount_used`, `refund_requested`, `is_premium_user`, dan `has_coupon_code` tidak ikut di-capping karena nilainya memang berupa indikator 0/1.

---

### 5. Pipeline Preprocessing

Preprocessing dilakukan menggunakan `ColumnTransformer`.

Tahapan untuk fitur numerik:

- imputasi missing value menggunakan median,
- scaling menggunakan StandardScaler.

Tahapan untuk fitur kategorikal:

- imputasi missing value menggunakan nilai paling sering muncul,
- encoding menggunakan OneHotEncoder.

Preprocessor hanya di-fit pada data latih, kemudian digunakan untuk mentransformasi data latih dan data uji.

---

### 6. Feature Importance

Feature importance dilakukan menggunakan Random Forest Classifier. Tujuannya adalah melihat fitur mana yang dianggap paling berpengaruh oleh model.

Hasil feature importance disimpan ke file:

```bash
outputs/reports/feature_importance_hyperparameter_tuning.csv
```

Visualisasi feature importance disimpan ke file:

```bash
outputs/figures/feature_importance_hyperparameter_tuning.png
```

---

### 7. Feature Selection

Feature selection dilakukan menggunakan `SelectFromModel` dengan Random Forest sebagai estimator.

Feature selector dimasukkan ke dalam pipeline tuning agar proses pemilihan fitur dilakukan di dalam proses training. Jumlah fitur yang diuji pada proses tuning adalah 30, 50, dan 80 fitur.

---

### 8. Hyperparameter Tuning

Hyperparameter tuning dilakukan menggunakan `RandomizedSearchCV` dengan Stratified K-Fold cross-validation.

Model yang dituning:

1. Logistic Regression
2. Random Forest Classifier
3. Voting Classifier

Scoring utama yang digunakan adalah F1-Score karena data churn memiliki distribusi kelas yang tidak seimbang.

---

## Hasil Evaluasi Hyperparameter Tuning

| No | Model | Best CV F1-Score | Accuracy | Precision | Recall | F1-Score |
|---|---|---:|---:|---:|---:|---:|
| 1 | Logistic Regression | 0.482822 | 0.752000 | 0.353002 | 0.741304 | 0.478261 |
| 2 | Random Forest Classifier | 0.660387 | 0.852333 | 0.509759 | 0.965217 | 0.667168 |
| 3 | Voting Classifier | 0.656125 | 0.855333 | 0.514977 | 0.971739 | 0.673193 |

Berdasarkan hasil evaluasi pada data uji, model terbaik pada tahap hyperparameter tuning adalah **Voting Classifier** dengan F1-Score sebesar **0.673193**.

Voting Classifier juga menghasilkan recall tertinggi, yaitu **0.971739**, sehingga model ini paling baik pada tahap tuning dalam mengenali pelanggan yang benar-benar churn.

---

## Best Parameters Model Terbaik

Best parameters untuk model Voting Classifier:

```python
{
    "selector__max_features": 50,
    "model__weights": (1, 2, 1),
    "model__nb__var_smoothing": 1e-07,
    "model__lr__class_weight": "balanced",
    "model__lr__C": 10,
    "model__dt__min_samples_leaf": 2,
    "model__dt__max_depth": 3,
    "model__dt__class_weight": "balanced"
}
```

---

## Perbandingan dengan Skenario Sebelumnya

Pada tahap ini, hasil hyperparameter tuning juga digabungkan dengan hasil direct modeling dan preprocessing. Total model yang dibandingkan sementara berjumlah 9 model.

Ringkasan skenario:

- 3 model pada Direct Modeling
- 3 model pada Preprocessing
- 3 model pada Hyperparameter Tuning

Hasil perbandingan sementara disimpan ke file:

```bash
outputs/reports/model_results_all_scenarios.csv
models/model_results.csv
```

---

## Output Minggu 11

Output yang dihasilkan pada minggu ke-11:

```bash
notebooks/04_hyperparameter_tuning.ipynb

outputs/reports/feature_importance_hyperparameter_tuning.csv
outputs/reports/hyperparameter_tuning_results.csv
outputs/reports/best_parameters_summary.csv
outputs/reports/selected_features_best_tuned_model.csv
outputs/reports/model_results_all_scenarios.csv

outputs/reports/cv_results_tuning_logistic_regression.csv
outputs/reports/cv_results_tuning_random_forest.csv
outputs/reports/cv_results_tuning_voting_classifier.csv

outputs/figures/feature_importance_hyperparameter_tuning.png
outputs/figures/confusion_matrix_tuning_logistic_regression.png
outputs/figures/confusion_matrix_tuning_random_forest.png
outputs/figures/confusion_matrix_tuning_voting_classifier.png

models/best_model.pkl
models/best_tuned_estimator.pkl
models/model_results.csv
```

---

## Kesimpulan Minggu 11

Pada minggu ke-11, hyperparameter tuning dan feature selection sudah dilakukan pada tiga model, yaitu Logistic Regression, Random Forest Classifier, dan Voting Classifier.

Hasil evaluasi menunjukkan bahwa Voting Classifier menjadi model terbaik pada tahap tuning dengan F1-Score tertinggi sebesar 0.673193. Model ini juga memiliki recall yang tinggi, sehingga cukup baik dalam mendeteksi pelanggan yang berpotensi churn.

Tahap ini belum masuk ke deployment. Hasil tuning akan digunakan pada tahap berikutnya untuk membandingkan seluruh skenario secara final pada notebook `05_model_comparison.ipynb`.

---

## Pemahaman Singkat

Minggu ke-11 berfungsi untuk mengoptimalkan model. Pada tahap ini saya tidak hanya melatih model dengan parameter dasar, tetapi mencoba beberapa kombinasi parameter menggunakan RandomizedSearchCV.

Hasil tuning menunjukkan bahwa performa model meningkat dibandingkan tahap sebelumnya, terutama pada recall dan F1-Score. Hal ini penting karena pada kasus churn, model perlu mampu mendeteksi pelanggan yang benar-benar berpotensi churn.
