"""
Sandbox IT HSI - Django
Tugas Evaluasi Pekanan 4 - Membuat Pencarian Siswa Yang Lulus SNBT 2025
Materi yang digunakan:
1. String
2. Condition
3. Looping
4. List
5. Dictionary
6. Fungsi

Sumber = https://smakartika81.sch.id/index.php/berita-sekolah/item/261-siswa-lulus-snbt-2025.html
Mafza Rizki Tabina - S1 Sastra Jerman - Universitas Indonesia (UI)
Rafa Naila Latifa - S1 Farmasi - Universitas Indonesia (UI)
Nayla Nathania Setiadi - S1 Psikologi - UIN Jakarta
Anisa Siti Nur Azizah - S1 Ilmu Ekonomi - UIN Jakarta
Adilah Salsabila Djalante - S1 Pendidikan IPS - Universitas Negeri Makassar
Inaya Maulida - S1 Akuntansi - UPN Veteran Jakarta
Rosinta Helen Grasia - S1 Pendidikan Bahasa Indonesia - Universitas Lampung (UNILA)
Aditya Nugraha - S1 Ekonomi Pembangunan - UPN Veteran Jakarta
Clarissa Angelina - S1 Kedokteran - Universitas Palangkaraya
Aulia Nur Fadhillah - S1 Kimia - Universitas Negeri Jakarta (UNJ)
Edwardus Jonathan - S1 Sistem Informasi - UPN Veteran Jakarta
Muhammad Avip - S1 Matematika - Universitas Sebelas Maret (Surakarta)
Badriansyah - S1 Sains Atmosfir & Keplanetan - Institut Teknologi Sumatera (ITERA)
Samuel Bintang Hopkins - S1 Teknik Kelautan - Institut Teknologi Sumatera (ITERA)
Haffan Yusoef - S1 Fisika - Universitas Udayana
Syalwa Putri Shakina - S1 Kesehatan Masyarakat - UPN Veteran Jakarta
Qonita Khairunisa - S1 Sains Informasi - UPN Veteran Jakarta
Andika Rama Setya - S1 Pendidikan Geografi - Universitas Negeri Surabaya (UNESA)
Amel Oktavia Ramadhani - S1 Biologi - UIN Jakarta
Hanan Khairunnisa - S1 Ilmu Politik - UPN Veteran Jakarta
Sekar Ayudyah Syabani - D3 Sistem Informasi - UN Veteran Jakarta
Putri Mufida - S1 Akuntansi - Universitas Sultan Ageng Tirtayasa (UNTIRTA)
Amalia Nur Rizki - D3 Administrasi Bisnis - Politeknik Negeri Jakarta (PNJ)
"""


import os

"""
Lengkapi fungsi dibawah
1. Inisialiasi data
Hints
- Gunakan string literal
"""
def init_str_data_siswa() -> str:
    str_data_siswa = """Mafza Rizki Tabina - S1 Sastra Jerman - Universitas Indonesia (UI)
Rafa Naila Latifa - S1 Farmasi - Universitas Indonesia (UI)
Nayla Nathania Setiadi - S1 Psikologi - UIN Jakarta
Anisa Siti Nur Azizah - S1 Ilmu Ekonomi - UIN Jakarta
Adilah Salsabila Djalante - S1 Pendidikan IPS - Universitas Negeri Makassar
Inaya Maulida - S1 Akuntansi - UPN Veteran Jakarta
Rosinta Helen Grasia - S1 Pendidikan Bahasa Indonesia - Universitas Lampung (UNILA)
Aditya Nugraha - S1 Ekonomi Pembangunan - UPN Veteran Jakarta
Clarissa Angelina - S1 Kedokteran - Universitas Palangkaraya
Aulia Nur Fadhillah - S1 Kimia - Universitas Negeri Jakarta (UNJ)
Edwardus Jonathan - S1 Sistem Informasi - UPN Veteran Jakarta
Muhammad Avip - S1 Matematika - Universitas Sebelas Maret (Surakarta)
Badriansyah - S1 Sains Atmosfir & Keplanetan - Institut Teknologi Sumatera (ITERA)
Samuel Bintang Hopkins - S1 Teknik Kelautan - Institut Teknologi Sumatera (ITERA)
Haffan Yusoef - S1 Fisika - Universitas Udayana
Syalwa Putri Shakina - S1 Kesehatan Masyarakat - UPN Veteran Jakarta
Qonita Khairunisa - S1 Sains Informasi - UPN Veteran Jakarta
Andika Rama Setya - S1 Pendidikan Geografi - Universitas Negeri Surabaya (UNESA)
Amel Oktavia Ramadhani - S1 Biologi - UIN Jakarta
Hanan Khairunnisa - S1 Ilmu Politik - UPN Veteran Jakarta
Sekar Ayudyah Syabani - D3 Sistem Informasi - UN Veteran Jakarta
Putri Mufida - S1 Akuntansi - Universitas Sultan Ageng Tirtayasa (UNTIRTA)
Amalia Nur Rizki - D3 Administrasi Bisnis - Politeknik Negeri Jakarta (PNJ)"""
    
    ##1. Lengkapi code untuk inisialisasi data

    return str_data_siswa


