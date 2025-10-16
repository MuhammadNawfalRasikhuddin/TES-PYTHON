#Nama   : Muhammad Nawfal Rasikhuddin
#Kelas  : XI TJAT 2
#Absen  : 20

import numpy as np

def biaya_fotokopi(jumlah_fotokopi):
    return jumlah_fotokopi * 300

def biaya_print(jumlah_print):
    return jumlah_print * 1000

def hitung_kembalian(uang_dibayar, total_harga):
    return uang_dibayar - total_harga

jumlah_fotokopi = int(input("Jumlah fotokopi: "))
jumlah_print = int(input("Jumlah print: "))
uang_dibayar = int(input("Uang yang dibayarkan: "))

biaya_fc = biaya_fotokopi(jumlah_fotokopi)
biaya_pr = biaya_print(jumlah_print)

total_harga = np.sum([biaya_fc, biaya_pr])

kembalian = hitung_kembalian(uang_dibayar, total_harga)

print("\nRincian Biaya :")
print(f"Biaya Fotokopi : Rp {biaya_fc}")
print(f"Biaya Print : Rp {biaya_pr}")
print(f"Total Harga : Rp {total_harga}")
print(f"Kembalian : Rp {kembalian}")
