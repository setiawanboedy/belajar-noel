#===============================Pengenalan Python=======================================

# print nama
# print("Noel")

# contoh print
# print("Budi")

#type string
nama = "Noel" #variable
print(nama)

print("=======================================================")

#type angka/number4
umur = 13
print(umur)

jumlah = umur + 2
print(jumlah)

print("=======================================================")

#type list/array/collection
belanjaan = ["sabun","sampo","sikat gigi","sayur"]
print(belanjaan)

#index
sabun = belanjaan[0]
print(sabun)

sikat_gigi = belanjaan[3]
print(sikat_gigi)

print("=========================================================")
#Type Boolean
benar = True
salah = False

tinggi_budi = 170
tinggi_noel = 160

is_tinggi_sama = tinggi_budi == tinggi_noel
is_tinggi_lebih = tinggi_budi > tinggi_noel
is_tinggi_kurang = tinggi_budi < tinggi_noel
print(is_tinggi_sama)
print(is_tinggi_lebih)
print(is_tinggi_kurang)

print("=========================================================")

is_tinggi_tidak = tinggi_budi != tinggi_noel
is_tinggi_lebih_sama = tinggi_budi >= tinggi_noel
is_tinggi_kurang_sama = tinggi_budi <= tinggi_noel
print(is_tinggi_tidak)
print(is_tinggi_lebih_sama)
print(is_tinggi_kurang_sama)

print(f"Apakah tinggi budi tidak sama dengan tinggi noel: {is_tinggi_tidak}")
print(f"Apakah tinggi budi tidak sama dengan tinggi noel: {is_tinggi_tidak} dan tinggi budi lebih dari tinggi noel: {is_tinggi_lebih}")
print("Apakah tinggi budi kurang dari atau sama dengan tinggi noel: {is_tinggi_kurang_sama}")
print("Apakah tinggi budi lebih dari atau sama dengan tinggi noel: ", is_tinggi_lebih_sama)