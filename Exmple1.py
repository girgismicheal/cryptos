from Cryptography.ciphers import AES


def main():
    key  =input('enter your key: ')#'0123456789ABCDEF0123456789ABCDEF'
    text =input('enter your text: ')#'0123456789ABCDEF0123456789ABCDEF'
    encryption = int(input('for encryption enter 1 for decryption enter 0 :'))
    if encryption==1:
        print('the cipher text is :',AES(key).encrypt(text))
    elif encryption==0:
        print('the plain text is: ' ,AES(key).decrypt(text))
    else:
        print('sorry ! please try again with valid choice')

if __name__ == "__main__":
    Continue =1
    while Continue == 1:
        main()
        Continue = int(input('1: to Continue and else to end the program '))
