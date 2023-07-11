from cipher_abstract import Cipher

class Scytale(Cipher):

    def encrypt(self, rows, plaintext):
        assert len(plaintext) % rows == 0
        n = len(plaintext)
        columns = n // rows
        ciphertext = ['-'] * n
        for i in range(n):
            row = i // columns
            col = i % columns
            ciphertext[col * rows + row] = plaintext[i]
        return "".join(ciphertext)


    def decrypt(self, rows, ciphertext):
        assert len(ciphertext) % rows == 0
        return self.encrypt(len(ciphertext) // rows, ciphertext)