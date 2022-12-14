# Menghitung Berat Badan Ideal (BMI)
class hitungBMI():

    print("\n")

    # Menghitung BMI
    def rumus_BMI():

        # Masukkan Data
        bb = float(input("Masukkan Berat Badan Anda (kg): "))
        tb = float(input("Masukkan Tinggi Badan Anda (cm): "))

        # Jadikan Satuan Cm ke M
        meter_tb = tb / 100
    
        # Rumus BMI
        bmi = bb / meter_tb ** 2

        print("\t")
        # Komparasi BMI
        if 18.5 <= bmi <= 22.9:
            print("Nilai BMI anda:", bmi, "= Normal Weight")
        elif bmi < 18.5:
            print("Nilai BMI anda:", bmi, "= Under Weight")
        elif bmi > 22.9:
            print("Nilai BMI anda:", bmi, "= Over Weight")
        

    rumus_BMI()

# Fungsi Menampilkan Keluar
def keluar():
    print("Jazakallahu Khairan Katsiran")
    print("\t")

# Fungsi Menampilkan Menu
def tampilkan_menu():
    print("\t")
    print("------ Aku Nanyeak? ------")
    print("[1] Mau Hitung BMI Lagi?")
    print("[3] Keluar")

    menu = input("Pilih Menu: ")
    print("\t")

    if menu == "1":
        hitungBMI.rumus_BMI()

    elif menu == "3":
        keluar(), exit()

    else:
        print("Perintah tidak dikenal.")

# Nanyeak ulang
if __name__ == "__main__":

    while(True):
        tampilkan_menu()

