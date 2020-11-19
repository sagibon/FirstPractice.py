import binascii


def encfunction(text):
    enclist = [b^11 for b in text]
    return enclist

while(True):
    word = input("enter a sentence to encrypt or decrypt, the program will understand which one:\n ")
    print(type(word))
    if word == 'stop':
        break

    elif word.__contains__('a') or word.__contains__('b') or word.__contains__('c') or word.__contains__('d') or word.__contains__('e') or word.__contains__('f'):
        print("Decrypting...")
        print(binascii.unhexlify(word).decode("utf8"))
        print(type(word))
    else:
        print("Encrypting...")
        print(type(binascii.hexlify(word.encode("utf8"))))
        print(binascii.hexlify(word.encode("utf8")))
        utf8 = binascii.hexlify(word.encode("utf8"))
        print(encfunction(utf8))
        print(bytes(encfunction(utf8)))


""" else:
        word = binascii.hexlify(word.encode("utf8"))
        print(type(word))
        print("Encrypting...")
        list = [int(d) for d in word]

        for i in list:
            encrypted = xor(i,11)
            #print(encrypted)
            encrypted = chr(encrypted)
            print(encrypted,end='')
        decod = input("enter chars to decode:")
        listdecrypt = [d for d in decod]
        place=0
        for i in listdecrypt:
            ord(listdecrypt[place])
            print(listdecrypt)
            decoded = xor(int(listdecrypt[place]),11)
            final = binascii.unhexlify(decoded).decode("utf8")
            print(final)
            place+=1"""



















