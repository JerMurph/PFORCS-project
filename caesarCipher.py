import sys

#Used this site as a cross reference to make sure my cipher was accurate
#https://www.dcode.fr/caesar-cipher

#Sample texts for testing decryption and encryption:

#hello
#nkrru (Shift by 6)

#a wall of text is an excessively long post, which can often be so long that some don't read it.
#g cgrr ul zkdz oy gt kdikyyobkre rutm vuyz zu g tuzoikhugxj ux zgrq vgmk joyiayyout, cnoin igt ulzkt hk yu rutm zngz yusk jut'z xkgj oz. (Shift by 6)
 
def menu():
    print("CAESAR CIPHER")
    print("===================")
    print("1: Encrypt")
    print("2: Decrypt")
    print("3: Decrypt (Brute Force)")
    print("4: Exit")
    
    while True:
        try:
            option = int(input("Enter a number from 1-4: "))

            if option == 1:
                encrypt()
                break
            elif option == 2:
                decrypt()
                break
            elif option == 3:
                bruteForceDecrypt()
                break
            elif option == 4:
                print("Goodbye")
                sys.exit()
            else:
                print("You must pick a number from 1-4!")
        except ValueError:
            print("You must enter a number!")

def encrypt():

    while True:
        try:
            encryptMsg = input("Enter your message for encryption: ").lower()
            numShift = int(input("Enter the number of letters you would like to shift by: "))

            if numShift > 0 and numShift <= 25:
                break

        except ValueError:
            print("You must enter a number!")
        else:
            print("You must enter a number from 1 to 25!")

    encryptedMsg = ""

    for symbol in encryptMsg:
        if symbol.isalpha():
            num = ord(symbol)
            num += numShift

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMsg += chr(num)
        else:
            encryptedMsg += symbol

    print("Encrypted Message: " + encryptedMsg)

def decrypt():

    while True:
        try:
            decryptMsg = input("Enter your message for decryption: ").lower()
            numShift = int(input("Enter the number of letters you would like to shift by: "))

            if numShift > 0 and numShift <= 25:
                break

        except ValueError:
            print("You must enter a number!")
        else:
            print("You must enter a number from 1 to 25!")

    decryptedMsg = ""

    for symbol in decryptMsg:
        if symbol.isalpha():
            num = ord(symbol)
            num -= numShift

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            decryptedMsg += chr(num)
        else:
            decryptedMsg -= symbol

    print("Decrypted Message: " + decryptedMsg)

def bruteForceDecrypt():
    bruteForceMsg = input("Enter your message: ").lower()

    possibleShift = ''

    print()
    print("Shift(s): " + " " + "Message:")
    print("===================")
    
    for possibleShift in range(1, 26):

        possibleMsg = ""
        
        for symbol in bruteForceMsg:
            if symbol.isalpha():
                num = ord(symbol)
                num -= possibleShift

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26
                possibleMsg += chr(num)
            else:
                possibleMsg -= symbol

        print("+" + str(possibleShift) + ": " +  "       " + possibleMsg)
    
if __name__ == "__main__":
    menu()