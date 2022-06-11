# Kelompok 8
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
3. Buka aplikasi *database* yang kalian miliki, lalu *import* file [DatabasePerpustakaan.sql](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/PerpustakaanDigital.sql) dan [TabelPenulis.sql](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/TabelPenulis.sql) ini atau *copy* kode di bawah ini untuk membuat *database* dan *table* nya. Bila Anda menggunakan XAMPP, anda hanya perlu menyalin kode di atas pada baris pertama.
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
```sql
CREATE TABLE Penulis(
   authorid       INTEGER  NOT NULL PRIMARY KEY 
  ,Nama           VARCHAR(117) NOT NULL
  ,Jenis_kelamin  VARCHAR(7) NOT NULL
  ,Lahir          VARCHAR(10)
  ,Meninggal      VARCHAR(10)
  ,Review         NUMERIC(4,2) NOT NULL
  ,Jumlah_penilai INTEGER  NOT NULL
);
```
4. *Import* file [Perpustakaan_Dataset.csv](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/Perpustakaan_Dataset.csv) dan [Penulis_Dataset.csv](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/Penulis_Dataset.csv) di dalam *database*.
6. Download file [PerpustakaanDigital.py](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/PerpustakaanDigital.py) ini.
7. Kami sarankan agar program ini dijalankan dengan dengan PyCharm seperti yang kita lakukan.
8. Program dapat digunakan.
## Demo
**Tampilan awal aplikasi.**

![Awal](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/0.jpeg)

**Menampilkan data perpustakaan.**
![1.1](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/1.1.jfif)

**Menampilkan data penulis.**
![1.2](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/1.2.jfif)

**Mencari buku berdasarkan nama buku.**
![2.1](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/2.1.jfif)

**Mencari buku berdasarkan nama penulis buku.**
![2.2](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/2.2.jfif)

**Mencari buku berdasrkan tahun penerbitan.**
![2.3](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/2.3.jfif)

**Mencari buku berdasarkan ISBN.**
![2.4](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/2.4.jfif)

**Mengulas buku.**
![3.1](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/3.1.jfif)

**Mengulas penulis.**
![3.2](https://github.com/Rizkyhamm/PerpustakaanDigital/blob/main/3.2.jfif)

Video [demo](https://drive.google.com/file/d/1vnv9p7pgMkpBjjyP6bYFI6h0IV_T-3vS/view?usp=sharing).

## Referensi
1. [Dataset Buku](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
2. [Dataset Penulis](https://www.kaggle.com/datasets/choobani/goodread-authors)
3. [Pandas](https://www.codegrepper.com/code-examples/python/pandas+set+max+columns)
4. [Pandas](https://www.youtube.com/watch?v=m1jHkL0qZsI)
5. [MySQL](https://www.youtube.com/watch?v=7S_tz1z_5bA&t=2610s)
6. [Python MySQL](https://www.youtube.com/watch?v=3vsC05rxZ8c&t=4s)
7. [Playlist Python MySQL](https://youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G)
