import sys
#Used this site as a cross reference to make sure my cipher was accurate
#https://www.dcode.fr/caesar-cipher

#Main menu which displays all possible options the user can pick from

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
 "k", "l", "m", "n", "o", "p", "q", "r", 
 "s", "t", "u", "v", "w", "x", "y", "z"] #Array containing the alphabet

newAlphabet = {} #Alphabet after shifting by the user's inputted number
 
def menu():

    print("CAESAR CIPHER")
    print("===================")
    print("1: Encrypt")
    print("2: Decrypt")
    print("3: Decrypt (Brute Force)")
    print("4: Exit")
    
    #User has to pick an option from 1 to 4 otherwise the program keeps looping back until the user inputs a valid entry
    while True:
        try:
            option = int(input("Enter a number from 1-4: ")) #Enter a number

            if option == 1:
                encrypt() #Option 1 brings up the encryption section
                break
            elif option == 2:
                decrypt() #Option 2 brings up the decryption section
                break
            elif option == 3:
                bruteForceDecrypt() #Option 3 will up the brute force decryption section
                break
            elif option == 4:
                print("Goodbye") #Option 4 exits the program
                sys.exit()
            else:
                print("You must pick a number from 1-4!") #Loops back if a number not between 1 to 4 is entered
        except ValueError:
            print("You must enter a number!") #Loops back if anything but a number isn't entered

#This function takes user's input and encrypts the text 
def encrypt():

    while True:
        try:
            encryptMsg = input("Enter your message for encryption: ").lower() #Enter the text for encryption
            numShift = int(input("Enter the number of letters you would like to shift by: ")) #Enter the number of letters to shift by

            if numShift > 0 and numShift <= 25: #Check the shift number is greater than 1 and less or equal to 25
                break

        except ValueError:
            print("You must enter a number!") #Error if a number isn't entered
        else:
            print("You must enter a number from 1 to 25!") #Error if a number less than 1 or greater than 25 is entered

    encryptedMsg = ""

    #Loop through the alphabet array, shifting by the number inputted by the user
    for i in range(len(alphabet)):
        letter = alphabet[i]
        shiftedLetter = alphabet[(i+numShift)%26]
        newAlphabet[letter] = shiftedLetter #Shifted alphabet is put into the newAlphabet array

    #Loop through the letters in the text that was inputted by the user
    for letter in encryptMsg:
        if letter in alphabet:
            letter = newAlphabet[letter]
            encryptedMsg = encryptedMsg + letter
        else:
            encryptedMsg = encryptedMsg + letter

    print("Encrypted Message: " + encryptedMsg)

#Decrypts the text inputted by the user which decrypts the text inputted by the user, assuming they know the message and shift number
def decrypt():

    while True:
        try:
            decryptMsg = input("Enter your message for decryption: ").lower() #Enter the text for dedryption
            numShift = int(input("Enter the number of letters you would like to shift by: ")) #Enter the number of letters to shift by

            if numShift > 0 and numShift <= 25: #Check the shift number is greater than 1 and less or equal to 25
                break
        except ValueError:
            print("You must enter a number!") #Error if a number isn't entered
        else:
            print("You must enter a number from 1 to 25!") #Error if a number less than 1 or greater than 25 is entered

    decryptedMsg = ""

    #Loop through the alphabet array, shifting by the number inputted by the user
    for i in range(len(alphabet)):
        letter = alphabet[i]
        shiftedLetter = alphabet[(i-numShift)%26]
        newAlphabet[letter] = shiftedLetter #Shifted alphabet is put into the newAlphabet array

    #Loop through the letters in the text that was inputted by the user
    for letter in decryptMsg:
        if letter in alphabet:
            letter = newAlphabet[letter]
            decryptedMsg = decryptedMsg + letter
        else:
            decryptedMsg = decryptedMsg + letter

    print("Decrypted Message: " + decryptedMsg)

#Prints out a list of all possible combinations based on the user's input should they not know the number of shifts
def bruteForceDecrypt():

    bruteForceMsg = input("Enter your message: ").lower() #Enter the message for decryption

    possibleShift = ''

    print()
    print("Shift(s): " + " " + "Message:")
    print("===================")
    
    #Prints out a list of possible combinations from 1 to 26 shifts
    for possibleShift in range(1, 26):
        possibleMsg = ""
        for i in range(26):
            letter = alphabet[i]
            shiftedLetter = alphabet[(i-possibleShift)%26]
            newAlphabet[letter] = shiftedLetter
        for letter in bruteForceMsg:
            if letter in alphabet:
                letter = newAlphabet[letter]
                possibleMsg = possibleMsg + letter
            else:
                possibleMsg = possibleMsg + letter     
        print("+" + str(possibleShift) + ": " +  "       " + possibleMsg)
    
if __name__ == "__main__":
    menu()