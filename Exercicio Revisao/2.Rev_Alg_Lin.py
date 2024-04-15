# calcule i^15
x = 0
for x in range(7):
    a = 1j**x
    print(a)

print("A cada 4 elementos ela repete")
n = int(input("Digite a pontencia: "))
x = 1j ** (n % 4)
print(x)
