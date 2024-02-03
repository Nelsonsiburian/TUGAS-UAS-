print("==========TOKO FUSION==========" )
Pembeli = input("Nama Pembeli : ")
print("Nama Pembeli")
# def itu sebagai apa
def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n==========MENU MAKANAN==========")
    print("1. Nasi Goreng - Rp.15000,00")
    print("2. Mie Goreng - Rp.15000,00")
    print("3. Ayam Bakar - Rp.20000,00")
    print("4. Ayam Goreng - Rp20000,00")
    print("5. Ikan Bakar - Rp.25000,00")
    print("6. Ikan Goreng - Rp.25000,00")
    nomor = int(input("MASUKKAN PILIHAN 1/2/3/4/5/6 : "))
    porsi = int(input("Berapa Porsi : "))
    
    if nomor == 1:
        totalmakanan = porsi * 15000
        print(porsi,'Nasi Goreng = Rp.',totalmakanan)
        makan=("Nasi Goreng")
    elif nomor == 2:
        totalmakanan = porsi * 15000
        print(porsi,'Mie Goreng = Rp.',totalmakanan)
        makan=("Mie Goreng")
    elif nomor == 3:
        totalmakanan = porsi * 20000
        print(porsi,'Ayam Bakar = Rp.',totalmakanan)
        makan=("Ayam Bakar")
    elif nomor == 4:
        totalmakanan = porsi * 20000
        print(porsi,'Ayam Goreng = Rp.',totalmakanan)
        makan=("Ayam Goreng")
    elif nomor == 5:
        totalmakanan = porsi * 25000
        print(porsi,'Ikan Bakar = Rp.',totalmakanan)
        makan=("Ikan Bakar")
    elif nomor == 6:
        totalmakanan = porsi * 25000
        print(porsi,'Ikan Goreng = Rp.',totalmakanan)
        makan=("Ikan Goreng")
    else:
        print("Pilihan tidak ada di daftar menu\nsilahkan pilih kembali !!!")
        makanan()
        
def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n==========MENU MINUMAN==========")
    print("1. Es Teh Manis - Rp.5000,00")
    print("2. Kopi - Rp.5000,00")
    print("3. Es Jeruk - Rp.10000,00")
    print("4. Es Lemon - Rp.10000,00")
    print("5. Jus Mangga - Rp.15000,00")
    nomor = int(input("MASUKKAN PILIHAN 1/2/3/4/5 : "))
    gelas = int(input("Berapa gelas : "))
    
    if nomor == 1:
        totalminuman = gelas * 5000
        print(gelas,'Es Teh Manis = Rp.',totalminuman)
        minum=("Es Teh Manis")
    elif nomor == 2:
        totalminuman = gelas * 5000
        print(gelas,'Kopi = Rp.',totalminuman)
        minum=("Mie Goreng")
    elif nomor == 3:
        totalminuman = gelas * 10000
        print(gelas,'Es Jeruk = Rp.',totalminuman)
        minum=("Es Jeruk")
    elif nomor == 4:
        totalminuman = gelas * 10000
        print(gelas,'Es Lemon  = Rp.',totalminuman)
        minum=("Es Lemon")
    elif nomor == 5:
        totalminuman = gelas * 15000
        print(gelas,'Jus Mangga = Rp.',totalminuman)
        minum=("Jus mangga")
    else:
        print("Pilihan tidak ada di daftar menu\nsilahkan pilih kembali !!!")
        minuman() 
          
makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("/ntotal yang harus di bayar : ",total_semua)
uang = int(input("uang tunai pembeli : Rp."))
kembalian = int(uang - total_semua)
print("kembalian :", kembalian)
# \t kegunaan ya apa
print("\n==========S T U K B E L I==========")
print("Nama\t\t:,pembeli")
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")") 
print("\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t:Rp.",total_semua)
print("Dibayar\t\t:Rp.",uang)
print("Kembalian\t\t:Rp.",kembalian)

print("====================")
print("====================")