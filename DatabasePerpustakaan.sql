CREATE DATABASE Perpustakaan;
CREATE TABLE Buku(
   Judul              VARCHAR(1000)
  ,Penulis            VARCHAR(1000)
  ,Review             NUMERIC(4,2)
  ,ISBN               DOUBLE  PRIMARY KEY 
  ,Jumlah_Penilai     INTEGER (10) 
  ,Tahun_Penerbitan   DATE 
);