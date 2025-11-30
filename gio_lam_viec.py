time = int(input("Nhập giờ trong ngày (0-23):"))
if time < 9 or time > 17 :
    print("Ngoài giờ làm việc")
else:
    print("Trong giờ làm việc")