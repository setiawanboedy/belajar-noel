# Belajar tentang fungsi dalam bahasa pytnon
# Fungsi adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu.

def sapa():
    print("Halo! Selamat datang di program kami.")

def nama():
    print("Nama saya adalah Noel.")    

nama()

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang di program kami.")


sapa_nama("Noel")
sapa_nama("Budi")

print("====================Fungsi dengan Parameter======================")

# Fungsi dengan nilai kembalian (return)
buah_buahan = ['apel', 'mangga', 'anggur', 'kiwi']
def total_buah(buah_list):
    total = 0
    for buah in buah_list:
        total += 1
    return total

jumlah_buah = total_buah(buah_buahan)
print("Jumlah buah dalam list:", jumlah_buah)

belanjaan = ['sayur', 'daging', 'ikan']
jumlah_belanjaan = total_buah(belanjaan)
print("Jumlah belanjaan dalam list:", jumlah_belanjaan)

print("====================Fungsi dengan Nilai Default======================")

# Fungsi dengan nilai default
def sapa_pengguna(nama="Rendi"):
    print(f"Halo, {nama}! Selamat datang di program kami.")

sapa_pengguna()
sapa_pengguna("Noel")

print("====================Latihan List dan Fungsi======================")
# Latihan penggunaan list dan fungsi
def tambah_buah(buah_list, buah_baru):
    buah_list.append(buah_baru)
    return buah_list

daftar_buah = ['apel', 'mangga', 'anggur']

print("Daftar buah awal:", daftar_buah)

daftar_buah = tambah_buah(daftar_buah, 'kiwi')
print("Setelah menambahkan kiwi:", daftar_buah)
daftar_buah = tambah_buah(daftar_buah, 'pisang')
print("Setelah menambahkan pisang:", daftar_buah)

print("====================Latihan Fungsi Perhitungan======================")
# Latihan fungsi untuk perhitungan sederhana
def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

sisi_persegi = 4
luas_persegi = hitung_luas_persegi(sisi_persegi)
print(f"Luas persegi dengan sisi {sisi_persegi} adalah: {luas_persegi}")

alas_segitiga = 5
tinggi_segitiga = 10
luas_segitiga = hitung_luas_segitiga(alas_segitiga, tinggi_segitiga)
print(f"Luas segitiga dengan alas {alas_segitiga} dan tinggi {tinggi_segitiga} adalah: {luas_segitiga}")


