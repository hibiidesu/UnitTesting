
def biodata_mahasiswa():
    data = {"NAMA": "Nabil Falih Khairullah",
            "TELEPON": "081231231231",
            "ALAMAT": "Beji",
            "EMAIL": "Nabil@mail.com",
            "UMUR": "18 tahun",
            "HOBI": "Olahraga",}
    return data

def add_mahasiswa():
    return
#nama
def add_nama(nama):
    title_nama = nama.title()
    return title_nama

#telepon
def add_telepon(telepon):
    str_telepon = str(telepon)
    return str_telepon

#alamat
def add_alamat(alamat):
    return alamat

#email
def add_email(email):
    return email

#umur
def add_umur(umur):
    str_umur = str(umur)
    return str_umur + " tahun"

#hobi
def add_hobi(hobi):
    return hobi