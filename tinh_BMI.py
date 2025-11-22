can = float(input("Nhập cân nặng (kg):"))
cao = float(input("Nhập chiều cao(m):"))

bmi = can / (cao * cao)

if bmi < 18.5:
    loai = "Gầy"
elif 18.5 <= bmi <= 24.9:
    loai = "Bình thường"
else :
    loai = "Thừa cân"


print( " BMI của bạn là : ", bmi )
print( " Phân loại: ", loai)


