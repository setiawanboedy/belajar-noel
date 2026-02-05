# Belajar 7 - List dan Perulangan Lanjutan di Python
# Fungsi dalam list seperti append, insert, remove, pop, clear, index, count, 
# sort, reverse, copy

# Contoh penggunaan append
buah_buahan = ['apel', 'mangga', 'anggur']
print("List awal:", buah_buahan)

print("====================Append======================")

# Menambahkan elemen baru ke dalam list
buah_buahan.append('kiwi')
print("Setelah append kiwi:", buah_buahan)

print("====================Insert======================")
# Menyisipkan elemen pada indeks tertentu
buah_buahan.insert(1, 'pisang')
print("Setelah insert pisang pada indeks 1:", buah_buahan)

print("====================Remove======================")
# Menghapus elemen tertentu dari list
buah_buahan.remove('pisang')
print("Setelah remove pisang:", buah_buahan)

print("====================Pop======================")
# Menghapus elemen terakhir dari list
# buah_buahan = ['apel', 'mangga', 'anggur', 'kiwi']
buah_buahan.pop()
print("Setelah pop:", buah_buahan)

print("====================Index======================")
# Mencari indeks dari elemen tertentu
index_mangga = buah_buahan.index('mangga')
print("Indeks mangga:", index_mangga)

print("====================Count======================")
# Menghitung jumlah kemunculan elemen tertentu
# buah_buahan = ['apel', 'mangga', 'anggur', 'kiwi', 'apel']
buah_buahan.append('apel')
jumlah_buah_apel = buah_buahan.count('apel')
print("Jumlah buah apel dalam list:", jumlah_buah_apel)

jumlah_semua_buah = len(buah_buahan)
print("Jumlah buah dalam list:", jumlah_semua_buah)

print("====================Clear======================")
# Menghapus semua elemen dari list
buah_buahan.clear()
print("Setelah clear:", buah_buahan)

# Latihan Logic kasir sederhana
print("====================Latihan Kasir======================")
katalog_buah = {'apel': 5000, 'mangga': 7000, 'anggur': 6000, 'kiwi': 8000}
keranjang_belanja = []
total_harga_belanja = 0

while True:
    nama_buah = input("Masukkan nama buah yang dibeli (atau ketik selesai dan keluar): ")
    if nama_buah == 'selesai':
        break
    elif nama_buah in katalog_buah:
        keranjang_belanja.append(nama_buah)
        total_harga_belanja += katalog_buah[nama_buah]
        print(f"Buah {nama_buah} ditambahkan ke keranjang, dengan harga: {katalog_buah[nama_buah]}")
    else:
        print("Maaf buah tidak tersedia atau salah perintah")

print("Keranjang belanja buah: ", keranjang_belanja)
print("Total belanja buah adalah: ", total_harga_belanja)            
print("Terimakasih sudah belanja!")