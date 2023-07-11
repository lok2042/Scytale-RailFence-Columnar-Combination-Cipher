import unittest
import random  
import string

from group_4_cipher import Group4Cipher, getRows, isPrime
from columnar import Columnar
from rail_fence import RailFence
from scytale import Scytale

def generate_str(length):
    return ''.join((random.choice(string.ascii_letters) for x in range(length)))

class TestOverall(unittest.TestCase):
    
    def test_overall(self):

        # Part 1
        plaintext1 = "The Russians have invaded Ukraine! SEEK SHELTER IMMEDIATELY. This is not a drill...."

        while isPrime(len(plaintext1)):
            plaintext1 = plaintext1 + " "
        rows1 = getRows(plaintext1)
        group4Cipher1 = Group4Cipher(rows1, "putin")
        
        ciphertext1 = group4Cipher1.encrypt(plaintext1) 
        decryptedText1 = group4Cipher1.decrypt(ciphertext1) 

        self.assertEqual(
            plaintext1,
            decryptedText1
        )

        # Part 2
        plaintext2 = "The quick brown fox jumps over the lazy dog"

        while isPrime(len(plaintext2)):
            plaintext2 = plaintext2 + " "
        rows2 = getRows(plaintext2)
        group4Cipher2 = Group4Cipher(rows2, "quick")
        
        ciphertext2 = group4Cipher2.encrypt(plaintext2) 
        decryptedText2 = group4Cipher2.decrypt(ciphertext2) 

        self.assertEqual(
            plaintext2,
            decryptedText2
        )


class TestScytale(unittest.TestCase):

    def test_scytale(self):
        scytale = Scytale()

        for i in range(20):
            plaintext = generate_str(i)

            while isPrime(len(plaintext)):
                plaintext = plaintext + " "

            rows = getRows(plaintext)  

            ciphertext = scytale.encrypt(rows, plaintext) 
            decryptedText = scytale.decrypt(rows, ciphertext) 

            self.assertEqual(
                plaintext,
                decryptedText
            )


class TestRailFence(unittest.TestCase):

    def test_railfence(self):
        
        for i in range(20):
            plaintext = generate_str(i)

            while isPrime(len(plaintext)):
                plaintext = plaintext + " "

            rows = getRows(plaintext) 
            railFence = RailFence(rows)

            ciphertext = railFence.encrypt(plaintext) 
            decryptedText = railFence.decrypt(ciphertext) 

            self.assertEqual(
                plaintext,
                decryptedText
            )


class TestColumnar(unittest.TestCase):

    def test_columnar(self):

        key = "security"

        for i in range(20):
            
            # Generate a random string with length between 6 and 20
            plaintext = generate_str(random.randint(6, 20))

            columnar = Columnar(key)
            ciphertext = columnar.encrypt(plaintext) 
            decryptedText = columnar.decrypt(ciphertext) 

            self.assertEqual(
                plaintext,
                decryptedText
            )

if __name__ == '__main__':
    unittest.main()