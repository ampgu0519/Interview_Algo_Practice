from Codewars.SimpleFun305.typist import typist

def test_typist_all_lower():
    assert typist('aa') == 2

def test_typist_all_upper():
    assert typist("AA") == 3

def test_typist_upper_lower_start_lower():
    assert typist('aAa') == 5

def test_typist_upper_lower_start_upper():
    assert typist('AaA') == 6

def test_typist_longer_word_all_lower():
    assert typist('abcdefghijklmnopqrstuvwxyz') == 26

def test_typist_longer_word_all_upper():
    assert typist('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 27

def test_typist_longer_word_upper_lower_start_upper():
    assert typist('AbCdEfGhIjKlMnOpQrStUvWxYz') == 52

def test_typist_longer_word_upper_lower_start_lower():
    assert typist('aBcDeFgHiJkLmNoPqRsTuVwXyZ') == 51

