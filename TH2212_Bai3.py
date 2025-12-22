a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
c = float(input("Nhập số c:"))

def soLN(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c

    return max

numMax = soLN(a,b,c)
print(f"Số lớn nhất là:{numMax}")

