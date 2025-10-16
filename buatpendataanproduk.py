# Membuat kelas Produk
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    # Method untuk menampilkan info produk
    def info(self):
        print(f"Nama Produk : {self.nama}")
        print(f"Harga       : Rp{self.harga:,.2f}")
        print(f"Stok        : {self.stok}")

# Membuat objek produk Buku Python
buku = Produk("Buku Python", 50000.00, 10)

# Menampilkan informasi produk
buku.info()
