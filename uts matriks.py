#Kasus manajemen data nilai (Array dan Matriks)
mahasiswa = ["M1", "M2", "M3", "M4"]
mata_kuliah = ["Algoritma", "Basis Data", "Struktur Data"]

nilai_mahasiswa = [
    [80, 75, 90],  # Mahasiswa 1
    [70, 85, 78],  # Mahasiswa 2
    [88, 90, 92],  # Mahasiswa 3
    [60, 65, 70]   # Mahasiswa 4
]

nilai_tertinggi = 0
mahasiswa_tertinggi = ""

for i in range(len(mahasiswa)):
    rata = sum(nilai_mahasiswa[i]) / len(nilai_mahasiswa[i])
    print(f"Rata-rata {mahasiswa[i]}: {rata:.1f}")

    if rata > nilai_tertinggi:
        nilai_tertinggi = rata
        mahasiswa_tertinggi = mahasiswa[i]

#output
print(f"Mahasiswa dengan rata-rata tertinggi: {mahasiswa_tertinggi}")
print(f"dengan nilai rata-rata : {nilai_tertinggi:.1f}")