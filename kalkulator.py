import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#function untuk mengakhiri while loop
def tanya_lanjut() -> bool:
    print("\n1. lanjut")
    print("2. kembali")
    out = input(">>> ").lower().strip()
    return out in ["kembali", "2", "2. kembali", "out"]
        


#kalkulator standar(aritmatika)
class KalkulatorStandard:
    @staticmethod
    def kalkulator_standar():
        while True:   
            clear()
            print("---------- mode standar ----------")
            print("")  
            try:
                #input
                no1 = float(input("masukkan angka: "))
                op = input("masukkan penjumlahan(+,-,/,x): ").lower().strip()
                no2 = float(input("masukkan angka: "))
                if op == "+":
                    hasil = (no1 + no2)
                    print(f"\n{no1} + {no2} = {hasil}")
                elif op == "-":
                    hasil = (no1 - no2)
                    print(f"\n{no1} - {no2} = {hasil}")
                elif op in ["/", ":"]:
                    hasil = (no1 / no2)
                    print(f"\n{no1} / {no2} = {hasil}")
                elif op in ["x", "*"]:
                    hasil = (no1 * no2)
                    print(f"\n{no1} x {no2} = {hasil}")
                else:
                    print("operator tidak ditemukan")
                    input("tekan Enter untuk melanjutkan...")
                    continue
                        
            except ValueError:
                    print("tolong masukkan angka!!")
                    input("tekan Enter untuk melanjutkan...")
                    continue
            except ZeroDivisionError:
                    print("Tidak dapat dibagi nol")
                    input("tekan Enter untuk melanjutkan...")
                    continue

            #mengakhiri while loop
            if tanya_lanjut():
                break
        

#kalkulator konversi suhu (celcius, fahrenheit, kelvin, reamur)
class KonverterPemuaian:
    #konversi dari satuan C, F, K, R, ke celcius
    @staticmethod
    def ke_celcius(dari_suhu, besaran_suhu):
        if dari_suhu == "c":
            return besaran_suhu
        elif dari_suhu == "f":
            return 5/9*(besaran_suhu - 32)
        elif dari_suhu == "k":
            return besaran_suhu - 273.15
        elif dari_suhu == "r":
            return 5/4 * besaran_suhu
        else:
            raise ValueError("satuan tidak valid!!")

    #konversi dari satuan celcius ke C, F, K, R
    @staticmethod
    def dari_celcius(ke_suhu, besaran_suhu):
        if ke_suhu == "c":
            return besaran_suhu
        elif ke_suhu == "f":
            return 9/5 * besaran_suhu + 32
        elif ke_suhu == "k":
            return besaran_suhu + 273.15
        elif ke_suhu == "r":
            return 4/5 * besaran_suhu
        else:
            raise ValueError("satuan tidak valid!!")

    #memanggil function dan mengembalikan nilai
    @staticmethod
    def konversi_suhu(dari_suhu, besaran_suhu, ke_suhu):
        suhu_dari_celcius = KonverterPemuaian.ke_celcius(dari_suhu, besaran_suhu) 
        return KonverterPemuaian.dari_celcius(ke_suhu, suhu_dari_celcius)

    #mengambil input user dan menampilkan hasil perhitungan ke user
    @staticmethod
    def kalkulator_suhu():
        while True:    
            clear()
            print("---------- konversi suhu ----------\n")
            
            try:
                #input
                dari_suhu = input("dari suhu (C/F/K/R): ").lower().strip()
                besaran_suhu = float(input("besaran suhu: "))
                ke_suhu = input("ke suhu (C/F/K/R): ").lower().strip()

                #validasi kelvin tidak boleh kurang dari 0
                if dari_suhu == "k" and besaran_suhu < 0:
                    print("Kelvin tidak bisa negatif")
                    input("Tekan Enter untuk melanjutkan... ")
                    continue

                #menjalankan function untuk mengkonversi suhu dan menampilakan hasil konversi
                hasil_akhir = KonverterPemuaian.konversi_suhu(dari_suhu, besaran_suhu, ke_suhu)
                print(f"\n{besaran_suhu}°{dari_suhu.upper()} = {hasil_akhir:.2f}°{ke_suhu.upper()}")
                
            #menangkap eror
            except ValueError as e:
                print(f"Eror {e}")
                input("tekan enter untuk melanjutkan... ")
                continue

            #mengakhiri while loop
            if tanya_lanjut():
                break

