"""
Name : Girgis micheal Fawzy
Date : 1 / 2 / 2021
"""
import glob
import string
from collections import OrderedDict

from .CONSTANTS.AES_CONSTANTS import *
from .CONSTANTS.DES_CONSTANTS import *


def reshape(list1, h, w):
    mat = []
    for i in range(h):
        mat.append(list1[i * w:i * w + w])
    return mat

def matmul(matrix1, matrix2):
    res = [[0 for x in range(len(matrix2[0]))] for y in range(len(matrix1))]

    # explicit for loops
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res


def mod(list1):
    result = []
    for i in range(len(list1)):
        l = []
        for j in range(len(list1[0])):
            l.append((list1[i][j]) % 26)
        result.append(l)
    return result


def flatten(mat):
    l = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            l.append(mat[i][j])
    return l


def transpose(mat):
    mat_T = []
    for i in range(len(mat[0])):
        l = []
        for j in range(len(mat)):
            l.append(mat[j][i])
        mat_T.append(l)
    return mat_T

def MAT_creation(key):
    assert isinstance(key, str)
    key = key.replace(" ", "")
    alphabet = list(string.ascii_lowercase)
    alphabet.remove('j')
    key = list(key.lower())
    mat = list(OrderedDict.fromkeys(key)) + [i for i in alphabet if i not in key]
    mat = reshape(mat, 5, 5)
    dic_mat = {}
    for i in range(5):
        for j in range(5):
            dic_mat[mat[i][j]] = (i, j)
    return dic_mat


def make_pairs(plain_text):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.replace("j", "i")
    paired_plain_text = ''

    i = 0
    while i < len(plain_text) - 1:
        if plain_text[i] == plain_text[i + 1] and plain_text[i] != 'x':
            paired_plain_text += plain_text[i] + 'x'
            i = i + 1
        elif plain_text[i] == plain_text[i + 1] and plain_text[i] == 'x':
            paired_plain_text += plain_text[i] + 'q'
            i = i + 1
        else:
            paired_plain_text += plain_text[i:i + 2]
            i = i + 2
    if len(plain_text) - i:
        paired_plain_text += plain_text[-1]
        if len(paired_plain_text) % 2 == 1:
            paired_plain_text += 'x'
    return [paired_plain_text[i:i + 2] for i in range(0, len(paired_plain_text), 2)]


#DES helper functions

def permutatation(mat, tabel):
    return [mat[i - 1] for i in tabel]



