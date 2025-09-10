#operator bitwise

a = 23
b = 15

#bitwise or (|)
c = a | b 
print('==============================')
print("operasi a | b  = c -> ", c)
print('biner dari c ->', format(c,'0b'))


#bitwise AND
c = a & b 
print('==============================')
print("operasi a & b = c ->", c)
print("biner dari c ->", format(c,"0b"))


#bitwise NOT
c = ~a
print('==============================')
print("operasi a ~ b = c ->", c)
print("biner dari c ->", format(c,"0b"))


#bitwise xOR
c = a ^ b 
print('==============================')
print("operasi a ^ b = c ->", c)
print("biner dari c ->", format(c,"0b"))


#bitwise Right shift
c = a>>2
print('==============================')
print("operasi a >> b = c ->", c)
print("biner dari c ->", format(c,"0b"))


#bitwise Left shift
c = b<<3 
print('==============================')
print("operasi a << b = c ->", c)
print("biner dari c ->", format(c,"0b"))