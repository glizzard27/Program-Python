# Project Super Calculator dengan menggunakan bahasa Python
# Nama : Muhammad Fajar Baihaqi
# No. Peserta : XM24028
# NPM : 50421950 
# Kelas : 3IA20

def main():
    while True:
        print("\n====== Supercalculator ======")
        print("1. Kalkulator Dasar Aritmatika")
        print("2. Kalkulator Konversi Suhu")
        print("3. Kalkulator BMI")
        print("4. Keluar")
        print("=======================")

        pilihan_menu = int(input("Pilih nomor menu (1/2/3/4): "))

        if pilihan_menu == 1:
            kalkulator_biasa()
            ulang()
        elif pilihan_menu == 2:
            kalkulator_suhu()
            ulang()
        elif pilihan_menu == 3:
            kalkulator_bmi()
            ulang()
        elif pilihan_menu == 4:
            print("Terima kasih telah menggunakan Supercalculator. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu 1, 2, 3, atau 4.")
            ulang()

def kalkulator_biasa():
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: "))

    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            print("Bilangan Tak Terdefinisi")
            return
        
    print(f"Hasil: {hasil}")

def kalkulator_suhu():
    print("1. Konversi Celsius ke Fahrenheit")
    print("2. Konversi Fahrenheit ke Celsius")

    pilihan = int(input("Pilih nomor opsi (1/2): "))
    
    def konversi_celsius_ke_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def konversi_fahrenheit_ke_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    if pilihan == 1:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        hasil = konversi_celsius_ke_fahrenheit(celsius)
        print(f"{celsius} Celsius sama dengan {hasil:.2f} Fahrenheit")

    elif pilihan == 2:
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        hasil = konversi_fahrenheit_ke_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit sama dengan {hasil:.2f} Celsius")

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

def kalkulator_bmi():
    def hitung_bmi(berat, tinggi):
        bmi = berat / (tinggi ** 2)
        return bmi

    def evaluasi_bmi(bmi):
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"
    
    berat = float(input("Masukkan berat (kilogram): "))
    tinggi = float(input("Masukkan tinggi (meter): "))

    bmi = hitung_bmi(berat, tinggi)
    status_bmi = evaluasi_bmi(bmi)

    print(f"\nBMI Anda: {bmi:.2f}")
    print(f"Status BMI: {status_bmi}")

def ulang():
    while main == True :
        main()
    
# Memanggil dan Menjalankan Fungsi Utama
main()