def key_round_generator(key, PC1, PC2, LSHIFT_MAP, round_num):
    key = permutatation(key, PC1)
    key_list = []
    key1 = list(key[:len(key) // 2])
    key2 = list(key[len(key) // 2:])
    # pc1 divide
    for i in range(round_num):
        key1=key1[-LSHIFT_MAP[i]:] + key1[:-LSHIFT_MAP[i]]
        key2 = key2[-LSHIFT_MAP[i]:] + key2[:-LSHIFT_MAP[i]]

        key_list.append(list(key1) + list(key2))

    for i in range(round_num):
        key_list[i] = permutatation(key_list[i], PC2)

    return key_list


def Make_xor(list1, list2):
    return [list1[i] ^ list2[i] for i in range(len(list1))]



def Round(L0, R0, key):
    L1 = R0  # pass right to left
    # Expand py E table
    R0 = permutatation(R0, E)


    E_XOR_R = Make_xor(R0, key)
    E_XOR_R = reshape(E_XOR_R, 8, 6)


    OutOfSBox = [SBOXES[i][int(bin(E_XOR_R[i][-1] + 2 * E_XOR_R[i][0]), 2)][
                int(bin(E_XOR_R[i][4] + 2 * E_XOR_R[i][3] + 4 * E_XOR_R[i][2] + 8 * E_XOR_R[i][1]), 2)] for i in
                 range(8)]
    OutOfSBox = [int(j) for i in OutOfSBox for j in '{:04b}'.format(i)]


    per = permutatation(OutOfSBox, P)

    R1 = Make_xor(L0, per)

    return L1, R1

def Caesar_Cipher_enc(plain_text, key):
    cipher_text = ''
    for p in plain_text:
        if p.isupper():

            index = ord(p) - ord('A')
            index = (index + key) % 26 + ord('A')
            cipher_text += chr(index)
        elif p.islower():

            index = ord(p) - ord('a')
            index = (index + key) % 26 + ord('a')
            cipher_text += chr(index)
        elif p.isdigit():

            index = (int(p) + key) % 10
            cipher_text += str(index)

    return cipher_text

def Playfair_enc(plain_text, key):
    p = make_pairs(plain_text)
    mat = MAT_creation(key)

    cipher_text = ''
    for (c1, c2) in p:
        row1, col1 = mat[c1]
        row2, col2 = mat[c2]

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1

        for key, value in mat.items():

            if value == (row1, col1):
                cipher_text += key
        for key, value in mat.items():
            if value == (row2, col2):
                cipher_text += key

    return cipher_text


def Hill_cipher(plain_text, key):
    take = len(key)
    cipher_text = ''
    if len(plain_text) % take != 0:
        plain_text = plain_text + 'X' * (take - (len(plain_text) % take))
    plain_text = [ord(i) - ord('a') for i in list(plain_text.lower().replace(' ', ''))]
    plain_text = reshape(plain_text, len(plain_text) // take, take)

    plain_text = flatten(transpose(mod(matmul(key, transpose(plain_text)))))
    plain_text = cipher_text.join([chr(i + ord('a')) for i in plain_text])
    return plain_text


def Vigenere_Cipher(plain_text, key, Auto=False):
    plain_text = plain_text.lower()
    key = key.lower()
    cipher_text = ''
    if Auto:
        key = key + plain_text
    else:
        key = key * -(-len(plain_text) // len(key))

    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))

    return cipher_text


def vernam(plain_text, key):
    assert len(plain_text) == len(key)
    plain_text = plain_text.lower()
    key = key.lower()
    cipher_text = ''
    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))

    return cipher_text

def Des_enc(p_string, key_string, round_num=16):
    # convert key and plain text to binary
    p = [int(i) for j in p_string for i in "{:04b}".format(int(j, 16))]
    key = [int(i) for j in key_string for i in "{:04b}".format(int(j, 16))]
    # generate all keys
    key_generated = key_round_generator(key, PC1, PC2, LSHIFT_MAP, round_num)

    ip_P = permutatation(p, IP)

    L0 = ip_P[:len(ip_P) // 2]
    R0 = ip_P[len(ip_P) // 2:]
    for i in range(round_num):
        L1, R1 = Round(L0, R0, key_generated[i])
        L0, R0 = L1, R1

    L1, R1 = R1, L1

    cipher = permutatation(L1 + R1, IP_INVERSE)

    return hex(int(str(''.join([str(elem) for elem in cipher])), 2))[2:]


def Des_dec(p_string, key_string, round_num=16):
    # convert key and plain text to binary
    p = [int(i) for j in p_string for i in "{:04b}".format(int(j, 16))]
    key = [int(i) for j in key_string for i in "{:04b}".format(int(j, 16))]
    # generate all keys
    key_generated = key_round_generator(key, PC1, PC2, LSHIFT_MAP, round_num)
    ip_P = permutatation(p, IP)

    L0 = ip_P[:len(ip_P) // 2]
    R0 = ip_P[len(ip_P) // 2:]
    for i in range(round_num):
        L1, R1 = Round(L0, R0, key_generated[round_num - i - 1])
        L0, R0 = L1, R1

    L1, R1 = R1, L1

    cipher = permutatation(L1 + R1, IP_INVERSE)
    return hex(int(str(''.join([str(elem) for elem in cipher])), 2))[2:]







#AES helper functions

def hex_to_binary(hex):
    temp = []
    for H in hex:
        temp += [int(i) for i in format(int(str(H), 16), '#06b')[2:]]
    return temp


def BinarytoHex(BinaryList):
    return format(int(''.join([str(i) for i in BinaryList]), 2), '#04x')[2:].upper()


def xor(hexa_1, hexa_2):
    hexa_in_binary_form = hex_to_binary(hexa_1)
    hexa_in_binary_form2 = hex_to_binary(hexa_2)

    output = []
    output2 = []
    for i in range(len(hexa_in_binary_form)):
        output.append(hexa_in_binary_form[i] ^ hexa_in_binary_form2[i])

    for i in range(0, len(output), 8):
        output2.append(BinarytoHex(output[i:i + 8]))
    return ''.join(output2)


def Xor_mat(grid1, grid2):
    new_mat = []
    for i in range(4):
        mat = []
        for j in range(4):
            mat.append(xor(grid1[i][j], grid2[i][j]))
        new_mat.append(mat)
    return new_mat


def shiftrow(hexa_num):  # take string shift and back
    return hexa_num[2:] + hexa_num[0:2]


# subbytes functions
def subbyte(hexa_byte):  # string return the value
    Sub_STRing = ''

    for i in range(0, len(hexa_byte), 2):
        Sub_STRing += SBOX[int(hexa_byte[i], 16)][int(hexa_byte[i + 1], 16)]
    return Sub_STRing


def subbyte_mat(grid_hexa):  # string return the value
    new_status = []

    for i in range(4):
        l = []
        for j in range(4):
            l.append(SBOX[int(grid_hexa[i][j][0], 16)][int(grid_hexa[i][j][1], 16)])
        new_status.append(l)
    return new_status


def Inv_subbyte_mat(grid_hexa):  # string return the value
    new_status = []

    for i in range(4):
        l = []
        for j in range(4):
            l.append(SBOXINV[int(grid_hexa[i][j][0], 16)][int(grid_hexa[i][j][1], 16)])
        new_status.append(l)
    return new_status


# mix columns and matrix multiplication in gloa feild
def multiply_by_2(v):
    s = v << 1
    s &= 0xff
    if (v & 128) != 0:
        s = s ^ 0x1b
    return s


def multiply_by_3(v):
    return multiply_by_2(v) ^ v

def mix_column(column):
    r = [   multiply_by_2(column[0]) ^ multiply_by_3(column[1]) ^ column[2] ^ column[3],
            multiply_by_2(column[1]) ^ multiply_by_3(column[2]) ^ column[3] ^ column[0],
            multiply_by_2(column[2]) ^ multiply_by_3(column[3]) ^ column[0] ^ column[1],
            multiply_by_2(column[3]) ^ multiply_by_3(column[0]) ^ column[1] ^ column[2],]

    return r

def mix_columns(grid):
    new_grid = [[], [], [], []]
    for i in range(4):
        col = [grid[j][i] for j in range(4)]
        col = mix_column(col)
        for i in range(4):
            new_grid[i].append(col[i])
    return new_grid


def Inv_mix_columns(grid):
    status = mix_columns([[int(j, 16) for j in i] for i in grid])
    status = mix_columns(status)
    status = mix_columns(status)
    for i in range(4):
        for j in range(4):
            status[i][j] = hex(status[i][j])[2:]
            if len(status[i][j]) < 2:
                status[i][j] = '0' + status[i][j]
    return status


# generate rounds keys
def findroundkey(temp1, round_number):
    w0 = temp1[0:8]
    w1 = temp1[8:16]
    w2 = temp1[16:24]
    w3 = temp1[24:32]

    temp2 = subbyte(shiftrow(w3))
    if (round_number == 1):
        temp2 = xor(temp2, '01000000')
    elif (round_number == 2):
        temp2 = xor(temp2, '02000000')
    elif (round_number == 3):
        temp2 = xor(temp2, '04000000')
    elif (round_number == 4):
        temp2 = xor(temp2, '08000000')
    elif (round_number == 5):
        temp2 = xor(temp2, '10000000')
    elif (round_number == 6):
        temp2 = xor(temp2, '20000000')
    elif (round_number == 7):
        temp2 = xor(temp2, '40000000')
    elif (round_number == 8):
        temp2 = xor(temp2, '80000000')
    elif (round_number == 9):
        temp2 = xor(temp2, '1b000000')
    elif (round_number == 10):
        temp2 = xor(temp2, '36000000')

    w4 = xor(w0, temp2)
    w5 = xor(w1, w4)
    w6 = xor(w2, w5)
    w7 = xor(w3, w6)

    return w4 + w5 + w6 + w7

# shift

# A1EE5608B33AF05470858608D1DE080F
def rotate(status):  # status numpy array in shape of (4,4)

    status[1] = status[1][1:] + status[1][:1]
    status[2] = status[2][2:] + status[2][:2]
    status[3] = status[3][3:] + status[3][:3]

    return status

def Inv_rotate(status):  # status numpy array in shape of (4,4)

    status[1] = status[1][-1:] + status[1][:-1]
    status[2] = status[2][-2:] + status[2][:-2]
    status[3] = status[3][-3:] + status[3][:-3]

    return status


def AES_enc(text, key):
    key_list = []
    key_list.append(key)
    # key extracted for each round
    for i in range(1, 11):
        key = findroundkey(temp1=key, round_number=i)
        key_list.append(key)
    # reshape the keys and text to (4 * 4)
    text = transpose(reshape([text[i:i + 2] for i in range(0, len(text), 2)], 4, 4))
    for j in range(len(key_list)):
        key_list[j] = transpose(reshape([key_list[j][i:i + 2] for i in range(0, len(key_list[j]), 2)], 4, 4))
    # round 0

    status = Xor_mat(text, key_list[0])  # grid hexa string

    # round 1
    for k in range(1, 11):
        status = subbyte_mat(status)  # grid hexa string

        status = rotate(status)

        if k != 10:
            status = mix_columns([[int(j, 16) for j in i] for i in status])  # grid hexa string
            for i in range(4):
                for j in range(4):
                    status[i][j] = hex(status[i][j])[2:]
                    if len(status[i][j]) < 2:
                        status[i][j] = '0' + status[i][j]


        status = Xor_mat(status, key_list[k])

    cipher_text = ''
    for i in range(4):
        for j in range(4):
            cipher_text += status[j][i]
    return cipher_text

def AES_dec(text, key):
    key_list = []
    key_list.append(key)

    # key generation
    for i in range(1, 11):
        key = findroundkey(temp1=key, round_number=i)
        key_list.append(key)

    # reshape the keys and text to (4 * 4)
    text = transpose(reshape([text[i:i + 2] for i in range(0, len(text), 2)], 4, 4))
    for j in range(len(key_list)):
        key_list[j] = transpose(reshape([key_list[j][i:i + 2] for i in range(0, len(key_list[j]), 2)], 4, 4))


    status = Xor_mat(text, key_list[-1])  # reound 0, grid hexa string
    for k in range(2, 12): # 10 rounds
        status = Inv_rotate(status)
        status = Inv_subbyte_mat(status)
        status = Xor_mat(status, key_list[-k])

        if k != 11:
            status = Inv_mix_columns(status)

    plain_text = ''
    for i in range(4):
        for j in range(4):
            plain_text += status[j][i]

    return plain_text


#
# from utils import *
#
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