x = 10
y = 5
#operator logika and
print(x < 12 and y > 3)
print(x > 12 and y < 3)
print(x < 12 and y < 3)
print("---------------------------------------------------------------------------------------------------------------")

#operator logika or
print(x < 4 or y > 50)
print(x > 4 or y < 50)
print(x < 4 or y < 50)
print("---------------------------------------------------------------------------------------------------------------")

#operator logika not
print(not x < 15)
print(not y < 2 )
print("---------------------------------------------------------------------------------------------------------------")

#XOR
print('==== XOR ====')
a = False
b = False
c = a ^ b
print(a, 'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a, 'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a, 'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)