#kalkulator untuk menghitung pemuaian
class KalkulatorPemuaian:
    #pemuaian panjang (function)
    @staticmethod
    def pemuaian_panjang():
        while True:
            clear()
            print("\n---------- pemuaian panjang ----------\n")
            try:
                #input user
                L0 = float(input("Masukkan panjang awal: "))
                alpha = float(input("Masukkan koefisien muai panjang: "))
                dT = float(input("Masukkan perubahan suhu: "))
                
                #menghitung input user
                dL = alpha * L0 * dT
                L_akhir = L0 + dL
                
                #menampilkan hasil kalkulasi
                print(f"\nPertambahan panjang = {dL:.6g}")
                print(f"Panjang akhir = {L_akhir:.6g}")
                
            #mencegah Eror    
            except ValueError:
                print("tolong masukkan angka!!")
                input("tekan enter untuk melanjutkan...")
                continue
            
            #mengakhiri while loop
            if tanya_lanjut():
                break
            
    #pemuaian luas (function)
    @staticmethod       
    def pemuaian_luas():
        while True:
            clear()
            print("\n---------- Pemuaian Luas ----------\n")
            try:
                #input user
                A0 = float(input("Masukkan luas awal: "))
                beta = float(input("Masukkan koefisien muai luas: "))
                dT = float(input("Masukkan perubahan suhu: "))
                
                #menghitung input user
                dA = beta * A0 * dT
                A_akhir = A0 + dA

                #menampilkan hasil kalkulasi
                print(f"\nPertambahan luas = {dA:.6g}")
                print(f"Luas akhir = {A_akhir:.6g}")

            #mencegah Eror
            except ValueError:
                print("tolong masukkan angka!!")
                input("tekan enter untuk melanjutkan...")
                continue

            #mengakhiri while loop
            if tanya_lanjut():
                break

    #pemuaian volume (function)
    @staticmethod
    def pemuaian_volume():
        while True:
            clear()
            print("\n---------- Pemuaian Volume ----------\n")
            try:
                #input user
                V0 = float(input("Masukkan volume awal: "))
                gamma = float(input("Masukkan koefisien muai volume: "))
                dT = float(input("Masukkan perubahan suhu: "))

                #menghitung input user
                dV = gamma * V0 * dT
                V_akhir = V0 + dV

                #menampilkan kalkulasi
                print(f"\nPertambahan volume = {dV:.6g}")
                print(f"Volume akhir = {V_akhir:.6g}")
            
            #mencegah Eror
            except ValueError:
                print("tolong masukkan angka!!")
                input("tekan enter untuk melanjutkan...")
                continue

            #mengakhiri while loop
            if tanya_lanjut():
                break

    #menu kalkulator pemuaian, mengambil input untuk memilih mode
    @staticmethod
    def menu_pemuaian():
        while True:
            clear()

            #mengambil input user, memilih mode
            print("\n---------- kalkulator pemuaian ----------\n")
            print("1. pemuaian panjang")
            print("2. pemuaian luas")
            print("3. pemuaian volume")
            print("4. Kembali")
            pilihan = input("Pilih menu: ")

            #pemanggil function
            if pilihan in ["1", "pemuaian panjang", "1. pemuaian panjang"]:
                KalkulatorPemuaian.pemuaian_panjang()
            elif pilihan in ["2", "pemuaian luas", "2. pemuaian luas"]:
                KalkulatorPemuaian.pemuaian_luas()
            elif pilihan in ["3", "pemuaian volume", "3. pemuaian volume"]:
                KalkulatorPemuaian.pemuaian_volume()
            elif pilihan in ["4", "kembali", "4. kembali"]:
                break
            #mencegah Eror
            else:
                print("pilihan tidak valid")
                input("tekan enter untuk melanjutkan...")
                continue

#menu awal kalkulator, mengambil input untuk memilih mode
def kalkulator():
    while True:
        clear()
        print("---------- kalkulator ----------\n")
        print("pilih menu")
        print("--> 1.standar")
        print("--> 2.konversi suhu")
        print("--> 3.pemuaian suhu")
        print("\nkeluar [X]")
        print("")
        mode = input("menu: ").lower().strip()

        #pemangil function
        if mode in ["standar", "1", "1.standar"]:
            KalkulatorStandard.kalkulator_standar()
        elif mode in ["konversi suhu", "2", "2.konversi suhu"]:
            KonverterPemuaian.kalkulator_suhu()
        elif mode in ["pemuaian suhu", "3", "3.pemuaian suhu"]:
            KalkulatorPemuaian.menu_pemuaian()
        elif mode in ["x", "keluar"]:
            print("program selesai...")
            return
        else:
            print("mode tidak ditemukan")
            input("tekan Enter untuk melanjutkan...")

#memanggil fungsi agar program bekerja
if __name__ == "__main__":
    kalkulator() 