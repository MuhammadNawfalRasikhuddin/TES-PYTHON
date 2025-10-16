#Perulangan dan kondisi dari doni
tabungan_Doni = 0
uang_doni_perminggu = 50000

minggu_doni = 0
target_tabungan = 300000

while tabungan_Doni < target_tabungan:
    minggu_doni += 1
    tabungan_Doni += uang_doni_perminggu
    print(f"Minggu ke-{minggu_doni}: Tabungan Doni = Rp{tabungan_Doni}")
print (f"Target tercapai dalam {minggu_doni} minggu dengan total uang Rp{tabungan_Doni}")