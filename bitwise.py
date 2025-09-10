# Mendefinisikan dua bilangan bulat
a = 60  # dalam biner: 0011 1100
b = 13  # dalam biner: 0000 1101

# Menggunakan operator bitwise
bitwise_and = a & b    # Bitwise AND
bitwise_or = a | b     # Bitwise OR
bitwise_not = ~a       # Bitwise NOT
bitwise_xor = a ^ b    # Bitwise XOR
shift_left = a << 2    # Shift left
shift_right = a >> 2   # Shift right

# Menampilkan hasil
print(f"a: {a} (biner: {bin(a)})")
print(f"b: {b} (biner: {bin(b)})")
print(f"Bitwise AND: {bitwise_and} (biner: {bin(bitwise_and)})")
print(f"Bitwise OR: {bitwise_or} (biner: {bin(bitwise_or)})")
print(f"Bitwise NOT: {bitwise_not} (biner: {bin(bitwise_not)})")
print(f"Bitwise XOR: {bitwise_xor} (biner: {bin(bitwise_xor)})")
print(f"Shift Left: {shift_left} (biner: {bin(shift_left)})")
print(f"Shift Right: {shift_right} (biner: {bin(shift_right)})")
