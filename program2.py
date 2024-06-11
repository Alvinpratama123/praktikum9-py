def input_data_barang():
    barang_list = []
    n = int(input("Masukkan jumlah barang: "))
    
    for i in range(n):
        print(f"Masukkan data barang ke-{i+1}:")
        nama_barang = input("Nama: ")
        jenis_barang = input("Jenis: ")
        kode = input("Kode: ")
        harga = float(input("Harga: "))
        barang = {
            "nama_barang": nama_barang,
            "jenis": jenis_barang,
            "kode": kode,
            "harga": harga,
        }
        barang_list.append(barang)
        
    return barang_list

def tampilkan_data_barang(barang_list):
    if not barang_list:
        print("Tidak ada data barang.")
        return
    
    for i, barang in enumerate(barang_list):
        print(f"Barang ke-{i+1}:")
        print(f"Nama Barang: {barang['nama_barang']}")
        print(f"Jenis: {barang['jenis']}")
        print(f"Kode: {barang['kode']}")
        print(f"Harga: {barang['harga']}")

def tambah_barang(barang_list):
    print("Masukkan data barang baru:")
    nama_barang = input("Nama: ")
    jenis_barang = input("Jenis: ")
    kode = input("Kode: ")
    harga = float(input("Harga: "))
    barang = {
        "nama_barang": nama_barang,
        "jenis": jenis_barang,
        "kode": kode,
        "harga": harga,
    }
    barang_list.append(barang)
    print("Barang berhasil ditambahkan!")

def cari_kode_barang(barang_list):
    kode_cari = input("Masukkan kode barang yang dicari: ")
    for barang in barang_list:
        if barang["kode"] == kode_cari:
            print("Barang ditemukan:")
            print(f"Nama Barang: {barang['nama_barang']}")
            print(f"Jenis: {barang['jenis']}")
            print(f"Kode: {barang['kode']}")
            print(f"Harga: {barang['harga']}")
            return
    print("Barang dengan kode tersebut tidak ditemukan.")

def total_harga_barang(barang_list):
    total_harga = sum(barang["harga"] for barang in barang_list)
    print(f"Total harga semua barang: {total_harga}")

def menu():
    barang_list = []
    
    while True:
        print("\nMenu:")
        print("1. Input data barang")
        print("2. Tampilkan data barang")
        print("3. Tambah barang")
        print("4. Cari barang berdasarkan kode")
        print("5. Tampilkan total harga barang")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            barang_list = input_data_barang()
        elif pilihan == '2':
            tampilkan_data_barang(barang_list)
        elif pilihan == '3':
            tambah_barang(barang_list)
        elif pilihan == '4':
            cari_kode_barang(barang_list)
        elif pilihan == '5':
            total_harga_barang(barang_list)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Program utama
menu()
