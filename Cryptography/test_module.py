from ciphers import Caesar, Playfair, Hill, Vignere, Vernam, AES, DES
from utils import *


def test_Caesar_Cipher_enc():
    plaint_text = """dimtnywkgcqrfxuvfmjdkujfyntgfsjxnjvippvv"""
    key = 3
    assert Caesar_Cipher_enc(plaint_text, key) == "glpwqbznjftuiaxyipmgnxmibqwjivmaqmylssyy"


def test_Playfair_enc():
    plaint_text = "rkesbbraumtqoejzccwobhnbymnqicpxipmxxpzw"
    key = "rats"
    assert (Playfair_enc(plaint_text, key) == "thfttzrabokbupdkvgdvuanvszhuolenwkukyptxvx")


# def  test_Hill_cipher():
def test_Vigenere_Cipher():
    plaint_text = "mdampuaf"
    key = "pie"
    assert (Vigenere_Cipher(plaint_text, key) == "blebxypn")


def test_vernam():
    plaint_text = "PXPTYRFJ"
    key = "SPARTANS"
    assert (vernam(plaint_text, key) == "hmpkrrsb")


def test_hill2by2():
    plaint_text = "VVMSQFGA"
    key = [[5, 17], [8, 3]]
    assert (Hill_cipher(plaint_text, key) == "uxcujnew")


def test_Des_enc():
    plaint_text = "FFFFFFFFFFFFFFFF"
    key = "0000000000000000"
    assert (Des_enc(plaint_text, key) == "355550b2150e2451")


def test_Des_dec():
    plaint_text = "355550b2150e2451"
    key = "0000000000000000"
    assert (Des_dec(plaint_text, key) == "ffffffffffffffff")


def test_AES_enc():
    plaint_text = "0123456789ABCDEF0123456789ABCDEF"
    key = "0123456789ABCDEF0123456789ABCDEF"
    assert (AES_enc(plaint_text, key) == "A1EE5608B33AF05470858608D1DE080F")


def test_AES_dec():
    plaint_text = "A1EE5608B33AF05470858608D1DE080F"
    key = "0123456789ABCDEF0123456789ABCDEF"
    assert (AES_dec(plaint_text, key) == "0123456789ABCDEF0123456789ABCDEF")


def test_ceaserClass():
    plaint_text = """dimtnywkgcqrfxuvfmjdkujfyntgfsjxnjvippvv"""
    key = 3
    assert Caesar(key).encrypt(plaint_text) == "glpwqbznjftuiaxyipmgnxmibqwjivmaqmylssyy"


def test_PlayfairClass():
    plaint_text = """rkesbbraumtqoejzccwobhnbymnqicpxipmxxpzw"""
    key = 'rats'
    assert Playfair(key).encrypt(plaint_text) == "thfttzrabokbupdkvgdvuanvszhuolenwkukyptxvx"


def test_HillClass():
    plaint_text = """VVMSQFGA"""
    key = [[5, 17], [8, 3]]
    assert Hill(key).encrypt(plaint_text) == "uxcujnew"


def test_VignereClass():
    plaint_text = """mdampuaf"""
    key = "pie"
    assert Vignere(key).encrypt(plaint_text) == "blebxypn"


def test_VernamClass():
    plaint_text = """PXPTYRFJ"""
    key = "SPARTANS"
    assert Vernam(key).encrypt(plaint_text) == "hmpkrrsb"


def test_DesClass_enc():
    plaint_text = "FFFFFFFFFFFFFFFF"
    key = "0000000000000000"
    assert (DES(key).encrypt(plaint_text) == "355550b2150e2451")


def test_DesClass_dec():
    plaint_text = "355550b2150e2451"
    key = "0000000000000000"
    assert (DES(key).decrypt(plaint_text) == "ffffffffffffffff")


def test_AESClass_enc():
    plaint_text = "0123456789ABCDEF0123456789ABCDEF"
    key = "0123456789ABCDEF0123456789ABCDEF"
    assert (AES(key).encrypt(plaint_text) == "A1EE5608B33AF05470858608D1DE080F")


def test_AESClass_dec():
    plaint_text = "A1EE5608B33AF05470858608D1DE080F"
    key = "0123456789ABCDEF0123456789ABCDEF"
    assert (AES(key).decrypt(plaint_text) == "0123456789ABCDEF0123456789ABCDEF")


if __name__ == '__main__':
    test_Caesar_Cipher_enc()
    test_Playfair_enc()
    test_Vigenere_Cipher()
    test_vernam()
    test_hill2by2()
    test_ceaserClass()
    test_PlayfairClass()
    test_HillClass()
    test_VignereClass()
    test_VernamClass()
    test_Des_enc()
    test_Des_dec()
    test_AES_enc()
    test_AES_dec()
    test_DesClass_enc()
    test_DesClass_dec()
    test_AESClass_enc()
    test_AESClass_dec()

