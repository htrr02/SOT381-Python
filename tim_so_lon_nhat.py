num1 = int(input("Nhập vào số a:"))
num2 = int(input("Nhập vào số b:"))
num3 = int(input("Nhập vào số c:"))

if (num1 > num2) and (num1 > num3) :
    print(num1, " Là số lớn nhất")
elif (num2 > num3) and (num2 > num1) :
    print(num2, "Là số lớn nhất")
else :
    print(num3, "Là số lớn nhất")