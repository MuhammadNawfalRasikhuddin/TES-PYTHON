Nama = (input("Masukan Nama Anda : "))
Gaji = int(input("Masukan Gaji Anda (Rp): "))
Bonus = 0

if Gaji > 5000000:
    Bonus = 0.10 
    Total_Setelah_Bonus = Gaji + (Gaji*Bonus)

elif Gaji < 5000000:
    Bonus = 0.05 
    Total_Setelah_Bonus = Gaji + (Gaji*Bonus)

print ("Total gaji yang di dapat setelah mendapat bonus yaitu Rp ", Total_Setelah_Bonus)