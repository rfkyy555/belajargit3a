#bilangan array
arr = [9, 11, 12, 24, 5, 77, 109, 88, 60, 43, 31, 55]

#menjumlahkan bilangan ganjil dan genap
total_genap = sum(num for num in arr if num % 2 == 0)
total_ganjil = sum(num for num in arr if num % 2 != 0)

#Array terbalik
arr_terbalik = arr[::-1]

#output
print(f"Total genap = {total_genap}")
print(f"Total ganjil = {total_ganjil}")
print("Array terbalik:", ", ".join(map(str, arr_terbalik)))