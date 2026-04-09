# buat kalkulator kalori dengan oop
class KalkulatorKalori:
    def __init__(self):
        self.total_kalori = 0

    def tambah_kalori(self, kalori):
        self.total_kalori += kalori

    def tampilkan_total_kalori(self):
        print(f"Total kalori yang dikonsumsi: {self.total_kalori} kalori")

# Gunakan input user
kalkulator = KalkulatorKalori()
while True:
    makanan = input("Masukkan nama makanan (atau ketik 'selesai' untuk berhenti): ")
    if makanan.lower() == 'selesai':
        break
    kalori = int(input(f"Masukkan jumlah kalori untuk {makanan}: "))
    kalkulator.tambah_kalori(kalori)
kalkulator.tampilkan_total_kalori()

