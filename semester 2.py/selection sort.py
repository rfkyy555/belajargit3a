my_array = [8, 3, 10, 12, 7, 0, 9]

n = len(my_array)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    min_value = my_array.pop(min_index)
    my_array.insert(i, min_value)

print("Sorted array (ascending):", my_array)

# urutan terbalik (descending)
reversed_array = my_array[::-1]
print("Sorted array (descending):", reversed_array)
