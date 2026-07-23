def cek_genap_ganjil():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap")
    else:
        print(f"{angka} adalah angka ganjil")

    while True:
        ulang = input("Periksa Angka Lain Gak? (y/n): ")
        if ulang.lower() == 'y':
            angka = int(input("Masukkan angka: "))
            if angka % 2 == 0:
                print(f"{angka} adalah angka genap")
            else:
                print(f"{angka} adalah angka ganjil")
        elif ulang.lower() == 'n':
            break
        else:
            print("Pilihan Gaenek. Silakan masukkan 'y' atau 'n'.")


def hitung_luas():
    dowo = int(input("Masukkan panjang persegi panjang: "))
    ombo = int(input("Masukkan lebar persegi panjang: "))
    luas = dowo * ombo
    print(f"Luas persegi panjang adalah {luas}")


def tampilkan_menu():
    while True:
        print("\n======== MENU ========")
        print("1. Cek Angka Genap/Ganjil")
        print("2. Hitung Luas Persegi Panjang")
        print("3. Metu")

        pilihan = input("Pilih o menune (1/2/3): ")

        if pilihan == "1":
            cek_genap_ganjil()
        elif pilihan == "2":
            hitung_luas()
        elif pilihan == "3":
            print("Suwon Bossss...")
            break
        else:
            print("GAK ENEK, PILIHO NEH!!!")


tampilkan_menu()
