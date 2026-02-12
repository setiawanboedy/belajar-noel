# Belajar class dalam bahasa python
# Class adalah blueprint untuk membuat objek yang menggabungkan data dan fungsi.
# Dengan class, kita dapat membuat struktur data yang kompleks dan mengorganisir kode dengan lebih baik.

class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def deskripsi(self):
        return f"{self.merk} berwarna {self.warna} tahun {self.tahun}"

mobil_saya = Mobil("Toyota", "Merah", 2020)
print(mobil_saya.deskripsi())

print("====================Class dengan Inheritance======================")
# Inheritance (Pewarisan) adalah konsep di mana sebuah class dapat mewarisi atribut dan metode dari class lain.
class Kendaraan:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def deskripsi(self):
        return f"{self.merk} berwarna {self.warna}"
    
class Motor(Kendaraan):
    def __init__(self, merk, warna, tipe):
        super().__init__(merk, warna)
        self.tipe = tipe

    def deskripsi_motor(self):
        return f"{self.merk} berwarna {self.warna} tipe {self.tipe}"

motor_saya = Motor("Honda", "Hitam", "Sport")
print(motor_saya.deskripsi_motor())


