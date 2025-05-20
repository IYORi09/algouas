NAMA KELOMPOK 5 TUGAS FINAL ALGORITMA & PEMROGRAMAN :
1. Muh. Rizky Zaldy JR (240907500022)
2. Farel Ramadhani Putra (240907501043)
3. Sitti Asmaul Khusnah (240907501041)
4. Erika Desi Saputri (240907502025)
5. Nur Ulfiah Triputri Iskandar (240907502030)
6. Nahdatunnisa Alfitrah (240907502031)

# 📊 Analisis Tingkat Pengangguran dan Pendidikan

Program ini merupakan aplikasi berbasis Streamlit, sebuah framework Python yang memungkinkan pembuatan aplikasi web interaktif secara cepat dan efisien.
Tujuan utama dari program ini adalah untuk menganalisis hubungan antara tingkat pendidikan dan tingkat pengangguran melalui pendekatan statistik berupa 
korelasi Pearson dan regresi linear sederhana. Analisis ini penting karena pendidikan merupakan salah satu faktor utama yang memengaruhi tingkat partisipasi 
angkatan kerja dan pengangguran dalam suatu negara. Dalam banyak literatur ekonomi, ditemukan bahwa semakin tinggi tingkat pendidikan seseorang, 
maka peluangnya untuk mendapatkan pekerjaan cenderung lebih besar, dan tingkat penganggurannya lebih rendah.

- Struktur dan Sumber Data
Untuk keperluan analisis ini, digunakan data dummy atau simulasi yang mewakili kecenderungan umum dalam masyarakat.
Data terdiri dari dua kolom:
Tingkat_Pendidikan:
skala ordinal dari 1 hingga 5,
di mana 1 mewakili SD,
2 untuk SMP, 3 untuk SMA,
4 untuk D3, dan 5 untuk S1 ke atas.

- Tingkat_Pengangguran:
angka dalam persentase yang menunjukkan proporsi pengangguran pada tiap jenjang pendidikan.
Penggunaan data dummy ini bertujuan untuk menyederhanakan proses dan memberi gambaran tentang alur analisis,
namun metode ini dapat dengan mudah diadaptasi untuk data riil yang bersumber dari instansi seperti BPS
(Badan Pusat Statistik) atau World Bank Open Data.

Data ini kemudian dimasukkan ke dalam struktur DataFrame menggunakan pustaka pandas, 
yang memberikan fleksibilitas tinggi dalam pemrosesan data tabular di Python. 
Pandas memungkinkan pengguna untuk dengan cepat memvisualisasikan, memfilter, dan mengubah data.

- Analisis Korelasi
Langkah pertama dalam analisis adalah menghitung korelasi Pearson antara variabel tingkat pendidikan
dan tingkat pengangguran menggunakan numpy.corrcoef(). Korelasi Pearson mengukur kekuatan dan arah hubungan linier antara dua variabel numerik.
Nilai korelasi berkisar dari -1 hingga 1, dengan:
Nilai mendekati +1 menandakan korelasi positif yang kuat (kedua variabel naik bersama),
Nilai mendekati -1 menandakan korelasi negatif yang kuat (satu naik, yang lain turun),
Nilai mendekati 0 menandakan hubungan linier yang lemah atau tidak ada.

Dalam kasus ini, korelasi negatif menunjukkan bahwa semakin tinggi tingkat pendidikan seseorang,
tingkat pengangguran yang dialami cenderung lebih rendah. 
Hal ini sejalan dengan teori modal manusia (human capital theory), yang menyatakan bahwa investasi dalam pendidikan meningkatkan produktivitas tenaga kerja,
yang pada akhirnya memperbesar peluang kerja (Becker, 1964).

- Regresi Linear Sederhana
Setelah mengetahui hubungan awal melalui korelasi, analisis dilanjutkan dengan regresi linear sederhana menggunakan LinearRegression dari pustaka scikit-learn.
 Regresi linear digunakan untuk memodelkan hubungan sebab-akibat antara satu variabel independen (Tingkat_Pendidikan) dan satu variabel dependen (Tingkat_Pengangguran).
