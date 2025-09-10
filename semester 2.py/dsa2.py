#Nilai matriks
matrix = [
    [8, 6, 4],
    [12, 10, 8],
    [16, 14, 12]
]

#Mencari nilai maksimal dan minimal dalam matriks
nilai_maksimal = max(max(row) for row in matrix)
nilai_minimal = min(min(row) for row in matrix)

#Output
print(f"Nilai maksimal = {nilai_maksimal}")
print(f"Nilai minimal = {nilai_minimal}")
