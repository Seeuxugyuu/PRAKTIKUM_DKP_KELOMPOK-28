from Method import *

menu = []
harga = []

def hitung_total_harga():
    return sum(harga)

def input_uang_pembayaran():
    return int(input("Uang Pembayaran:    | Rp"))

def hitung_kembali(uang_bayar, total_harga):
    return uang_bayar - total_harga

def tampilkan_rincian_pemesanan():
    print("============================================")
    print("               RINCIAN PEMESANAN")
    print("============================================")
    print("Menu                | Harga")
    print("--------------------|-------")
    for i in range(len(menu)):
        print(f"{menu[i]:19} | Rp{harga[i]:>6}")
    print("--------------------|-------")

def tampilkan_terima_kasih():
    print("")
    print("                TERIMA KASIH")
    print("============================================")

def tampilkan_keterangan_kurang():
    print("Uang pembayaran kurang, ulangi!")

def tampilkan_metode_pembayaran(metode):
    panggil = metode(total_harga)
    panggil.thx()
    panggil.selesai(3)
    input("Tekan Enter untuk bisa keluar")

print("============================================")
print("         RESTORAN STEAK KELOMPOK 28")
print("============================================")
while True:
    print("MENU:")
    print("1. Beef")
    print("2. Chicken")
    print("3. Pasta")
    print("4. Drinks")
    print("5. Selesai")
    pil = int(input("Pilih menu : "))
    if pil == 1:
        while True:
            print("============================================")
            print("               BEEF MENU")
            print("============================================")
            print("1. Sirloin - Rp43.000")
            print("2. Tenderloin - Rp45.000")
            print("3. Ribeye - Rp47.000")
            print("4. T-Bone - Rp105.000")
            print("5. Kembali")
            pil_beef = int(input("Pilih menu : "))
            if pil_beef == 1:
                menu.append("Sirloin")
                harga.append(43000)
            elif pil_beef == 2:
                menu.append("Tenderloin")
                harga.append(45000)
            elif pil_beef == 3:
                menu.append("Ribeye")
                harga.append(47000)
            elif pil_beef == 4:
                menu.append("T-Bone")
                harga.append(105000)
            elif pil_beef == 5:
                break
            else:
                print("Menu tidak tersedia")
        print("")
    elif pil == 2:
        while True:
            print("============================================")
            print("               CHICKEN MENU")
            print("============================================")
            print("1. Chicken Steak - Rp33.000")
            print("2. Crispy Chicken Steak - Rp38.000")
            print("3. Chicken Cordon Bleu - Rp38.000")
            print("4. Chicken Snichtzel - Rp38.000")
            print("5. Kembali")
            pil_chicken = int(input("Pilih menu : "))
            if pil_chicken == 1:
                menu.append("Chicken Steak")
                harga.append(33000)
            elif pil_chicken == 2:
                menu.append("Crispy Chicken Steak")
                harga.append(38000)
            elif pil_chicken == 3:
                menu.append("Chicken Cordon Bleu")
                harga.append(38000)
            elif pil_chicken == 4:
                menu.append("Chicken Snichtzel")
                harga.append(38000)
            elif pil_chicken == 5:
                break
            else:
                print("Menu tidak tersedia")
        print("")
    elif pil == 3:
        while True:
            print("============================================")
            print("               PASTA MENU")
            print("============================================")
            print("1. Bolognese - Rp30.000")
            print("2. Carbonara - Rp35.000")
            print("3. Aglio Olio - Rp30.000")
            print("4. Kembali")
            pil_pasta = int(input("Pilih menu : "))
            if pil_pasta == 1:
                menu.append("Bolognese")
                harga.append(30000)
            elif pil_pasta == 2:
                menu.append("Carbonara")
                harga.append(35000)
            elif pil_pasta == 3:
                menu.append("Aglio Olio")
                harga.append(30000)
            elif pil_pasta == 4:
                break
            else:
                print("Menu tidak tersedia")
        print("")
    elif pil == 4:
        while True:
            print("============================================")
            print("               DRINKS MENU")
            print("============================================")
            print("1. Ice Tea - Rp8.000")
            print("2. Hot Tea - Rp8.000")
            print("3. Ice Sweet Tea - Rp10.000")
            print("4. Hot Sweet Tea - Rp10.000")
            print("5. Ice Lemon Tea - Rp14.000")
            print("6. Hot Lemon Tea - Rp14.000")
            print("7. Ice Lychee Tea - Rp16.000")
            print("8. Coca Cola - Rp9.000")
            print("9. Sprite - Rp9.000")
            print("10. Fanta - Rp9.000")
            print("11. Happy Soda - Rp16.000")
            print("12. Mineral Water - Rp5.000")
            print("13. Kembali")
            pil_drinks = int(input("Pilih menu : "))
            if pil_drinks == 1:
                menu.append("Ice Tea")
                harga.append(8000)
            elif pil_drinks == 2:
                menu.append("Hot Tea")
                harga.append(8000)
            elif pil_drinks == 3:
                menu.append("Ice Sweet Tea")
                harga.append(10000)
            elif pil_drinks == 4:
                menu.append("Hot Sweet Tea")
                harga.append(10000)
            elif pil_drinks == 5:
                menu.append("Ice Lemon Tea")
                harga.append(14000)
            elif pil_drinks == 6:
                menu.append("Hot Lemon Tea")
                harga.append(14000)
            elif pil_drinks == 7:
                menu.append("Ice Lychee Tea")
                harga.append(16000)
            elif pil_drinks == 8:
                menu.append("Coca Cola")
                harga.append(9000)
            elif pil_drinks == 9:
                menu.append("Sprite")
                harga.append(9000)
            elif pil_drinks == 10:
                menu.append("Fanta")
                harga.append(9000)
            elif pil_drinks == 11:
                menu.append("Happy Soda")
                harga.append(16000)
            elif pil_drinks == 12:
                menu.append("Mineral Water")
                harga.append(5000)
            elif pil_drinks == 13:
                break
            else:
                print("Menu tidak tersedia")
        print("")
    elif pil == 5:
        break
    else:
        print("Pilihan tidak tersedia, ulangi!")

print("")
tampilkan_rincian_pemesanan()
total_harga = hitung_total_harga()
print(f"Total Harga         | Rp{total_harga:>6}")
while True:
    uang_bayar = input_uang_pembayaran()
    if uang_bayar >= total_harga:
        break
    else:
        tampilkan_keterangan_kurang()
kembali = hitung_kembali(uang_bayar, total_harga)
print(f"Kembali             | Rp{kembali:>6}")
print("")
tampilkan_terima_kasih()

tampilkan_metode_pembayaran(metode)
