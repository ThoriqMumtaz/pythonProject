class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    def hitung_harga(self):
        return self.harga
    
class ProdukDigital(Produk):
    def __init__(self, nama, harga, ukuranfile, formatfile):
        super().__init__(nama, harga)
        self.ukuran_file = ukuranfile
        self.format_file = formatfile
    def hitung_harga(self):
        return self.harga

class ProdukFisik(Produk):
    def __init__(self, nama, harga, ongkir, berat, alamat_pengiriman, stok_gudang):
        super().__init__(nama, harga)
        self.ongkir = ongkir
        self.berat = berat
        self.alamat_pengiriman = alamat_pengiriman
        self.stok_gudang = stok_gudang
    def hitung_harga(self):
        return self.harga + self.ongkir
    
class KeranjangBelanja:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah
    def TotalHarga(self):
        TotalHarga = self.produk.hitung_harga() * self.jumlah
        return TotalHarga
    
    

p1 = ProdukDigital("", int, "", "")
p2 = ProdukFisik("", int, int, int, "", int)

item1 = KeranjangBelanja(p1, int)
item2 = KeranjangBelanja(p2, int)

print(item1.TotalHarga())
print(item2.TotalHarga())
   