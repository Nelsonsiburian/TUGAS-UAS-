print("Konversi Suhu")
print("1. Celcius")
print("2. Farenheit")
print("3. Reamur")
print("4. Kelvin")

suhu = int(input("Masukkan  Opsi Yang Ingin Dipilih : "))

if(suhu == 1):
    print("1. Celcius ke Farenheit")
    print("2. Celcius ke Reamur")
    print("2. Celcius ke Kelvin")
    
    suhu_celcius = int(input("Masukkan Opsi Yang Ingin Dipilih Untuk Konversi Suhu"))
    
    if(suhu_celcius == 1):
        print("Celcius Ke Farenheit")
        
        a = float(input("Masukkan angka  derajat : ... "))
        print("Suhu Dalam celcius ialah :",a,"C")
        
        farenheit =(9/5 * a) + 32
        
        print("Suhu dalam Farenheit adalah :",farenheit,"F")
        
        
    elif(suhu_celcius == 2):
        print("Celcius ke Reamur")
        
        a = float(input("Masukkan angka derajat : ... "))
        print("Suhu dalam celcius ialah :",a,"c")
        
        reamur = (4/5) * a
        print("Suhu dalam Reamur adalah :",reamur,("R"))
    
        
    elif(suhu_celcius == 3):
        print("Celcius ke Kelvin")
        
        a= float(input("Masukkan angka derajat : ... "))  
        print("Suhu dalam celcius ialah :",a,"c")
        
        kelvin = a + 273
        print("Suhu dalam Kelvin adalah :",kelvin,"K")  
        
        
if (suhu == 2):
    print("1. Farenheit ke Reamur") 
    print("2. Farenheit ke Kelvin")
    print("3. Farenheit ke Celcius")    
    
    suhu_farenheit = int(input("Masukkan Opsi Yang ingin dipilih untuk konversi suhu"))
    
    if(suhu_farenheit == 1):
        print("Farenheit ke Reamur")
        a = float(input("Masukan angka derajat : "))
        print("Suhu dalam farenheit adalah :",a,"F")
        
        Reamur = (4/5) * (a - 32)  
        print("Suhu dalam reamur adalah :",reamur,"R")
        
    elif(suhu_farenheit == 2):
        print("Farenheit ke Kelvin")
        
        a = float(input("Masukan angka derajat : "))
        print("Suhu dalam farenheit ialah :",a,"F")
        
        kelvin = ((5/9) * (a - 32)) + 273
        print("Suhu dalam kelvin adalah :",kelvin,"K")
        
    elif(suhu_farenheit == 3):
        print("Farenheit ke Celcius")
        
        a= float(input("masukan angka derajat : "))
        print("Suhu dalam farenheit ialah :",a,"F")
        
        celcius = 5/9 * (a - 32)
        print("Suhu dalam kelvin adalah :",kelvin,"k")  
        
        
if(suhu == 3):
    print("1. Reamur ke kelvin")
    print("2. Reamur ke Celcius")
    print("3. Reamur ke Farenheit")
    
    suhu_reamur = int(input("Masukkan Opsi yang ingin sipilih : "))
    if(suhu_reamur == 1):
        print("Reamur ke kelvin")
        
        a = float(input("Masukkan angka derajat : "))
        print("Suhu dalam reamur ialah :",a,"R")
        
        kelvin = ((5/4) * a) + 273
        print("Suhu dalam kelvin adlah :",kelvin,"K")
        
    if(suhu_reamur == 2):
        print("Reamur ke Celcius")
        
        a = float(input("Maukan angka derajat : "))  
        print("suhu dalam Reamur ialah :",a,"R")
        
        celcius = a - (5/4) * a
        print("Suhu dalam selcius adalah :",celcius,"C")
        
    if(suhu_reamur == 3):
        print("Reamur ke Farenheit")
        
        a = float(input("Masukan angka derajat : "))
        print("Suhu dalam Reamur ialah :",a,"R")
        
        farenheit = ((9/4) * a) + 32
        print("suhu dalam farenheit adalah :",farenheit,"F")
        
if(suhu == 4):
    print("1. Kelvin ke Celcius")
    print("2. Kelvin ke Farenheit")
    print("3. Kelvin ke Reamur") 
    
    suhu_kelvin = int(input("Masukkan Opsi yang ingin dipilih : "))
    
    if(suhu_kelvin == 1):
        print("Kelvin ke Celcius")
        
        a = float(input("Masukkan angka derajat : "))
        print("Suhu dalam Kelvin ialah :",a,"K")
        
        celcius = a - 273
        print("suhu dalam celcius adalah :",celcius,"C") 
        
    if(suhu_kelvin == 2):
        print("Kelvin Ke Farenheit")
        
        a = float(input("Masukkan angka derajat : "))
        print("Suhu dalam kelvin ialah :",a,"K")   
        
        farenheit = (9/5 * (a - 273)) + 32
        print("Suhu dalam Farenheit adalah :",farenheit,"F")
        
    if(suhu_kelvin == 3):
        print("Kelvin ke Reamur")
        
        a = float(input("Masukkan angka derajat : "))
        print("suhu dalam kelvin ialah :",a,"k")
        
        reamur = (9/5 * (a -273))
        print("Suhu dalam reamur adalah :",reamur,"R")               
      
         
         
    
    