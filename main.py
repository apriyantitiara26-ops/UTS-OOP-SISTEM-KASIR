class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga):
        if Produk.validasi_harga(harga):
            self.__harga = harga
        else:
            raise ValueError("Harga tidak boleh negatif!")

    @staticmethod
    def validasi_harga(harga):
        return harga >= 0

    @classmethod
    def buat_produk(cls, nama, harga):
        return cls(nama, harga)


class Kasir:
    def __init__(self):
        self.keranjang = []

    def tampilkan_produk(self):
        print("\n=== DAFTAR PRODUK ===")
        print("1. Indomie       Rp3.500")
        print("2. Air Mineral   Rp4.000")
        print("3. Roti          Rp5.000")
        print("4. Susu          Rp7.000")

    def tambah_barang(self):
        self.tampilkan_produk()

        pilihan = input("\nPilih barang (1-4): ")
        jumlah = int(input("Jumlah barang: "))

        daftar = {
            "1": Produk.buat_produk("Indomie", 3500),
            "2": Produk.buat_produk("Air Mineral", 4000),
            "3": Produk.buat_produk("Roti", 5000),
            "4": Produk.buat_produk("Susu", 7000)
        }

        if pilihan in daftar and jumlah > 0:
            produk = daftar[pilihan]
            subtotal = produk.harga * jumlah

            self.keranjang.append(
                (produk, jumlah, subtotal)
            )

            print("Barang berhasil ditambahkan!")
        else:
            print("Pilihan atau jumlah tidak valid!")

    def tampilkan_struk(self):
        if not self.keranjang:
            print("Belum ada barang yang dibeli!")
            return

        total = 0

        print("\n======= STRUK BELANJA =======")

        for produk, jumlah, subtotal in self.keranjang:
            print(produk.nama, "x", jumlah, "=", subtotal)
            total += subtotal

        print("-----------------------------")
        print("Total Belanja: Rp", total)

        bayar = int(input("Uang pembayaran: Rp"))

        if bayar >= total:
            print("Kembalian: Rp", bayar - total)
            print("Terima kasih sudah berbelanja!")
            self.keranjang.clear()
        else:
            print("Uang pembayaran kurang!")
        

# Membuat object kasir
kasir = Kasir()

# Menu utama
while True:
    print("\n===== APLIKASI SISTEM KASIR =====")
    print("1. Tambah Barang")
    print("2. Cetak Struk dan Bayar")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kasir.tambah_barang()
    elif pilihan == "2":
        kasir.tampilkan_struk()
    elif pilihan == "3":
        print("Program kasir selesai.")
        break
    else:
        print("Pilihan tidak tersedia!")