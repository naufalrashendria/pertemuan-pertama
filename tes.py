while True: # agar terus berulang meminta input dari user
    print("\n======== MENU ========")
    print("1. Cek Angka Genap/Ganjil")
    print("2. Itung Luas Persegi Panjang")
    print("3. Metu")

    pilihan = input("Pilih o menune (1/2/3): ") # input pilihan menu

    if pilihan == '1':
        angka = int(input("Masukkan angka: ")) # input angka
        if angka % 2 == 0:  
            print(f"{angka} adalah angka genap") # output jika angka genap
        else:
            print(f"{angka} adalah angka ganjil") # output jika angka ganjil

    elif pilihan == '2':
        dowo = int(input("Masukkan panjang persegi panjang: ")) 
        ombo = int(input("Masukkan lebar persegi panjang: ")) 
        luas = dowo * ombo 

        print(f"Luas persegi panjang adalah {luas}")

    elif pilihan == '3':
        print("Suwon Bossss...")
        break

    else:
        print("GAK ENEK, PILIHO NEH!!!.") 
        break