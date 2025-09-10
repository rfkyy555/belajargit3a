import pandas as pd

data = {
    "Nama": ["akmal", "kaiii", "farhan kebab", "slamet kopling", "opang"],
    "Umur": [15, 16, 15, 16, 17],
    "Nilai Ujian ": [70, 85, 90, 75, 80],
}

proses = pd.DataFrame(data)

rata_rata = proses["Nilai Ujian "].mean()

siswa_di_atas_rata_rata = proses[proses["Nilai Ujian "] > rata_rata]

print("================Rekap Nilai================")
print("Data Siswa:")
print(proses)

print("==============Rata Rata Nilai==============")
print("Rata-rata Nilai Ujian:", round(rata_rata, 2))

print("=============Siswa Berprestasi=============")
print("Siswa dengan Nilai Ujian di Atas Rata-rata:")
print(siswa_di_atas_rata_rata)
print("===========================================")