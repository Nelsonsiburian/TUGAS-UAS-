print('SELAMAT DATANG DI ATM ')
print('PILIH OPTION:')
print('1. check uang saya')
print('2. ambil uang saya')
print('3. tabung uang saya')
option=int(input('silahkan pilih option :'))
uang_kamu=300000
# if itu sebagai apa
if option==1:
    print('uang saya berjumlah Rp.300.000')
# elif itu sebagai apa
elif option==2:
    print('uang saya berjumlah Rp.300.000 mau ambil berapa')
    print('1. Rp.100.000')
    print('2. Rp.200.000')
    print('3. Rp.300.000')
    option2=int(input('option:'))
    if option2==1:
        hasil=uang_kamu-100000
        print('uang kamu sekarang berjumlah ',hasil)
    elif option2==2:
        hasil=uang_kamu-200000
        print('uang kamu sekarang berjumlah ',hasil)
    elif option2==3:
        hasil=uang_kamu-300000
        print('uang kamu sekarang berjumlah ',hasil)
    else:
        print('keyword anda salah, mohon ulang lagi!')
elif option==3:
    print('uang saya berjumlah Rp.300.000, mau tabung berapa?')
    option3=int(input('masukan jumlah uang'))
    hasil3=uang_kamu+option3
    print('jumlah uang kamu sekarang adalah',hasil3)
# else itu apa
else:
    print('pilihan anda salah, silahkan ulang lagi!!!')                
            
            
        
    
        