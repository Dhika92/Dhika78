class Handphone:
    def __init__(self, ram, kamera, harga):
        self.__ram = ram  
        self.__kamera = kamera  
        self.harga = harga

    # Getter untuk RAM
    def get_ram(self):
        return self.__ram

    # Setter untuk RAM
    def set_ram(self, ram):
        self.__ram = ram

    # Getter untuk Kamera
    def get_kamera(self):
        return self.__kamera

    # Setter untuk Kamera
    def set_kamera(self, kamera):
        self.__kamera = kamera

    def mengirim_pesan(self, nomor, pesan):
        print(f"Mengirim pesan ke {nomor}: {pesan}")

    def menelfon(self, nomor):
        print(f"Menelfon {nomor}...")

    def memotret(self):
        print(f"Memotret dengan kamera {self.__kamera} MP...")

# Membuat objek baru
hp3 = Handphone("16GB", 200, 12000000)

# Mengakses variabel private menggunakan getter
print(f"HP3: RAM {hp3.get_ram()}, Kamera {hp3.get_kamera()}MP, Harga Rp{hp3.harga}")

# Mengubah nilai variabel private menggunakan setter
hp3.set_ram("32GB")
hp3.set_kamera(300)

# Menampilkan nilai setelah diubah
print(f"HP3 (Setelah diubah): RAM {hp3.get_ram()}, Kamera {hp3.get_kamera()}MP, Harga Rp{hp3.harga}")
