# Variabel global untuk menyimpan data
konversi_suhu = []

# Tampilan menu
def show_menu():
    print("\t")
    print("----------- Menu -----------")
    print("[1] Convert Celcius to Fahrenheit")
    print("[2] Convert Fahrenheit to Celcius")
    print("[3] Keluar")

    menu = input("Silahkan Pilih Menu: ")
    print("\t")

    if menu == "1":
        convert_celcius()

    elif menu == "2":
        convert_fahrenheit()

    elif menu == "3":
        keluar(), exit()

    else:
        print("Perintah tidak dikenal.")

# Program konversi Celcius to Fahrenheit
def convert_fahrenheit():
    # Input data suhu celcius
    celc_fahrenheit = float(input("Masukkan Suhu Fahrenheit: "))

    # Kalkulasi rumus
    fahr = (9/5 * celc_fahrenheit) + 32

    # Menampilkan hasil
    print("Suhu", celc_fahrenheit, "Fahrenheit setara dengan", fahr, "Celcius")

# Program konversi Fahrenheit to Celcius
def convert_celcius():
    # Input data suhu fahrenheit
    celc_celcius = float(input("Masukkan Suhu Celcius: "))

    # Kalkulasi rumus
    celcius = 5/9 * (celc_celcius - 32)

    # Menampilkan hasil
    print("Suhu", celc_celcius, "Celcius setara dengan", celcius, "Fahrenheit")

# Keluar program
def keluar():
    print("Jazakallahu Khairan Katsiran")

# Nanyeak ulang
if __name__ == "__main__":

    while(True):
        show_menu()
