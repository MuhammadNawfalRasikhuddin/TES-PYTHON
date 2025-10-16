angka_Awal = int(input("Masukkan angka awal: "))
angka_Akhir = int(input("Masukkan angka akhir: "))

for i in range(angka_Awal, angka_Akhir + 1):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")
