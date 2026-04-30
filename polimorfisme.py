# ============================================================
# (b) POLIMORFISME - Sistem Dinamis
# ============================================================
# Satu fungsi "hitung_subsidi()" dipanggil pada berbagai tipe objek petani,
# namun menghasilkan perhitungan yang berbeda tergantung tipe objeknya

class Petani:
    def __init__(self, nama, luas_lahan):
        self.nama = nama                  # Nama petani
        self.luas_lahan = luas_lahan      # Luas lahan dalam hektar

    def hitung_subsidi(self):
        # Metode dasar, akan di-override oleh kelas turunan
        pass

    def tampil_subsidi(self):
        # Metode untuk menampilkan hasil perhitungan subsidi
        subsidi = self.hitung_subsidi()   # Memanggil metode sesuai tipe objeknya
        print(f"Petani  : {self.nama}")
        print(f"Subsidi : Rp {subsidi:,.0f}")
        print()


class PetaniSawah(Petani):
    def __init__(self, nama, luas_lahan):
        super().__init__(nama, luas_lahan)

    def hitung_subsidi(self):
        # Subsidi sawah: Rp 500.000 per hektar
        return self.luas_lahan * 500_000


class PetaniKebun(Petani):
    def __init__(self, nama, luas_lahan):
        super().__init__(nama, luas_lahan)

    def hitung_subsidi(self):
        # Subsidi kebun: Rp 300.000 per hektar
        return self.luas_lahan * 300_000


class PetaniTegalan(Petani):
    def __init__(self, nama, luas_lahan):
        super().__init__(nama, luas_lahan)

    def hitung_subsidi(self):
        # Subsidi tegalan: Rp 200.000 per hektar
        return self.luas_lahan * 200_000


# ---- PENGUJIAN POLIMORFISME ----
# Daftar petani dengan berbagai tipe
daftar_petani = [
    PetaniSawah("Budi Santoso", 2.5),
    PetaniKebun("Siti Rahayu", 1.8),
    PetaniTegalan("Joko Widodo", 3.0),
]

print("=" * 40)
print("PERHITUNGAN SUBSIDI PETANI")
print("=" * 40)

# Satu fungsi tampil_subsidi() dipanggil ke semua objek,
# namun hasilnya berbeda-beda (polimorfisme)
for petani in daftar_petani:
    petani.tampil_subsidi()
