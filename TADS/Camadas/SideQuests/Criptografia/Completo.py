from Cryptodome.Cipher import AES
from Cryptodome import Random

plain_text = "This is the text to encrypt"
key = b"0361231230000000"

class FerramentasCrypto:
    def encrypt(self, plain_text, key):
        cipher = AES.new(key, AES.MODE_CBC)
        b = plain_text.encode("UTF-8")
        return cipher.iv, cipher.encrypt(b)
    def decrypt(self, iv, enc_text):
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        return cipher.decrypt(enc_text).decode("UTF-8")

if __name__ == "__main__":
    tool = FerramentasCrypto()
    iv, enc_text = tool.encrypt(plain_text[:16], key)
    dec_text = tool.decrypt(iv, enc_text)
    print(dec_text)