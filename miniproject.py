# 20_MuhammadNawfalRasikhuddin_XITJAT2_MiniProject.py

# Program untuk memeriksa suhu tubuh seseorang
# dan memberikan keterangan kondisi tubuh

# Meminta input jumlah orang
jumlah_orang = int(input("Masukkan jumlah orang yang akan dicek: "))

# Perulangan untuk setiap orang
for i in range(jumlah_orang):
    print(f"\nData orang ke-{i+1}")
    nama = input("Masukkan nama: ")
    suhu = float(input("Masukkan suhu tubuh (°C): "))

    # Percabangan untuk menentukan kategori
    if suhu < 36:
        kategori = "Suhu Rendah"
    elif 36 <= suhu <= 37.5:
        kategori = "Normal"
    else:
        kategori = "Demam"

    # Output hasil
    print(f"{nama} memiliki suhu tubuh {suhu}°C, kategori: {kategori}")
