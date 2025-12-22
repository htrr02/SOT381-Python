a = float(input("Nhập số a :"))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c :"))

max = a
if b > max :
    max = b
if c > max :
    max = c

min = a
if b < min :
    min = b
if c < min :
    min = c

print(f"Max: {max}, Min: {min}")
