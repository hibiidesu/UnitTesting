import biodata
import pytest

def test_add_biodata():
    data = biodata.biodata_mahasiswa()
    assert data["NAMA"] == "Nabil Falih Khairullah"
    assert data["TELEPON"] == "081231231231"
    assert data["ALAMAT"] == "Beji"
    assert data["EMAIL"] == "Nabil@mail.com"
    assert data["UMUR"] == "18 tahun"
    assert data["HOBI"] == "Olahraga"

def test_add_nama():
    nama = biodata.add_nama("nabil falih khairullah")
    assert nama == "Nabil Falih Khairullah"
    assert nama.istitle() == True

def test_add_telepon():
    telepon = biodata.add_telepon(+6281231231231)
    assert isinstance(telepon, str) == True

def test_add_umur():
    umur = biodata.add_umur(18)
    assert umur == "18 tahun"
