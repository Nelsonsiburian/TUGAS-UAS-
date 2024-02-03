print("PROGRAM MENGHITUNG NILAI AKHIR MAHASISWA")

nama=input("Masukkan Nama :")
nim=input("Masukkan Nim :")
matkul=input("Masukkan Mata Kuliah :")
semester=input("Masukkan Semester :")
tugas=float(input("Masukkan Nilai Tugas :"))
uts=float(input("Masukkan Nilai Uts :"))
uas=float(input("Masukkan Nilai Uas :"))

na=(tugas * 0.2) + (uts * 0.4) + (uas * 0.4)

print("==========HASIL PERHITUNGAN==========")

print("Nama :",nama)
print("Nim :",nim)
print("Mata Kuliah :",matkul)
print("Semester :",semester)
print("Nilai Tugas :",tugas)
print("Nilai Uts :",uts)
print("Nilai Uas :",uas)
print("Nilai Akhir :",na)

if na >= 90:
    print("Grade : A")
elif na >= 80:
    print("Grade : B")
elif na >= 75:
    print("Grade : C")
elif na >= 50:
    print("Grade : D")
elif na <= 40:
    print("Grade : E")
if na >= 60:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")        
            

 