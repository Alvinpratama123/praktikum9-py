def input_data_mahasiswa():
    mahasiswa_list = []
    n = int(input("masukan jumlah mahasiswa :"))
    
    for i in range (n):
        print(f"masukan data mahasiswa ke- {i+1}:")
        nama = input("nama: ")
        nim = input("nim: ")
        prodi = input("prodi: ")
        nilai = float(input("nilai :"))
        mahasiswa = {
            "nama":nama,
            "nim":nim,
            "prodi":prodi,
            "nilai":nilai,
        }
        mahasiswa_list.append(mahasiswa)
        
    return mahasiswa_list

#fungsi untuk menampilkan data mahasiswa 
def tampilkan_data_mahasiswa(mahasiswa_list):
    for i, mahasiswa in enumerate(mahasiswa_list):
        print(f"mahasiswa ke-{i+1}:")
        print(f"nama : {mahasiswa['nama']}")
        print(f"nim : {mahasiswa['nim']}")
        print(f"prodi : {mahasiswa['prodi']}")
        print(f"nilai : {mahasiswa['nilai']}")
        
        
#program  utama
mahasiswa_list = input_data_mahasiswa()
tampilkan_data_mahasiswa(mahasiswa_list)      
        
    