import pytest
import matematika

def test_pertambahan():
    output = matematika.pertambahan(2,4)
    assert output == 6

def test_perkalian():
    output = matematika.perkalian(2,4)
    assert output == 8
    
def test_pengurangan():
    output = matematika.pengurangan(2,4)
    assert output == -2