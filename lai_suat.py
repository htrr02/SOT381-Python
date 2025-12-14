von = 100_000_000
lai_suat = 0.07
so_nam = 5

for nam in range(1, so_nam + 1):
    von = von + von * lai_suat
    print(f"Năm {nam}: Số tiền = {int(von):,} VND")
