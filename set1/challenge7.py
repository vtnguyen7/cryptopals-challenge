from Crypto.Cipher import AES
import base64

f = open("7.txt", "r")
opened = [x.strip("\n") for x in f.readlines()]
ciphertext = bytes(base64.b64decode("".join(opened)))

key = "YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)

print(cipher.decrypt(ciphertext))
