import math
print("Nhap vao a: ")
a=float(input())
print("Nhap vao b: ")
b=float(input())
print("Nhap vao c: ")
c=float(input())
delta = float(math.pow(b,2)-4*a*c)

if(a == 0):
    print("A phai khac 0")
else:
    if(delta < 0):
        print("Phuong trinh vo nghiem")
        print(delta)
    elif(delta == 0):
        x1 = x2 = float(-b/2*a)
        print("Phuong trinh co nghiem kep")
        print(x1)
        print(x2)
    else:
        x1 = -b + math.sqrt(delta)/2*a
        x2 = -b - math.sqrt(delta)/2*a
        print("Phuong trinh co 2 nghiem phan biet")
        print(x1)
        print(x2)
