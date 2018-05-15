<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>


### Specifications

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan data scraping pada spreadsheet berikut: [Topik Data Scraping](http://bit.ly/TopikDataScraping). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal 10 Mei 2018 pukul 20.00 WIB

3. Dalam mengerjakan tugas 1, calon warga basdat terlebih dahulu melakukan fork project github pada link berikut: https://github.com/wargabasdat/Seleksi-2018/tree/master/Tugas1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan pull request dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada repository tersebut, calon warga basdat harus mengumpulkan file script dan json hasil data scraping. Repository terdiri dari folder src dan data dimana folder src berisi file script/kode yang __WELL DOCUMENTED dan CLEAN CODE__ sedangkan folder data berisi file json hasil scraper.

5. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

``` Makefile
all: clean build run

clean: # remove data and binary folder

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary

```

6. Deadline pengumpulan tugas adalah __15 Mei 2018 Pukul 23.59__

7. Tugas 1 akan didemokan oleh masing-masing calon warga basdat

8. Demo tugas mencakup keseluruhan proses data scraping hingga memeroleh data sesuai dengan yang dikumpulkan pada Tugas 1

9. Hasil data scraping ini nantinya akan digunakan sebagai bahan tugas analisis dan visualisasi data

10. Sebagai referensi untuk mengenal data scraping, asisten menyediakan dokumen "Short Guidance To Data Scraping" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

11. Tambahkan juga gitignore pada file atau folder yang tidak perlu di upload, __NB : BINARY TIDAK DIUPLOAD__

12. JSON harus dinormalisasi dan harus di-_preprocessing_
```
Preprocessing contohnya :
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

13. Berikan README yang __WELL DOCUMENTED__ dengan cara __override__ file README.md ini. README harus memuat minimal konten :
```
- Description
- Specification
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```

<h1 align="center">
  <br>
  Selamat BerEksplorasi!
  <br>
  <br>
</h1>

<p align="center">
  <br>
  Basdat Industries - Lab Basdat 2018
  <br>
  <br>
</p>



# Description
  Aplikasi Ini digunakan untuk melakukan scraping terhadap data gempa sepanjang maksimal 1 tahun dari situs http://repogempa.bmkg.go.id/

# Specification
  1. Aplikasi ini dapat mencari data tentang gempa dari situs http://repogempa.bmkg.go.id/
  2. Mengolah datanya ke dalam format json

# How to use
  1. Di dalam folder Tugas1 ketik __make__ pada terminal maka proses scraping akan dimulai, file data akan terdapat pada data
  2. jika ingin input manual lingkup daerah gempa bisa dengan menjalankan program src.py pada folder src.py , lalu masukkan input manualnya

# JSON Structure
  Terdiri dari kumpulan __key__ yang berupa nomor data yang unik dan __value__ yang berisi juga key dan value untuk: 
  1. Date         => value tanggal kejadian
  2. Time         => value waktu kejadian
  3. Latitude     => Latitude
  4. Longitude    => Longitude
  5. Depth        => kedalaman
  6. Mag          => Magnitudo, Kekuatan gempa dalam skala richter.
  7. TypeMag      => Tipe magnitudo atau jenis jenis magnitudo gempa.
  8. smaj         => Jarak stasiun terjauh dari episenter.
  9. smin         => Jarak stasiun terdekat dari episenter.
  10. az          => Azimuthal gap, adalah sudut gap antara stasiun stasiun pencatat gempa terhadap epicenter.
  11. rms         => Root Mean Square atau kuadrat rata rata, adalah nilai error perhitungan.
  12. cPhase      => Count Phase, adalah jumlah fase waktu tiba gelombang gempa yang digunakan.
  13. Region      => Wilayah

  ##Contoh JSON structnya
  ```
  {
    "1": {
        "Date": "2017-05-15",
        "Time": "00:35:50.1",
        "Latitude": "-8.13",
        "Longitude": "115.35",
        "Depth": "10",
        "Mag": "2.4",
        "TypeMag": "MLv",
        "smaj": "1.64",
        "smin": "0.14",
        "az": "184",
        "rms": "0.476",
        "cPhase": "8",
        "Region": "Bali Region, Indonesia   "
    },
    "2": {
        "Date": "2017-05-15",
        "Time": "00:56:37.3",
        "Latitude": "0.41",
        "Longitude": "125.88",
        "Depth": "10",
        "Mag": "3.3",
        "TypeMag": "MLv",
        "smaj": "3.82",
        "smin": "1.3",
        "az": "170",
        "rms": "0.687",
        "cPhase": "8",
        "Region": "Northern Molucca Sea   "
    }
  }
  ```