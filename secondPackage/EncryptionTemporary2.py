
while(True):
    tte = input("\nEnter something to encrypt or decrypt: \n")
    print("Your text is: \n")
    for i in tte:
        print(chr(ord(i)^123), end='') #encrypts your text
