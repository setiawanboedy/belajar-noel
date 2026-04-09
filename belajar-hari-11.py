# Perhitungan BMI (Body Mass Index)
def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi
berat_badan = 70  # dalam kilogram
tinggi_badan = 175 # dalam centimeter
tinggi_badan = tinggi_badan / 100  # konversi ke meter
bmi = hitung_bmi(berat_badan, tinggi_badan)
print(f"BMI Anda adalah: {bmi:.2f}")

if bmi < 18.5:
    print("Kategori: Berat badan kurang")
elif 18.5 <= bmi < 24.9:
    print("Kategori: Berat badan normal")
elif 25 <= bmi < 29.9:
    print("Kategori: Berat badan berlebih")
else:
    print("Kategori: Obesitas")