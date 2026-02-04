# Perulangan dengan For dan While

# Perulangan dengan For
buah_buahan = ['apel', 'pisang', 'jeruk', 'mangga']

# perulangan dengan data
for buah in buah_buahan:
    print(buah)

print("==========================================")

# perulangan dengan index
for index in range(len(buah_buahan)):
    print(f"Buah ke-{index+1} adalah {buah_buahan[index]}")


print("==========================================")


# Perulangan dengan Enumerate
for index, buah in enumerate(buah_buahan):
    print(f"Buah ke-{index+1} adalah {buah}")

print("====================Perulangan dengan while======================")

# Perulangan dengan While
count = 0
while count < len(buah_buahan):
    print(f"Buah ke-{count+1} adalah {buah_buahan[count]}")
    count += 1


print("==========================================")
# Infinite Loop dengan While
# Jangan jalan karena berbahaya, uncommet untuk mencoba

# count = 0
# while True:
#     print(f"Buah ke-{count+1}")
#     count += 

print("====================Break======================")
# Perulangan dengan Break
for buah in buah_buahan:
    if buah == 'mangga':
        print(f"Ditemukan buah {buah}, menghentikan perulangan.")
        break
    print(f"Buah: {buah}")

print("====================Continue======================")

# Melanjutkan perulangan dengan Continue
for buah in buah_buahan:
    if buah == 'jeruk':
        # print(f"Melewati buah {buah}.")
        continue
    print(f"Buah: {buah}")

print("====================While Break======================")

# While dengan Break
index = 0
while index < len(buah_buahan):
    if buah_buahan[index] == 'jeruk':
        print(f"Ditemukan buah {buah_buahan[index]}, menghentikan perulangan.")
        break
    print(f"Buah ke-{index+1} adalah {buah_buahan[index]}")
    index += 1


print("====================Studi Kasus======================")

# Studi Kasus: Mencari angka genap dalam daftar
angka = [1, 3, 4, 6, 7, 8, 3, 6]

for num in angka:
    if num % 2 != 0:
        continue
    print(f"Semua angka genap: {num}")
    
    # cari angka terkecil bilangan genap
    if num == 4:
        print(f"Angka genap terkecil ditemukan di angka {num}, menghentikan perulangan.")
        break

print("==========================================")

# Studi Kasus: Mencari huruf vokal dalam sebuah kata dengan while
kata = "belajar"
index = 0
while index < len(kata):
    if kata[index] in 'aiueo':
        print(f"Huruf vokal ditemukan: {kata[index]}")
    index += 1

