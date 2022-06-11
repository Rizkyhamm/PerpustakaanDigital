import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="perpustakaan",
  auth_plugin='mysql_native_password'
)

def search_judul(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM Buku WHERE Judul LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount <= 0:
      print("Tidak ada data")
    else:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
        print(df)


def search_penulis(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM Buku WHERE Penulis LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount <= 0:
      print("Tidak ada data")
    else:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
        print(df)




def search_tahun(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM Buku WHERE Tahun_Penerbitan LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount <= 0:
      print("Tidak ada data")
    else:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
        print(df)



def search_ISBN(db):
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM Buku WHERE ISBN LIKE %s"
    val = ("%{}%".format(keyword),)
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount <= 0:
      print("Tidak ada data")
    else:
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
        print(df)

def search_data(db):
  print("=== PENCARIAN DATA BUKU ===")
  print("1. Cari Judul")
  print("2. Cari Penulis Buku")
  print("3. Cari Tahun Penerbitan")
  print("4. Cari ISBN")
  print("0. Kembali")
  print("------------------")
  menu = input("Pilih menu: ")


  if menu == "0":
    show_menu(db)
  if menu == "1":
    search_judul(db)
  elif menu == "2":
    search_penulis(db)
  elif menu == "3":
    search_tahun(db)
  elif menu == "4":
    search_ISBN(db)
  else:
    print("Menu salah!")

def show_data_buku(db):
  cursor = db.cursor()
  sql = "SELECT * FROM Buku"
  cursor.execute(sql)
  results = cursor.fetchall()

  if cursor.rowcount <= 0:
    print("Tidak ada data")
  else:
      pd.set_option("display.max_columns", None)
      pd.set_option("display.max_rows", None)
      pd.set_option("display.width", None)
      df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
      print(df)

def show_data_penulis(db):
  cursor = db.cursor()
  sql = "SELECT * FROM Penulis"
  cursor.execute(sql)
  results = cursor.fetchall()

  if cursor.rowcount <= 0:
    print("Tidak ada data")
  else:
      pd.set_option("display.max_columns", None)
      pd.set_option("display.max_rows", None)
      pd.set_option("display.width", None)
      df = pd.DataFrame(results, columns=['authorid', 'Nama', 'Jenis kelamin', 'Lahir', 'Meninggal', 'Review', 'Jumlah penilai'])
      print(df)

def show_data(db):
  print("=== MENAMPILKAN SEMUA DATA ===")
  print("1. Data Buku")
  print("2. Data Penulis")
  print("0. Kembali")
  print("------------------")
  menu = input("Pilih menu: ")


  if menu == "0":
    show_menu(db)
  if menu == "1":
    show_data_buku(db)
  elif menu == "2":
    show_data_penulis(db)
  else:
    print("Menu salah!")

def review_data_buku(db):
  cursor = db.cursor()
  nomor_isbn = input("Masukan Nomor ISBN Buku: ")
  sql = "SELECT * FROM Buku WHERE ISBN LIKE %s"
  val = ("%{}%".format(nomor_isbn),)
  cursor.execute(sql, val)
  results = cursor.fetchall()

  if cursor.rowcount <= 0:
    print("Tidak ada data")
  else:
      pd.set_option("display.max_columns", None)
      pd.set_option("display.max_rows", None)
      pd.set_option("display.width", None)
      df = pd.DataFrame(results, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
      print(df)
      print("Apakah Buku Tersebut Benar?")
      print("1. Ya")
      print("2. Tidak")
      menu = input("Pilih menu: ")


      if menu == "2":
        review_data_buku(db)

      elif menu == "1":
        nilai = float(input("Masukkan Nilai: "))

        sql = "SELECT Review FROM Buku WHERE ISBN LIKE %s"
        val = ("%{}%".format(nomor_isbn),)
        cursor.execute(sql, val)
        r_temp =str(cursor.fetchall())
        x =r_temp.replace("[(Decimal('","")
        r_temp = float(x.replace("'),)]",""))

        sql = "SELECT Jumlah_Penilai FROM Buku WHERE ISBN LIKE %s"
        val = ("%{}%".format(nomor_isbn),)
        cursor.execute(sql, val)
        jp_temp =str(cursor.fetchall())
        y = jp_temp.replace("[(","")
        jp_temp = float(y.replace(",)]",""))

        jumlah_penilai = int(jp_temp + 1)
        review = ((r_temp * jp_temp) + nilai) / (jumlah_penilai)

        sql = "UPDATE Buku SET Review =%s, Jumlah_Penilai=%s  WHERE ISBN=%s"
        val = (review, jumlah_penilai, nomor_isbn)
        cursor.execute(sql, val)
        db.commit()

        print("{} data berhasil diubah".format(cursor.rowcount))
        sql = "SELECT * FROM Buku WHERE ISBN LIKE %s"
        val = ("%{}%".format(nomor_isbn),)
        cursor.execute(sql, val)
        data = cursor.fetchall()
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(data, columns=['Judul', 'Penulis', 'Review', 'ISBN', 'Jumlah Penilai', 'Tahun Penerbitan'])
        print(df)


def review_data_penulis(db):
  cursor = db.cursor()
  nomor_id = input("Masukan ID Penulis: ")
  sql = "SELECT * FROM Penulis WHERE authorid LIKE %s"
  val = ("%{}%".format(nomor_id),)
  cursor.execute(sql, val)
  results = cursor.fetchall()

  if cursor.rowcount <= 0:
    print("Tidak ada data")
  else:
      pd.set_option("display.max_columns", None)
      pd.set_option("display.max_rows", None)
      pd.set_option("display.width", None)
      df = pd.DataFrame(results,columns=['authorid', 'Nama', 'Jenis kelamin', 'Lahir', 'Meninggal', 'Review', 'Jumlah penilai'])
      print(df)
      print("Apakah Penulis Tersebut Benar?")
      print("1. Ya")
      print("2. Tidak")
      menu = input("Pilih menu: ")


      if menu == "2":
        review_data_penulis(db)

      elif menu == "1":
        nilai = float(input("Masukkan Nilai: "))

        sql = "SELECT Review FROM Penulis WHERE authorid LIKE %s"
        val = ("%{}%".format(nomor_id),)
        cursor.execute(sql, val)
        r_temp =str(cursor.fetchall())
        x =r_temp.replace("[(Decimal('","")
        r_temp = float(x.replace("'),)]",""))

        sql = "SELECT Jumlah_Penilai FROM Penulis WHERE authorid LIKE %s"
        val = ("%{}%".format(nomor_id),)
        cursor.execute(sql, val)
        jp_temp =str(cursor.fetchall())
        y = jp_temp.replace("[(","")
        jp_temp = float(y.replace(",)]",""))

        jumlah_penilai = int(jp_temp + 1)
        review = ((r_temp * jp_temp) + nilai) / (jumlah_penilai)

        sql = "UPDATE Penulis SET Review =%s, Jumlah_Penilai=%s  WHERE authorid=%s"
        val = (review, jumlah_penilai, nomor_id)
        cursor.execute(sql, val)
        db.commit()

        print("{} data berhasil diubah".format(cursor.rowcount))
        sql = "SELECT * FROM Penulis WHERE authorid LIKE %s"
        val = ("%{}%".format(nomor_id),)
        cursor.execute(sql, val)
        data = cursor.fetchall()
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        pd.set_option("display.width", None)
        df = pd.DataFrame(data, columns=['authorid', 'Nama', 'Jenis kelamin', 'Lahir', 'Meninggal', 'Review', 'Jumlah penilai'])
        print(df)

def review_data(db):
  print("=== MEREVIEW BUKU/PENULIS ===")
  print("1. Review Buku")
  print("2. Review Penulis")
  print("0. Kembali")
  print("------------------")
  menu = input("Pilih menu: ")


  if menu == "0":
    show_menu(db)
  if menu == "1":
    review_data_buku(db)
  elif menu == "2":
    review_data_penulis(db)
  else:
    print("Menu salah!")

def show_menu(db):
  print("=== APLIKASI PERPUSTAKAAN DIGITAL ===")
  print("1. Tampilkan Semua Data")
  print("2. Cari Data")
  print("3. Review")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu: ")



  if menu == "1":
    show_data(db)
  elif menu == "2":
    search_data(db)
  elif menu == "3":
    review_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(mydb)
