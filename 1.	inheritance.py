# ============================================================
# (a) INHERITANCE - Pewarisan Sifat
# ============================================================
# Kelas induk (parent class) bernama Petani
# Berisi atribut dan metode yang umum/dasar

class Petani:
    def __init__(self, nama, nik, alamat, luas_lahan):
        self.nama = nama          # Nama petani
        self.nik = nik            # Nomor Induk Kependudukan
        self.alamat = alamat      # Alamat petani
        self.luas_lahan = luas_lahan  # Luas lahan dalam hektar

    def tampil_info(self):
        # Metode untuk menampilkan informasi dasar petani
        print(f"Nama       : {self.nama}")
        print(f"NIK        : {self.nik}")
        print(f"Alamat     : {self.alamat}")
        print(f"Luas Lahan : {self.luas_lahan} hektar")


# Kelas turunan pertama: PetaniSawah
# Mewarisi semua atribut dari Petani, ditambah atribut khusus sawah
class PetaniSawah(Petani):
    def __init__(self, nama, nik, alamat, luas_lahan, jenis_padi, masa_tanam):
        super().__init__(nama, nik, alamat, luas_lahan)  # Memanggil constructor induk
        self.jenis_padi = jenis_padi    # Jenis padi yang ditanam
        self.masa_tanam = masa_tanam    # Masa tanam dalam bulan

    def tampil_info(self):
        # Memanggil tampil_info dari induk, lalu tambahkan info khusus sawah
        super().tampil_info()
        print(f"Jenis Padi : {self.jenis_padi}")
        print(f"Masa Tanam : {self.masa_tanam} bulan")
        print(f"Jenis      : Petani Sawah")


# Kelas turunan kedua: PetaniKebun
# Mewarisi semua atribut dari Petani, ditambah atribut khusus kebun
class PetaniKebun(Petani):
    def __init__(self, nama, nik, alamat, luas_lahan, jenis_tanaman, hasil_panen_kg):
        super().__init__(nama, nik, alamat, luas_lahan)  # Memanggil constructor induk
        self.jenis_tanaman = jenis_tanaman        # Jenis tanaman kebun
        self.hasil_panen_kg = hasil_panen_kg      # Hasil panen dalam kg

    def tampil_info(self):
        # Memanggil tampil_info dari induk, lalu tambahkan info khusus kebun
        super().tampil_info()
        print(f"Jenis Tanaman  : {self.jenis_tanaman}")
        print(f"Hasil Panen    : {self.hasil_panen_kg} kg")
        print(f"Jenis          : Petani Kebun")


# ---- PENGUJIAN INHERITANCE ----
print("=" * 40)
print("DATA PETANI SAWAH")
print("=" * 40)
petani1 = PetaniSawah("Budi Santoso", "3301010101010001", "Desa Makmur", 2.5, "IR64", 3)
petani1.tampil_info()

print()
print("=" * 40)
print("DATA PETANI KEBUN")
print("=" * 40)
petani2 = PetaniKebun("Siti Rahayu", "3301010101010002", "Desa Sejahtera", 1.8, "Singkong", 500)
petani2.tampil_info()
