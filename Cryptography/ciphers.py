from .utils import *


class cipher:
    def __init__(self, key):
        self.key = key

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def encrypt(self, plain_text):
        pass

    def decrypt(self,cipher_texy):
        pass


class Caesar(cipher):
    def encrypt(self, plain_text):
        return Caesar_Cipher_enc(plain_text,self.key)


class Playfair(cipher):
    def encrypt(self, plain_text):
        return Playfair_enc(plain_text,self.key)


class Hill(cipher):
    def encrypt(self, plain_text):
        return Hill_cipher(plain_text,self.key)


class Vignere(cipher):
    def encrypt(self, plain_text):
        return Vigenere_Cipher(plain_text, self.key)


class Vernam(cipher):
    def encrypt(self, plain_text):
        return vernam(plain_text, self.key)


class AES(cipher):

    def encrypt(self, plain_text):
        return AES_enc(plain_text, self.key)

    def decrypt(self, cipher_texy):
        return AES_dec(cipher_texy, self.key)


class DES(cipher):

    def encrypt(self, plain_text):
        return Des_enc(plain_text, self.key)

    def decrypt(self, cipher_texy):
        return Des_dec(cipher_texy, self.key)
