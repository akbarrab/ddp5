list_kendaraan = ["Mobil", "Sedan", "1800", "grey", "4"]

list_kendaraan.append("109.000.0000")
list_kendaraan.append("BMW E34")
list_kendaraan.insert(2, "BMW")

print(list_kendaraan)

def hitung_luas_persegi(sisi):
    return sisi * sisi

def hitung_luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def main():
    while True:
        print("Pilih jenis bangun datar:")
        print("1. Persegi")
        print("2. Lingkaran")
        print("3. Segitiga")
        print("0. Keluar")
        
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "0":
            print("Terima kasih, sudah memakai program kami")
            break
        
        try:
            pilihan = int(pilihan)
        except ValueError:
            print("Pilihan tidak valid. Harap masukkan angka 1, 2, 3, atau 0.")
            continue

        match pilihan:
            case 1:
                sisi = float(input("Masukkan panjang sisi persegi: "))
                luas = hitung_luas_persegi(sisi)
                print(f"Luas persegi: {luas}")
            case 2:
                jari_jari = float(input("Masukkan jari-jari lingkaran: "))
                luas = hitung_luas_lingkaran(jari_jari)
                print(f"Luas lingkaran: {luas}")
            case 3:
                alas = float(input("Masukkan panjang alas segitiga: "))
                tinggi = float(input("Masukkan tinggi segitiga: "))
                luas = hitung_luas_segitiga(alas, tinggi)
                print(f"Luas segitiga: {luas}")
            case _:
                print("Pilihan tidak valid. Harap masukkan angka 1, 2, 3, atau 0.")

if _name_ == "_main_":
    main()