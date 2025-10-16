class Hewan:
    def __init__(self, nama, suara):
        self.nama = nama
        self.suara = suara
      
    def tampilkan_suara(self):
        print(f"{self.nama}  bersuara: {self.suara}")
    
    
class Gajah(Hewan):
    def __init__(self, nama):
        super().__init__(nama,"Trumpett")
        
    
class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama, 'meoww')

print('kegiatan b')
g= Gajah('Gajah')
K= Kucing('Kucing')

g.tampilkan_suara()
K.tampilkan_suara()
