# Membuat variable nama barang
# Membuat variable harga barang
# Membuat variable persen harga
# Input nama barang
# Input harga barang
# Menghitung harga barang
# Harga barang * persen / 100
# Print harga barang bersama nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while(True):
    nama_barang = input("Nama barang :")
    harga_barang1 = int(input("Harga barang :"))
    persen = input("Masukan persen barang =")
    barang_terjual = int(input ('Masukan jumlah barang terjual'))

    keuntungan_persen = harga_barang1 * persen / 100
    harga_jual = harga_barang1 + keuntungan_persen

    # Menghitung modal
    modal = harga_barang1 + barang_terjual
    # Menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    # Menghitung laba
    laba = keuntungan_persen * barang_terjual
    # Menghitung laba keseluruhan
    laba_keseluruhan = laba_keseluruhan + laba

    print('Barang', nama_barang)
    print('Harga barang1', harga_barang1)
    print('Keuntungan per barang', keuntungan_persen)
    print('Dijual dengan harga', harga_jual)
    print('Terjual', barang_terjual)
    print('Modal', modal)
    print('Laba', laba)

    ApakahLanjut = input("Apakah ingin input barang lain? Y lanjut")
    if(ApakahLanjut != 'Y'):
        break

print('.............')
print('Modal keseluruhan', modal_keseluruhan)
print('Laba keseluruhan', laba_keseluruhan)
