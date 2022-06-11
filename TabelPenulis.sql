CREATE TABLE Penulis(
   authorid       INTEGER  NOT NULL PRIMARY KEY 
  ,Nama           VARCHAR(117) NOT NULL
  ,Jenis_kelamin  VARCHAR(7) NOT NULL
  ,Lahir          VARCHAR(10)
  ,Meninggal      VARCHAR(10)
  ,Review         NUMERIC(4,2) NOT NULL
  ,Jumlah_penilai INTEGER  NOT NULL
);