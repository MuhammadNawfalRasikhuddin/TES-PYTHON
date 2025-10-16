# Input Data Membuat Program Diskon
nama = "Evans"
Total_Belanja = 750000
Diskon_Yang_Di_Dapat = 0

# jika total belanja elbih dari 500.000, mendapat diskon 10%
if Total_Belanja > 500000:
    Diskon_Yang_Di_Dapat = 0.10 #10%
    Total_Setelah_Diskon = Total_Belanja - (Total_Belanja*Diskon_Yang_Di_Dapat)

#Tampilkan Hasil Belanja Evans Setelah Mendapat Diskon
print("Total Belanja Evans Yaitu Rp", int(Total_Setelah_Diskon))