# functions = {
#     1: Caesar_Cipher_enc,
#     2: Playfair_enc,
#     3: Hill_cipher,
#     4: Vigenere_Cipher,
#     5: vernam
# }
# input_files = {
#     1: 'Caesar/caesar_plain.txt',
#     2: 'PlayFair/playfair_plain.txt',
#     4: 'Vigenere/vigenere_plain.txt',
#     5: 'Vernam/vernam_plain.txt'
# }
# Output_files = {
#     1: 'Caesar/caesar_Output.txt',
#     2: 'PlayFair/playfair_Output.txt',
#     4: 'Vigenere/vigenere_Output.txt',
#     5: 'Vernam/vernam_Output.txt'
# }
#
#
# def read_files():
#     print('For Caesar_Cipher insert: 1 ')
#     print('For Play_Fair_Cipher insert: 2 ')
#     print('For Hill_Cipher insert: 3 ')
#     print('For Vigenere_Cipher insert: 4 ')
#     print('For Vernam_Cipher insert: 5 ')
#     Choice = int(input('your choice : '))
#     if Choice == 1:
#         key = int(input('enter you key as ineger : '))  # '12'
#     elif Choice == 2:
#         key = input('enter your key: ')
#         pass
#     elif Choice == 3:
#         dim = int(input('enter you matrix dimensions as one intger: '))
#         if dim == 2:
#             input_files[3] = 'Hill/hill_plain_2x2.txt'
#             Output_files[3] = 'Hill/hill_Output_2x2.txt'
#         if dim == 3:
#             input_files[3] = 'Hill/hill_plain_3x3.txt'
#             Output_files[3] = 'Hill/hill_Output_3x3.txt'
#         key = []
#         for i in range(dim):
#             row = []
#             for j in range(dim):
#                 row.append(int(input(f'row {i} column {j}: ')))
#             key.append(row)
#     elif Choice == 4:
#         key = input('enter the key text : ')
#         type = int(input('for auto enter 1 else for repeate mode'))
#
#     elif Choice == 5:
#         key = input('enter the key text : ')
#
#     txtfiles = []
#     for file in glob.glob("./Input Files/" + input_files[Choice]):
#         txtfiles.append(file)
#
#     for i in txtfiles:
#
#         file1 = open(i, 'r')
#         lines = ''
#
#         while True:
#             line = file1.readline()
#             line = line[:-1]
#             if not line:
#                 break
#
#             if Choice == 1 or Choice == 2 or Choice == 3 or Choice == 5:
#                 lines += functions[Choice](line, key) + '\n'
#             else:
#                 lines += functions[Choice](line, key, Auto=type) + '\n'
#
#             print("{}".format(line.strip()))
#
#         file1.close()
#
#         file2 = open("./Input Files/" + Output_files[Choice], 'w')
#         file2.writelines((lines))
#         file2.close()
#
#
#
# def main():
#     Choice = 6
#     while (Choice == 6):
#         print('For reading the  plaintext from the input files insert : 0 ')
#         print('For Caesar_Cipher insert: 1 ')
#         print('For Play_Fair_Cipher insert: 2 ')
#         print('For Hill_Cipher insert: 3 ')
#         print('For Vigenere_Cipher insert: 4 ')
#         print('For Vernam_Cipher insert: 5 ')
#         print('For end insert: 6 ')
#         Choice = int(input('your choice: '))
#         if Choice == 0:
#             read_files()
#         elif Choice == 1:
#             plain_text = input('enter your text: ').lower()  # 'dimtnywkgcqrfxuvfmjdkujfyntgfsjxnjvippvv'
#             key = int(input('enter you key as ineger : '))  # '12'
#             cipher_text = Caesar_Cipher_enc(plain_text, int(key))
#             print('the cipher text is : ', cipher_text)
#
#         elif Choice == 2:
#             plain_text = input('enter your text: ').lower()
#             key = input('enter your key: ').lower()
#             cipher_text = functions[2](plain_text, key)
#             print('the cipher text is : ', cipher_text)
#
#         elif Choice == 3:
#             plain_text = input('enter your text: ').lower()  # 'dimtnywkgcqrfxuvfmjdkujfyntgfsjxnjvippvv'
#             dim = int(input('enter you matrix dimensions as one intger: '))
#             key = []
#             for i in range(dim):
#                 row = []
#                 for j in range(dim):
#                     row.append(int(input(f'row {i} column {j}: ')))
#                 key.append(row)
#             cipher_text = Hill_cipher(plain_text, key)
#             print('the cipher text is : ', cipher_text)
#
#         elif Choice == 4:
#             plain_text = input('enter your text: ').lower()
#             key = input('enter the key text : ').lower()
#             type = int(input('for auto enter 1 else for repeate mode '))
#             if type == 1:
#                 cipher_text = Vigenere_Cipher(plain_text, key, Auto=True)
#             else:
#                 cipher_text = Vigenere_Cipher(plain_text, key, Auto=False)
#             print('the cipher text is : ', cipher_text)
#
#         elif Choice == 5:
#             plain_text = input('enter your text: ').lower()
#             key = input('enter the key text : ').lower()
#
#             cipher_text = vernam(plain_text, key)
#             print('the cipher text is : ', cipher_text)
#
#         else:
#             print('sorry! try again with valid number.')
#
#
# if __name__ == '__main__':
#     exit = 0
#     while exit == 0:
#         main()
#         exit = int(input('to exit enter 1 else for continue: '))
