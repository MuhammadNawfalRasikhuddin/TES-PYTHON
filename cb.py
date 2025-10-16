# 02_Doni_XI
# Program menghitung tabungan Doni sampai target tercapai

target = 300000      # Target harga sepatu
tabungan_per_minggu = 50000  # Uang yang ditabung per minggu
tabungan = 0
minggu = 0

while tabungan < target:
    minggu += 1
    tabungan += tabungan_per_minggu
    print(f"Minggu ke-{minggu}: Tabungan = Rp{tabungan}")

print(f"Target tercapai dalam {minggu} minggu dengan total tabungan Rp{tabungan}.")
