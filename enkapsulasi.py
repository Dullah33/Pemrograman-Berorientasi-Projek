# ============================================================
# (c) ENKAPSULASI - Menyembunyikan Data Rahasia
# ============================================================
# Atribut yang bersifat rahasia (NIK, penghasilan, PIN rekening)
# disembunyikan menggunakan double underscore (__) agar tidak bisa
# diakses langsung dari luar kelas

class DataPetani:
    def __init__(self, nama, nik, penghasilan_per_tahun, pin_rekening):
        self.nama = nama                          # Atribut publik: bisa diakses langsung
        self.__nik = nik                          # RAHASIA: NIK petani
        self.__penghasilan = penghasilan_per_tahun  # RAHASIA: penghasilan
        self.__pin = pin_rekening                 # RAHASIA: PIN rekening bantuan

    # Getter untuk NIK - menampilkan NIK yang disensor sebagian
    def get_nik_sensor(self):
        nik_str = str(self.__nik)
        return nik_str[:4] + "****" + nik_str[-4:]  # Hanya tampilkan 4 digit awal & akhir

    # Getter untuk penghasilan - hanya bisa dibaca, tidak bisa diubah sembarangan
    def get_penghasilan(self):
        return self.__penghasilan

    # Setter penghasilan - validasi sebelum mengubah nilai
    def set_penghasilan(self, nilai_baru):
        if nilai_baru < 0:
            print("ERROR: Penghasilan tidak boleh negatif!")  # Validasi data
        else:
            self.__penghasilan = nilai_baru
            print("Penghasilan berhasil diperbarui.")

    # Metode verifikasi PIN - PIN tidak pernah ditampilkan, hanya dicek kebenarannya
    def verifikasi_pin(self, pin_input):
        if pin_input == self.__pin:
            print("✅ PIN benar! Akses rekening diberikan.")
        else:
            print("❌ PIN salah! Akses ditolak.")

    # Metode untuk menampilkan info yang aman (tidak menampilkan data rahasia)
    def tampil_info_publik(self):
        print(f"Nama       : {self.nama}")
        print(f"NIK        : {self.get_nik_sensor()}")  # NIK disensor
        print(f"Penghasilan: Rp {self.__penghasilan:,.0f}")
        print(f"PIN        : [TERSEMBUNYI]")             # PIN tidak ditampilkan


# ---- PENGUJIAN ENKAPSULASI ----
print("=" * 40)
print("SISTEM DATA PETANI (ENKAPSULASI)")
print("=" * 40)

petani = DataPetani("Budi Santoso", "3301010101010001", 24_000_000, "1234")

# Menampilkan info publik
petani.tampil_info_publik()

print()
print("-- Uji Verifikasi PIN --")
petani.verifikasi_pin("0000")   # PIN salah
petani.verifikasi_pin("1234")   # PIN benar

print()
print("-- Uji Ubah Penghasilan --")
petani.set_penghasilan(-5000)        # Input tidak valid
petani.set_penghasilan(30_000_000)   # Input valid

print()
print("-- Uji Akses Langsung ke Atribut Rahasia --")
try:
    print(petani.__nik)   # Ini akan error karena NIK bersifat private
except AttributeError as e:
    print(f"AKSES DITOLAK: {e}")  # Enkapsulasi berhasil melindungi data
