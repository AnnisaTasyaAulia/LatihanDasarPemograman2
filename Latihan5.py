# Deskriftif
# membuat variabel nama barang
# membuat variabel harga barang 
# membuat variabel persen harga
# input nama barang
# input harga barang 
# menghitung harga barang
# harga barang * persen / 100
# print harga barang bersama nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input("Nama barang                    : ")
    harga_barang1 = int (input("Harga barang                   : Rp. "))
    persen = int (input('Persen barang                  : '))
    barang_terjual = int(input('Jumlah barang terjual          : '))

    keuntungan_persen = harga_barang1 * persen/ 100
    harga_jual = harga_barang1 + keuntungan_persen 

    # Menghitung modal
    modal = harga_barang1 + barang_terjual
    print(nama_barang,'dijual dengan harga : Rp. ',harga_jual)
    modal_keseluruhan = modal_keseluruhan + modal

    # Menghitung laba
    laba = keuntungan_persen * barang_terjual
    # Menghitung laba keseluruhan
    laba_keseluruhan = laba_keseluruhan + laba

    print('Barang                :', nama_barang)
    print('Harga barang          : Rp. ', harga_barang1)
    print('Keuntungan per barang : Rp. ', keuntungan_persen)
    print('Dijual dengan harga   : Rp. ', harga_jual)
    print('Terjual               :', barang_terjual)
    print('Modal                 : Rp. ', modal)
    print('Laba                  : Rp. ', laba)

    ApakahLanjut = input("Apakah ingin input barang lain? Y lanjut : ")
    if(ApakahLanjut != 'Y'):
        break

print('=============== Total ===============')
print('Modal keseluruhan    : Rp. ', modal_keseluruhan)
print('Laba keseluruhan     : Rp. ', laba_keseluruhan)
