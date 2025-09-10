my_array = [22, 59, 94, 16, 8, 49, 56]

n = len(my_array)
for i in range(n - 1):
    for j in range(n - i - 1):  # gunakan 'j' untuk loop dalam
        if my_array[j] > my_array[j + 1]:
            # tukar elemen jika tidak urut
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Array setelah diurutkan:", my_array)