"""
Lengkapi fungsi dibawah
2. Membersihkan data
Hints
- Split string menggunakan karakter new line
- Bersihkan hasil split dengan mengecek panjang, data yang bersih adalah data dengan panjang > 0
"""
def buat_list_siswa(data_siswa:str) -> list:
    ## 2a. Lengkapi code untuk split
    list_kotor = data_siswa.split("\n")
    list_data_siswa = [i for i in list_kotor if len(i) > 0]  # Cleaning the data
    return list_data_siswa
    ## 2b. Lengkapi code untuk for

    return list_data_siswa


"""
Lengkapi fungsi dibawah
3. Membuat multikeys dictionary yang berisi
- nip (key)
- nama
- jurusan
- universitas

Hints
- Split string menggunakan karakter " - "
- Buat dictionary siswa
- Buat dictionary data siswa
"""
def buat_dict_siswa(list_data_siswa:list) -> dict:
    dict_data_siswa = {}
    angka = 1
    for i in list_data_siswa:
        nip = "S" + f"{angka:02}"
        data_siswa = i.split(" - ")
        nama = data_siswa[0]
        jurusan = data_siswa[1]
        universitas = data_siswa[2]
        siswa = {
            'nama': nama,
            'jurusan': jurusan,
            'universitas': universitas
        
       
            ## 3a. Lengkapi code untuk membuat dictionary siswa
        }
        dict_data_siswa[nip] = siswa
        angka += 1
    return dict_data_siswa
        ## 3b. Lengkapi code untuk menambahkan siswa baru ke dictionary data siswa
        ## 3c. Lengkapi code untuk iterasi angka sehingga nip bertambah dari 1, 2, 3 dan seterusnya
    
    return dict_data_siswa

"""
Lengkapi fungsi dibawah
4. Menambahkan informasi ke dictionary data siswa
- kota
- propinsi

Hints
- Iterasi tiap siswa
- Gunakan universitas untuk menentukan nama kota dan propinsi
"""
def tambah_info(dict_data_siswa:dict) -> dict:
   dict_data_siswa_baru = {}
   for siswa in dict_data_siswa:
        nip = siswa
        nama = dict_data_siswa[nip]['nama']
        jurusan = dict_data_siswa[nip]['jurusan']
        universitas = dict_data_siswa[nip]['universitas']
        kota = "Jakarta" if "Jakarta" in universitas else ""
        propinsi = "DKI Jakarta" if "Jakarta" in universitas else "Lainnya"
        ## 4a. Lengkapi code untuk menentukan kota dan propinsi yang lain
        
        siswa_baru = {
            'nama': nama,
            'jurusan': jurusan,
            'universitas': universitas,
            'kota': kota,
            'propinsi': propinsi
            ## 4b. Lengkapi code untuk menambahkan kota dan propinsi ke dictionary siswa
        }
   dict_data_siswa_baru[nip] = siswa_baru
        ## 4c. Lengkapi code untuk menambahkan siswa ke dictionary data siswa baru

   return dict_data_siswa_baru


