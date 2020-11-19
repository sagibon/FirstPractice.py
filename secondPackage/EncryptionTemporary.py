
while(True):
    user = input("\nEnter something to encrypt: \n")
    print("Your encrypted text is: ")
    for i in user:
        print(chr(ord(i)+2), end='')
    #return ur user name from password
    password = input("\nEnter your encrypted text to decrypt: \n")
    for i in password:
        print(chr(ord(i)-2),end='')