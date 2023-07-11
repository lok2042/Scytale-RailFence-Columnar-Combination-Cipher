from group_4_cipher import Group4Cipher
from random import randint

def main():

    print("\n=== 🎭 Group 4 Cipher Program 💻 ===")

    ############# SETTINGS ###############
    ROWS = 4            
    KEY = "security"    
    group4Cipher = Group4Cipher(ROWS, KEY)
    ######################################

    while True:
        print("\n--- MENU ---")
        print("1 - Encryption 🔒 ")
        print("2 - Decryption 🔑 ")
        print("0 - Quit 🛑 ")

        try:
            choice = int(input("Choice : "))
            print()
        except:
            print("Please enter an integer!")

        if choice == 1:

            plaintext = input("Enter plaintext  : ")
            print("\nOriginal Text : " + plaintext)

            textLength = len(plaintext)
            if textLength % group4Cipher.rows != 0:
                while True:
                    new_rows = randint(4, len(plaintext))
                    if textLength % new_rows == 0:
                        group4Cipher.rows = new_rows
                        break
            
            try:
                ciphertext = group4Cipher.encrypt(plaintext)
                print("Cipher Text   : " + ciphertext)
            except:
                print("Sorry, something went wrong 😢")

        elif choice == 2:

            ciphertext = input("Enter ciphertext : ")
            print("\nCipher Text   : " + ciphertext)

            try:
                plaintext = group4Cipher.decrypt(ciphertext)
                print("Original Text : " + plaintext)
            except:
                print("Sorry, something went wrong 😢")

        elif choice == 0:
            break
        else:
            print("Invalid Choice! Please try again.")

    print("👋 👋 END OF PROGRAM 👋 👋 \n")

if __name__ == '__main__':
    main()