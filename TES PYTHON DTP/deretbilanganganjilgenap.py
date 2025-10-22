baris_awal = int(input("masukkan bilangan awal : "))
baris_akhir = int(input("masukkan bilangan akhir : "))

for i in range (baris_awal, baris_akhir+1):
     if i % 2 == 0 :
         print (i, "ini adalah bilangan genap")
     else:
         print (i, "ini adalah bilangan ganjil")