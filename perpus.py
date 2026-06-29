class Perpustakaan:
    def __init__(self, nama_perpus):
        self.nama_perpus = nama_perpus
        self.daftar_buku = []
        self.daftar_anggota = []
    
    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
    
    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)
    
    def pinjam_buku(self, anggota, buku):
        if buku.status == "tersedia":
            buku.status ="dipinjam"
            anggota.buku_dipinjam.append(buku)
        elif buku.status == "dipinjam":
            print("buku sudah dipinjam")
    
    def kembalikan_buku(self, anggota, buku):
        if buku in anggota.buku_dipinjam:
            buku.status = "tersedia"
            anggota.buku_dipinjam.remove(buku)

class Buku:
    def __init__(self, judul, penulis, status):
        self.judul = judul
        self.penulis = penulis
        self.status = status
        
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []

perpus = Perpustakaan("Perpus Kota")

buku1 = Buku("Python Dasar", "Budi", "tersedia")
anggota1 = Anggota("Andi")
anggota2 = Anggota("asep")

perpus.tambah_buku(buku1)
perpus.tambah_anggota(anggota1)

perpus.pinjam_buku(anggota2, buku1)


