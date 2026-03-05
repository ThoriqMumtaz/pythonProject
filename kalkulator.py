import os
import sys
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#input & keterangan
def kalkulator():
    while True:
        clear()
        print("----- kalkulator -----")
        print("")
        print("pilih menu")
        print("--> 1.standar")
        print("--> 2.konversi suhu")
        print("\nkeluar [X]")
        print("")
        mode = input("menu: ").lower().strip()


        #kalkulator standar(aritmatika)
        def Kalkulator_standar():
            while True:   
                clear()
                print("--- mode standar ---")
                print("")  
                try:
                    #input
                    no1 = float(input("masukkan angka: "))
                    op = input("masukkan penjumlahan(+,-,/,x): ").lower().strip()
                    no2 = float(input("masukkan angka: "))
                    if op == "+":
                        hasil = (no1 + no2)
                        print(f"{no1} + {no2} = {hasil}")
                    elif op == "-":
                        hasil = (no1 - no2)
                        print(f"{no1} - {no2} = {hasil}")
                    elif op in ["/", ":"]:
                        hasil = (no1 / no2)
                        print(f"{no1} / {no2} = {hasil}")
                    elif op in ["x", "*"]:
                        hasil = (no1 * no2)
                        print(f"{no1} x {no2} = {hasil}")
                    else:
                        print("operator tidak ditemukan")
                        input("tekan Enter untuk melanjutkan...")
                            
                except ValueError:
                        print("tolong masukkan angka!!")
                except ZeroDivisionError:
                        print("Tidak dapat dibagi nol")

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
                print("--- konversi suhu ---")
                print("")
                
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
        
                    #celcius ke fahrenheit
                    if dari_suhu in ["celcius", "c"] and ke_suhu in ["fahrenheit", "f"]:
                        suhu_akhir = (9/5 * besaran_suhu + 32) 
                        print(f"{besaran_suhu} Celcius = {suhu_akhir} fahrenheit")
                    
                    #celcius ke kelvin
                    elif dari_suhu in ["celcius", "c"] and ke_suhu in ["kelvin", "k"]:
                        suhu_akhir = (besaran_suhu + 273)
                        print(f"{besaran_suhu} Celcius = {suhu_akhir} Kelvin")
                    
                    #celcius ke reamur
                    elif dari_suhu in ["celcius", "c"] and ke_suhu in ["reamur", "r"]:
                        suhu_akhir = (4/5 * besaran_suhu)
                        print(f"{besaran_suhu} Celcius = {suhu_akhir} Reamur")
                    
                    #fahrenheit ke celcius
                    elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["celcius", "c"]:
                        suhu_akhir = (5/9 * (besaran_suhu - 32))
                        print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} Celcius")
                    
                    #fahrenheit ke kelvin
                    elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["kelvin", "k"]:
                        suhu_akhir = (5/9 * (besaran_suhu - 32) + 273)
                        print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} kelvin")
                    
                    #fahrenheit ke reamur
                    elif dari_suhu in ["fahrenheit", "f"] and ke_suhu in ["reamur", "r"]:
                        suhu_akhir = (4/9 * (besaran_suhu - 32))
                        print(f"{besaran_suhu} Fahrenheit = {suhu_akhir} Reamur")
                    
                    #kelvin ke Celcius
                    elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["celcius", "c"]:
                        suhu_akhir = (besaran_suhu - 273)
                        print(f"{besaran_suhu} Kelvin = {suhu_akhir} Celcius")
                    
                    #kelvin ke fahrenheit
                    elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["fahrenheit", "f"]:
                        suhu_akhir = (9/5 * (besaran_suhu - 273) + 32)
                        print(f"{besaran_suhu} Kelvin = {suhu_akhir} Fahrenheit")
                    
                    #kelvin ke reamur
                    elif dari_suhu in ["kelvin", "k"] and ke_suhu in ["reamur", "r"]:
                        suhu_akhir = (4/5 * (besaran_suhu - 273))
                        print(f"{besaran_suhu} Kelvin = {suhu_akhir} Reamur")
                    
                    #reamur ke celcius
                    elif dari_suhu in ["reamur", "r"] and ke_suhu in ["celcius", "c"]:
                        suhu_akhir = (5/4 * besaran_suhu)
                        print(f"{besaran_suhu} Reamur = {suhu_akhir} Celcius")
                    
                    #reamur ke fahrenheit
                    elif dari_suhu in ["reamur", "r"] and ke_suhu in ["fahrenheit", "f"]:
                        suhu_akhir = (9/4 * besaran_suhu + 32)
                        print(f"{besaran_suhu} Reamur = {suhu_akhir} Fahrenheit")
                    
                    #reamur ke kelvin
                    elif dari_suhu in ["reamur", "r"] and ke_suhu in ["kelvin", "k"]:
                        suhu_akhir = (5/4 * besaran_suhu + 273)
                        print(f"{besaran_suhu} Reamur = {suhu_akhir} Kelvin")
                
                    #penangkap eror
                    else:
                        print("kombinasi suhu tidak valid")
                        input("tekan Enter untuk melanjutkan...")
                #penangkap eror
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

        #pemangil fungsi
        if mode in ["standar", "1", "1.standar"]:
            Kalkulator_standar()
        elif mode in ["konversi suhu", "2", "2.konversi suhu"]:
            Kalkulator_suhu()
        elif mode in ["x", "keluar"]:
            print("proggram selesai...")
            return
        else:
            print("mode tidak ditemukan")
            input("tekan Enter untuk melanjutkan...")
            kalkulator()

#memanggil fungsi agar program bekerja
kalkulator() 