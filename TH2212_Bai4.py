a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
c = float(input("Nhập số c:"))

def soLNNN(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    min = b
    if b < min:
        min = b
    if c < min:
        min = c

    return max, min

numMax, numMin = soLNNN(a,b,c)
print(f"Số lớn nhất là:{numMax}")
print(f"Số nhỏ nhất là:{numMin}")

