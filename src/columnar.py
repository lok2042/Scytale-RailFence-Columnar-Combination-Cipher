from math import ceil
from cipher_abstract import Cipher  

class Columnar(Cipher):

    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        cipher = ""
        key_index = 0
        plaintext_length = float(len(plaintext))
        plaintext_list = list(plaintext)
        key_list = sorted(list(self.key))
        col = len(self.key)
        row = int(ceil(plaintext_length / col))
    
        fill_space = int((row * col) - plaintext_length)
        plaintext_list.extend('_' * fill_space)
    
        matrix = [plaintext_list[i: i + col] for i in range(0, len(plaintext_list), col)]

        for letter in range(col):
            current_index = self.key.index(key_list[key_index])
            cipher += ''.join([row[current_index] for row in matrix])
            key_index += 1
    
        return cipher

    def decrypt(self, ciphertext):
        msg = ""
        key_index = 0
        msg_index = 0
        msg_length = float(len(ciphertext))
        msg_list = list(ciphertext)
        col = len(self.key)
        row = int(ceil(msg_length / col))
        key_list = sorted(list(self.key))
        
        decrypted_ciphertext = []
        
        for character in range(row):
            decrypted_ciphertext += [[None] * col]

        for character in range(col):
            current_index = self.key.index(key_list[key_index])
            
            for j in range(row):
                decrypted_ciphertext[j][current_index]= msg_list[msg_index] 
                msg_index += 1
            key_index += 1
        
        msg = ''.join(sum(decrypted_ciphertext, []))
        underscore_count = msg.count('_')
        
        if underscore_count > 0:
            return msg[: -underscore_count]
        
        return msg