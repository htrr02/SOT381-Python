n = (int(input("Nhập số n:")))
def giatriS(n):
    tu_so = 0
    mau_so = 0

    for i in range (1, n + 1):
        tu_so += i

    for i in range (1, n + 1):
        mau_so += i*2

    if mau_so == 0 :
        return 0

    return tu_so / mau_so
kq = giatriS(n)
print(f"Giá trị của S là : {kq}")