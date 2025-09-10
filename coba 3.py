# menghitung luas lingkaran 

import math

def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# Input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))
luas = luas_lingkaran(jari_jari)

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:.2f}")
