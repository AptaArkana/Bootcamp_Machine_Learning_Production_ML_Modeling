# Bootcamp Machine Learning Production ML Modeling
<p align='justify'>Lanjutan dari tugas sebelumnya setelah dilakukan tahapan preprocessing maka masuk tahap selanjutnya yaitu tahap modeling, untuk melacak version dari model projek ini menggunakan <a href="https://neptune.ai/">Neptune</a></p>

# Laporan Klasifikasi SVM

Hasil klasifikasi menggunakan Support Vector Machine (SVM) menunjukkan berbagai tingkat keberhasilan dalam mendeteksi emosi. Berikut adalah rincian performa model:

- **Anger (Marah):** Model memiliki precision sebesar 0.59 dan recall sebesar 0.80, menghasilkan f1-score sebesar 0.68. Dari 220 sampel, 80% dapat diklasifikasikan dengan benar.
- **Fear (Takut):** Model memiliki precision yang sangat tinggi sebesar 0.89, namun recall yang lebih rendah sebesar 0.56, menghasilkan f1-score sebesar 0.69. Dari 130 sampel, hanya 56% yang diklasifikasikan dengan benar.
- **Happy (Bahagia):** Precision adalah 0.64 dan recall 0.60, dengan f1-score sebesar 0.62. Dari 204 sampel, 60% diklasifikasikan dengan benar.
- **Love (Cinta):** Model memiliki precision sebesar 0.86 dan recall sebesar 0.62, menghasilkan f1-score sebesar 0.72. Dari 127 sampel, 62% diklasifikasikan dengan benar.
- **Sadness (Sedih):** Precision adalah 0.49 dan recall 0.53, dengan f1-score sebesar 0.51. Dari 200 sampel, 53% diklasifikasikan dengan benar.

Secara keseluruhan, akurasi model adalah 63% dari total 881 sampel. Rata-rata makro (macro average) untuk precision, recall, dan f1-score masing-masing adalah 0.69, 0.62, dan 0.64. Sedangkan rata-rata tertimbang (weighted average) adalah 0.66, 0.63, dan 0.64.

## Saran Perbaikan
1. **Penambahan Data Latih:** Menambah jumlah data latih terutama untuk kelas dengan performa rendah seperti "sadness" dapat membantu meningkatkan akurasi dan f1-score.
2. **Penyeimbangan Data:** Melakukan penyeimbangan data untuk mengurangi bias terhadap kelas dengan jumlah sampel yang lebih sedikit.
3. **Penyempurnaan Fitur:** Melakukan teknik pemilihan fitur (feature selection) yang lebih baik atau menambah fitur yang lebih relevan untuk setiap kategori emosi.
4. **Penggunaan Model Lain:** Mencoba algoritma lain seperti Random Forest atau Neural Networks yang mungkin memberikan hasil yang lebih baik.
5. **Fine-Tuning Hyperparameters:** Melakukan pencarian hyperparameter (hyperparameter tuning) untuk SVM agar performa model bisa dioptimalkan.

