# Variabel global untuk menyimpan data
data_pribadi = []

# Data Dictionary
data_pribadi = {
    "NIM": "L200220108",
    "Nama": "Muhammad Yulian Rizki",
    "Alamat": "Jln. Srikatan Nomor 35C",
    "Kode-Pos": "57391",
    "Umur": "18th",
    "Instagram": "@myulianrizki",
    "Hobby": "Bikin Design"
}

# Fungsi Menampilkan bantuan
def tampilkan_bantuan():
    print(" 1. Untuk menampilkan NIM siswa, anda bisa ketik N")
    print(" 2. Untuk menampilkan Nama siswa, anda bisa ketik a")
    print(" 3. Untuk menampilkan Alamat siswa, anda bisa ketik A")
    print(" 4. Untuk menampilkan Kode Pos siswa, anda bisa ketik K")
    print(" 5. Untuk menampilkan Umur siswa, anda bisa ketik u")
    print(" 6. Untuk menampilkan Instagram siswa, anda bisa ketik i")
    print(" 7. Untuk menampilkan Hobby siswa, anda bisa ketik h")
    print(" 8. Untuk keluar program, anda bisa ketik k")

# Fungsi Menampilkan NIM
def tampilkan_nim():
    print("NIM:", data_pribadi.get("NIM"))

# Fungsi Menampilkan Nama
def tampilkan_nama():
    print("Nama:", data_pribadi.get("Nama"))

# Fungsi Menampilkan Alamat
def tampilkan_alamat():
    print("Alamat:", data_pribadi.get("Alamat"))

# Fungsi Menampilkan Kode Pos
def tampilkan_kode_pos():
    print("Kode Pos:", data_pribadi.get("Kode-Pos"))

# Fungsi Menampilkan Umur
def tampilkan_umur():
    print("Umur:", data_pribadi.get("Umur"))

# Fungsi Menampilkan Instagram
def tampilkan_instagram():
    print("Instagram:", data_pribadi.get("Instagram"))

# Fungsi Menampilkan Hobby
def tampilkan_hobby():
    print("Hobby:", data_pribadi.get("Hobby"))

# Fungsi Menampilkan
def keluar():
    print("Jazakallahu Khairan Katsiran")


# Fungsi untuk menampilkan Menu
def show_menu():
    print("\t")  
    print("----------- Menu ----------") 
    print("[b] Show Help")
    print("[N] NIM Siswa")
    print("[a] Nama Siswa") 
    print("[A] Alamat Siswa") 
    print("[K] Kode Pos Siswa")
    print("[u] Umur Siswa")
    print("[i] Instagram Siswa")
    print("[h] Hobby Siswa")
    print("[k] Keluar")
    
    menu = input("Silahkan Pilih Menu: ")
    print("\t") 

    if menu == "b":
        print("Pilihan Saudara: b"),
        tampilkan_bantuan()

    elif menu == "N":
        print("Pilihan Saudara: N"),
        tampilkan_nim()

    elif menu == "a":
        print("Pilihan Saudara: a"),
        tampilkan_nama()

    elif menu == "A":
        print("Pilihan Saudara: A"),
        tampilkan_alamat()

    elif menu == "K":
        print("Pilihan Saudara: K"),
        tampilkan_kode_pos()

    elif menu == "u":
        print("Pilihan Saudara: u"),
        tampilkan_umur()

    elif menu == "i":
        print("Pilihan Saudara: i"),
        tampilkan_instagram()

    elif menu == "h":
        print("Pilihan Saudara: h"),
        tampilkan_hobby()
    
    elif menu == "k":
        print("Pilihan Saudara: k"),
        keluar(), exit()
    else:
        print("Perintah tidak valid.") 


# Nanyeak ulang
if __name__ == "__main__":

    while(True):
        show_menu()