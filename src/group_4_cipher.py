from columnar import Columnar
from rail_fence import RailFence
from scytale import Scytale
from cipher_abstract import Cipher
from random import randint

class Group4Cipher(Cipher):

    def __init__(self, rows, key):
        self.rows = rows
        self.key = key
    
    def encrypt(self, plaintext):
        
        # Layer 1 - Scytale
        global scytale
        scytale = Scytale()
        layerOne = scytale.encrypt(self.rows, plaintext)
        # print("Layer 1: " + layerOne)

        # Layer 2 - Rail Fence
        global railFence
        railFence = RailFence(self.rows)
        layerTwo = railFence.encrypt(layerOne)
        # print("Layer 2: " + layerTwo)

        # Layer 3 - Columnar
        global columnar
        columnar = Columnar(self.key)
        layerThree = columnar.encrypt(layerTwo)
        # print("Layer 3: " + layerThree)
        
        encryptedText = layerThree
        return encryptedText

    def decrypt(self, ciphertext):

        # Layer 3 - Columnar
        layerThree = columnar.decrypt(ciphertext)
        # print("Layer 3: " + layerThree)

        # Layer 2 - Rail Fence
        layerTwo = railFence.decrypt(layerThree)
        # print("Layer 2: " + layerTwo)

        # Layer 1 - Scytale
        layerOne = scytale.decrypt(self.rows, layerTwo)
        # print("Layer 1: " + layerOne)

        decryptedText = layerOne
        return decryptedText

def getRows(text):
    textLength = len(text)
    while True:
        # Return a integer between 4 and length of text
        rows = randint(4, len(text))
        if textLength % rows == 0:
            break
    return rows

def isPrime(num):
    for n in range(2, int(num ** 1 / 2) + 1):
        if num % n == 0:
            return False
    return True

