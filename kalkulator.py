import os
def clear():
    os.system("cls")


#kalkulator standar(aritmatika)
def Kalkulator_standar():
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
        print("\n1. lanjut")
        print("2. kembali")
        out = input(">>> ").lower().strip()
        if out in ["kembali", "2", "2. kembali", "out"]:
            break
        else:
            pass
        

#kalkulator konversi suhu (celcius, fahrenheit, kelvin, reamur)
def Kalkulator_suhu():
    while True:    
        clear()
        print("---------- konversi suhu ----------\n")
        
        try:
            #input
            dari_suhu = input("dari suhu (C/F/K/R): ").lower().strip()
            besaran_suhu = float(input("besaran suhu: "))
            ke_suhu = input("ke suhu (C/F/K/R): ").lower().strip()

            #(validasi) Kelvin tidak boleh minus/negatif
            if dari_suhu in ["k","kelvin"] and besaran_suhu < 0:
                print("Kelvin tidak bisa negatif")
                input("Tekan Enter untuk melanjutkan... ")
                continue

            #celcius ke fahrenheit, kelvin, reamur
            if dari_suhu in ["celcius", "c"] and ke_suhu in ["fahrenheit", "f"]:
                suhu_akhir = (9/5 * besaran_suhu + 32) 
                print(f"{besaran_suhu} Celcius = {suhu_akhir} fahrenheit")
            elif dari_suhu in ["celcius", "c"] and ke_suhu in ["kelvin", "k"]:
                suhu_akhir = (besaran_suhu + 273)
                print(f"{besaran_suhu} Celcius = {suhu_akhir} Kelvin")
            elif dari_suhu in ["celcius", "c"] and ke_suhu in ["reamur", "r"]:
                suhu_akhir = (4/5 * besaran_suhu)
                print(f"{besaran_suhu} Celcius = {suhu_akhir} Reamur")
            
            #fahrenheit ke celcius, kelvin, reamur
            elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["celcius", "c"]:
                suhu_akhir = (5/9 * (besaran_suhu - 32))
                print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} Celcius")
            elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["kelvin", "k"]:
                suhu_akhir = (5/9 * (besaran_suhu - 32) + 273)
                print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} kelvin")
            elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["reamur", "r"]:
                suhu_akhir = (4/9 * (besaran_suhu - 32))
                print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} Reamur")
            
            #kelvin ke Celcius, fahrenheit, reamur
            elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["celcius", "c"]:
                suhu_akhir = (besaran_suhu - 273)
                print(f"{besaran_suhu} Kelvin = {suhu_akhir} Celcius")
            elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["fahrenheit", "f"]:
                suhu_akhir = (9/5 * (besaran_suhu - 273) + 32)
                print(f"{besaran_suhu} Kelvin = {suhu_akhir} Fahrenheit")
            elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["reamur", "r"]:
                suhu_akhir = (4/5 * (besaran_suhu - 273))
                print(f"{besaran_suhu} Kelvin = {suhu_akhir} Reamur")
            
            #reamur ke celcius, fahrenheit, kelvin
            elif dari_suhu in ["reamur", "r"] and ke_suhu in ["celcius", "c"]:
                suhu_akhir = (5/4 * besaran_suhu)
                print(f"{besaran_suhu} Reamur = {suhu_akhir} Celcius")
            elif dari_suhu in ["reamur", "r"] and ke_suhu in ["fahrenheit", "f"]:
                suhu_akhir = (9/4 * besaran_suhu + 32)
                print(f"{besaran_suhu} Reamur = {suhu_akhir} Fahrenheit")
            elif dari_suhu in ["reamur", "r"] and ke_suhu in ["kelvin", "k"]:
                suhu_akhir = (5/4 * besaran_suhu + 273)
                print(f"{besaran_suhu} Reamur = {suhu_akhir} Kelvin")
        
            #menangkap eror
            else:
                print("kombinasi suhu tidak valid")
                input("tekan Enter untuk melanjutkan...")
        #menangkap eror
        except ValueError:
            print("tolong masuk angka!!")

        #mengakhiri while loop
        print("\n1. lanjut")
        print("2. kembali")
        out = input(">>> ").lower().strip()
        if out in ["kembali", "2", "2. kembali", "out"]:
            break
        else:
            pass

#pemuaian panjang (function)
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
            print("")
            print(f"Pertambahan panjang = {dL}")
            print(f"Panjang akhir = {L_akhir}")
            
            #mengakhiri loop
            print("\n1. lanjut")
            print("2. kembali")
            out = input(">>> ").lower().strip()
            if out in ["kembali", "2", "2. kembali", "out"]:
                break
            else:
                pass
        #mencegah Eror    
        except ValueError:
            print("tolong masukkan angka!!")
            input("tekan enter untuk melanjutkan...")
            continue
        
#pemuaian luas (function)       
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
            print("")
            print(f"Pertambahan luas = {dA}")
            print(f"Luas akhir = {A_akhir}")
            
            #mengakhiri loop
            print("\n1. lanjut")
            print("2. kembali")
            out = input(">>> ").lower().strip()
            if out in ["kembali", "2", "2. kembali", "out"]:
                break
            else:
                pass

        #mencegah Eror
        except ValueError:
            print("tolong masukkan angka!!")
            input("tekan enter untuk melanjutkan...")
            continue

#pemuaian volume (function)
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
            print(f"Pertambahan volume = {dV}")
            print(f"Volume akhir = {V_akhir}")
            
            #mengakhiri loop
            print("\n1. lanjut")
            print("2. kembali")
            out = input(">>> ").lower().strip()
            if out in ["kembali", "2", "2. kembali", "out"]:
                break
            else:
                pass
        
        #mencegah Eror
        except ValueError:
            print("tolong masukkan angka!!")
            input("tekan enter untuk melanjutkan...")
            continue

#menu kalkulator pemuaian, mengambil input untuk memilih mode
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
            pemuaian_panjang()
        elif pilihan in ["2", "pemuaian luas", "2. pemuaian luas"]:
            pemuaian_luas()
        elif pilihan in ["3", "pemuaian volume", "3. pemuaian volume"]:
            pemuaian_volume()
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
            Kalkulator_standar()
        elif mode in ["konversi suhu", "2", "2.konversi suhu"]:
            Kalkulator_suhu()
        elif mode in ["pemuaian suhu", "3", "3.pemuaian suhu"]:
            menu_pemuaian()
        elif mode in ["x", "keluar"]:
            print("program selesai...")
            return
        else:
            print("mode tidak ditemukan")
            input("tekan Enter untuk melanjutkan...")

#memanggil fungsi agar program bekerja
kalkulator() 