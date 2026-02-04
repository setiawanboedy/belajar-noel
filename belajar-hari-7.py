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