my_array = [8, 3, 10, 12, 7, 0, 9]

# bubble sort (ascending)
n = len(my_array)
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

print("Sorted array (ascending):", my_array)

#versi terbalik (descending)
reversed_array = my_array[::-1]
print("Sorted array (descending):", reversed_array) 
