class Cipher:
    def __init__(self, keyword):
        self.keyword = ''.join(set(keyword.upper()))  # Remove duplicates and uppercase
        self.keyword = keyword.upper()  # Remove duplicates and uppercase
        self.alphabet_upper = self.keyword + ''.join(chr(i) for i in range(65, 91) if chr(i) not in self.keyword)
        self.alphabet_lower = self.alphabet_upper.lower()

    def encode(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isupper():
                index = (ord(char) - 65) % 26  # Get index in alphabet (0-25)
                ciphertext += self.alphabet_upper[index]
            elif char.isspace():
                ciphertext += char
            else:
                index = (ord(char) - 97) % 26
                ciphertext += self.alphabet_lower[index]
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ""
        print(ciphertext)
        for char in ciphertext:
            if char.isupper():
                index = self.alphabet_upper.index(char)
                plaintext += chr(65 + index)
            elif char.isspace():
                plaintext += char
            else:
                index = self.alphabet_lower.index(char)
                plaintext += chr(97 + index)
        return plaintext

if __name__ == '__main__':
    # cipher = Cipher("crypto")
    # encoded_text = cipher.encode("Hello world")
    # decoded_text = cipher.decode("Fjedhc dn atidsn")
    #
    # print(f"Encoded text: {encoded_text}")  # Output: Btggj vjmgp
    # print(f"Decoded text: {decoded_text}")  # Output: Kojima is genius

    cipher = Cipher("trial")
    encoded_text = cipher.encode("Hello world")
    decoded_text = cipher.decode("Fjedhc dn atidsn")

    print(f"Encoded text: {encoded_text}")  # Output: Btggj vjmgp
    print(f"Decoded text: {decoded_text}")  # Output: Kojima is genius
