# Membuat variable nama barang
# Membuat variable harga barang
# Membuat variable persen harga
# Input nama barang
# Input harga barang
# Menghitung harga barang
# Harga barang * persen / 100
# Print harga barang bersama nama barang

while(True):

    nama_barang = input("Nama barang :")
    harga_barang1 = int(input("Harga barang :"))
    persen = input("masukan persen barang =")
    harga_keuntungan = int(harga_barang1) * int(persen) / 100
    harga_jual = int(harga_barang1) + harga_keuntungan
    print(nama_barang, "Dijual dengan : ", harga_jual)

    ApakahLanjut = input("Apakah ingin input barang lain? Y lanjut")
    if(ApakahLanjut != 'Y'):
        break