"""
Lengkapi fungsi dibawah
5. Mencari data siswa menggunakan salah satu keyword dibawah
- jurusan
- nama
- kota
- propinsi

Hints
- Iterasi tiap siswa
- Gunakan operasi dari string
"""
def cari_siswa(*args,**kwargs) -> dict:
    dict_hasil_cari = {}
    kata_kunci = args[1]

    if kwargs['kolom'] == "jurusan":
        for siswa in args[0]:
            nip = siswa
            jurusan = args[0][nip]['jurusan']

            if kata_kunci in jurusan:
                nama = args[0][nip]['nama']
                universitas = args[0][nip]['universitas']
                kota = args[0][nip]['kota']
                propinsi = args[0][nip]['propinsi']

                siswa_baru = {
                    'nama':nama,
                    'jurusan':jurusan,
                    'universitas':universitas,
                    'kota':kota,
                    'propinsi':propinsi
                }

                dict_hasil_cari.update({nip:siswa_baru})
    elif kwargs['kolom'] == "kota":
        ## 5a. Lengkapi code untuk keyword kota
        dict_hasil_cari

    elif kwargs['kolom'] == "propinsi":
        # 5b. Lengkapi code untuk keyword propinsi
        dict_hasil_cari

    elif kwargs['kolom'] == "nama":
        # 5c. Lengkapi code untuk keyword nama
        dict_hasil_cari
    
        
    return dict_hasil_cari

            
def print_hasil_pencarian(dict_hasil_cari:dict):
    if len(dict_hasil_cari) > 0:
        str_nip = "NIP"
        str_nama = "Nama"
        str_jurusan = "Jurusan"
        str_universitas = "Universitas"
        str_kota = "Kota"
        str_propinsi = "Propinsi"
        print("-"*162)
        print(f"| {str_nip:3} | {str_nama:<30} | {str_jurusan:30} | {str_universitas:45} | {str_kota:15} | {str_propinsi:20} |")
        print("-"*162)
        for siswa in dict_hasil_cari:
            nip = siswa
            nama = dict_hasil_cari[nip]['nama']
            jurusan = dict_hasil_cari[nip]['jurusan']
            universitas = dict_hasil_cari[nip]['universitas']
            kota = dict_hasil_cari[nip]['kota']
            propinsi = dict_hasil_cari[nip]['propinsi']
            print(f"| {nip:3} | {nama:<30} | {jurusan:30} | {universitas:45} | {kota:15} | {propinsi:20} |")
        
        print("-"*162)
    else:
        print("Siswa tidak ditemukan, Silahkan gunakan kata kunci lain")


"""
Lengkapi fungsi dibawah
6. Membuat fungsi main sebagai orkestrator

Hints
- Gunakan input
"""
if __name__ == '__main__':
    sistem_operasi = os.name
    str_data_siswa = ""
    str_data_siswa = init_str_data_siswa()
    list_data_siswa = buat_list_siswa(str_data_siswa)
    dict_data_siswa = buat_dict_siswa(list_data_siswa)
    dict_data_siswa_baru = tambah_info(dict_data_siswa)

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        
        print("SELAMAT DATANG DI SMA KARTIKA VIII-1")
        print("PENCARIAN SISWA LULUS SNBT 2025")
        print("===============================")

        print(f"1. Cari Berdasarkan Nama")
        print(f"2. Cari Berdasarkan Jurusan")
        print(f"3. Cari Berdasarkan Kota")
        print(f"4. Cari Berdasarkan Propinsi")
        print(f"5. Tampilkan semua Siswa\n")

        user_option = input("Masukan option: ")
        print("\n=========================\n")

        match user_option:
            case "1":
                nama = input("Masukan Nama Siswa: ")
                dict_hasil_cari = cari_siswa(dict_data_siswa_baru,nama,kolom="nama")
                print_hasil_pencarian(dict_hasil_cari)
            case "2":
                ## 6a. Lengkapi code untuk pencarian berdasarkan jurusan
                print()
            case "3":
                ## 6b. Lengkapi code untuk pencarian berdasarkan kota
                print()
            case "4":
                ## 6c. Lengkapi code untuk pencarian berdasarkan propinsi
                print()
            case "5":
                ## 6d. Lengkapi code untuk menampilkan semua siswa
                print()
        
        print("\n=========================\n")
        is_done = input("Apakah selesai (y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Selesai")
