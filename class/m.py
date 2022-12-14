class hitungBMI():
    def bmi_calculation():
        while True:
            #try validasi yang diinput hanya bilagnan desimal atau bulat
            try: 
                tinggi = float(input ("Masukkan Tinggi badan (m): ")) #input tinggi badan
                berat = float(input ("Masukkan Berat Badan (kg): ")) #input berat badan
                bmi = berat / (tinggi * tinggi) #penghitungan BMI
                if 18.5 <= bmi <= 22.9:
                    print("Normal")
                elif bmi < 18.5:
                    print("Underweight")
                elif 22.9 < bmi :
                    print ("Overweight")
                break
            #except digunakan untuk valdiasi jika inputan berupa selain bilangan desimal atau bulat maka akan mengeluarkan error
            except ValueError:
                print("Hanya Boleh Di isi Bilangan desimal atau bulat!")

    bmi_calculation()


        