Dengan kata lain, regresi ini menjawab pertanyaan: seberapa besar perubahan pada pengangguran yang dapat dijelaskan oleh perubahan pada pendidikan?

- Model regresi menghasilkan dua komponen utama:
Intercept (konstanta): nilai awal pengangguran saat pendidikan = 0 (meskipun dalam konteks ini, nilai 0 tidak bermakna karena skala mulai dari 1).
Koefisien regresi: nilai yang menunjukkan seberapa besar perubahan pengangguran untuk setiap kenaikan satu tingkat pendidikan.

Sebagai tambahan, nilai koefisien determinasi (R²) dihitung menggunakan r2_score, yang menunjukkan seberapa besar proporsi variasi
dalam tingkat pengangguran yang dapat dijelaskan oleh variasi dalam tingkat pendidikan. Misalnya, nilai R² = 0,90 berarti 90% 
variasi tingkat pengangguran dapat dijelaskan oleh perbedaan tingkat pendidikan. Ini adalah indikator penting untuk menilai kekuatan prediktif model.

- Visualisasi dan Interpretasi
Hasil analisis kemudian divisualisasikan dalam bentuk scatter plot (diagram sebar) menggunakan pustaka matplotlib, dengan:
Titik-titik biru yang mewakili data asli,
Garis merah yang menggambarkan garis regresi linear sebagai hasil prediksi model.
Visualisasi ini membantu pengguna untuk dengan cepat melihat pola hubungan antara pendidikan
dan pengangguran secara kasat mata. Grafik ini kemudian disematkan ke halaman Streamlit menggunakan st.pyplot(),
sehingga pengguna bisa langsung berinteraksi dengan hasilnya melalui antarmuka web.

Streamlit secara khusus dipilih dalam aplikasi ini karena sangat cocok untuk membuat prototipe analisis data dengan tampilan yang rapi dan mudah digunakan.
Pengguna hanya perlu menjalankan script Python, dan secara otomatis akan dibuka halaman web lokal yang menampilkan semua komponen analisis — dari data mentah,
hasil hitung, hingga visualisasi.

- Potensi Pengembangan
Meskipun program ini menggunakan data simulasi, metode yang digunakan bersifat umum dan dapat diperluas.
Pengguna bisa mengimpor data asli dari file Excel, CSV, atau database.
Selain itu, model dapat dikembangkan menjadi regresi multivariat jika terdapat lebih dari satu faktor yang memengaruhi pengangguran,
seperti umur, jenis kelamin, lokasi geografis, dan lain-lain. Penggunaan model machine learning seperti Random Forest Regression atau
XGBoost juga dapat menjadi opsi jika hubungan antar variabel bersifat non-linier.

Secara keseluruhan, aplikasi ini bukan hanya berguna sebagai sarana analisis sederhana, tetapi juga sebagai alat edukatif untuk memahami
bagaimana data statistik dapat digunakan dalam pembuatan keputusan berbasis data (data-driven decision making), khususnya di bidang pendidikan dan ketenagakerjaan.



Referensi:
- Becker, G. S. (1964). Human Capital:
  A Theoretical and Empirical Analysis, with Special Reference to Education. University of Chicago Press.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).
   An Introduction to Statistical Learning: with Applications in R. Springer.
- Psacharopoulos, G., & Patrinos, H. A. (2018).
   Returns to investment in education: a decennial review of the global literature. Education Economics, 26(5), 445–458.
- McKinney, W. (2010). Data Structures for Statistical Computing in Python.
  Proceedings of the 9th Python in Science Conference.
- Scikit-learn: Linear Regression.
  https://scikit-learn.org/stable/modules/linear_model.html



## 📦 Instalasi

```bash
pip install -r requirements.txt
