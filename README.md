# Anggota Tim
- Alimudinsyah Alrasyid
- Ilpi Yuditya Mulyana
- Rizky Hamdani Sakti
# PerpustakaanDigital
## *Problem*
Problem yang kami ambil yaitu dikarenakan perpustakaan kami semasa SMA tidak memiliki aplikasi *CRUD* yang membuat kami selaku pengunjung perpustakaan kesulitan untuk mencari buku yang kami mau.
## Solusi
Kami memberikan solusi dengan cara membuat sebuah aplikasi *CRUD* yang dapat melihat apa saja koleksi yang perpustakaan miliki dan melakukan ulasan terhadap suatu buku. Pengguna dapat mencari data semua buku ataupun dengan kata kunci seperti nama buku, nama penulis, tahun penerbitan dan juga nomor ISBN.
## Panduan menggunakan Aplikasi
1. Pastikan telah terpasang aplikasi MySQL Workbench atau XAMPP sebagai aplikasi *database*.
2. Pasang aplikasi Anaconda sebagai *environmet* yang akan digunakan dalam program Python.
3. Buka aplikasi *database* yang kalian miliki, lalu *import* file [.sql](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/PerpustakaanDigital.sql) ini atau *copy* kode di bawah ini untuk membuat *database* dan *table* nya. Bila Anda menggunakan XAMPP, anda hanya perlu menyalin kode di atas pada baris pertama.
```sql
CREATE DATABASE Perpustakaan;
CREATE TABLE Buku(
   Judul              VARCHAR(1000)
  ,Penulis            VARCHAR(1000)
  ,Review             NUMERIC(4,2)
  ,ISBN               DOUBLE  PRIMARY KEY 
  ,Jumlah_Penilai     INTEGER (10) 
  ,Tahun_Penerbitan   DATE 
);
```
4. *Import* file [DatasetPerpustakaanDigital.csv](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/DatasetPerpustakaanDigital.csv) dan [.csv](apa.com) di dalam *database*.
6. Download file [PerpustakaanDigital.py](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/PerpustakaanDigital.py) ini.
7. Kami sarankan agar program ini dijalankan dengan dengan PyCharm seperti yang kita lakukan.
8. Program dapat digunakan.
## Demo

## Referensi
1. [Dataset](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
2. [Pandas](https://www.codegrepper.com/code-examples/python/pandas+set+max+columns)
3. [Pandas](https://www.youtube.com/watch?v=m1jHkL0qZsI)
4. [MySQL](https://www.youtube.com/watch?v=7S_tz1z_5bA&t=2610s)
5. [Python MySQL](https://www.youtube.com/watch?v=3vsC05rxZ8c&t=4s)
6. [Playlist Python MySQL](https://youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G)
