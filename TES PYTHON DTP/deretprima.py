# Meminta input dari pengguna
angkaAwal = int(input("Masukkan Angka Awal : "))
angkaAkhir = int(input("Masukkan Angka Akhir : "))

# Perulangan dari angka awal sampai angka akhir
for i in range(angkaAwal, angkaAkhir + 1):
    # Bilangan prima selalu lebih besar dari 1
    if i > 1:
        # Cek apakah i punya faktor selain 1 dan dirinya sendiri
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                print(f"{i} adalah bukan bilangan prima")
                break
        else:
            print(f"{i} adalah bilangan prima")
    else:
        print(f"{i} adalah bukan bilangan prima")