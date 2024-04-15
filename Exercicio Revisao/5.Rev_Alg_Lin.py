c1 = complex(input("c1: "))
c2 = complex(input("c2: "))
c3 = complex(input("c3: "))

s1 = c1 + c2
s2 = c2 + c1
p1 = c1 * c2
p2 = c2 * c1

print("comutatividade: c1+c2=", s1, " e c2+c1=", s2)
print("comutatividade: c1xc2=", p1, " e c2xc1=", p2)

s3 = (c1 + c2) + c3
s4 = c1 + (c2 + c3)
p3 = (c1 * c2) * c3
p4 = c1 * (c2 * c3)
print("comutatividade: (c1+c2)+c3=", s3, " e c1+(c2+c3)=", s4)
print("comutatividade: (c1*c2)*c3=", p3, " e c1*(c2*c3)=", p4)

d1 = c1 * (c2 + c3)
d2 = (c1 * c2) + (c1 * c3)
print("distributividade: c1*(c2+c3)=", d1, " e (c1*c2)+(c1*c3)=", d2)
