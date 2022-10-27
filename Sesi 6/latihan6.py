# Tugas 6

print('===== Program Grade Nilai =====')
input('Nama Mahsiswa : ')
nilai =int(input('Masukan nilai : '))

if (nilai >= 90 and nilai <= 100) :
    Grade = 'A'
    Predikat = 'Selamat, Anda Mendapatkan Nilai Terbaik'
elif (nilai >= 80 and nilai <= 90) :
    Grade = 'B'
    Predikat = 'Sangat Memuaskan'
elif (nilai >= 70 and nilai <= 79) :
    Grade = 'C'
    Predikat = 'Memuaskan'
elif (nilai >= 60 and nilai <= 69) :
    Grade = 'D'
    Predikat = 'Tidak Memuaskan'
elif (nilai >= 0 and nilai <= 59) :
    Grade = 'E'
    Predikat = 'Tidak Lulus'
else :
    print ('Eror')

print ('Nilai anda : ', nilai)
print ('Grade : ', Grade)
print ('Predikat : ', Predikat)
print (type (nilai))

