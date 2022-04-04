from Crypto.Cipher import AES
import base64
import challenge9 as c9

def xor(a, b):

	x = bytearray()

	for i, j in zip(a, b):

		x.append(i ^ j)
	
	return(x)

key = "YELLOW SUBMARINE"
blocksize = len(key)

IV = b'\x00' * blocksize

f = open("10.txt", "r")
opened = [x.strip("\n") for x in f.readlines()]
text = bytearray(base64.b64decode("".join(opened)))

cipher = AES.new(key, AES.MODE_ECB)


def encryptor(plaintext, IV):

	feed = bytearray(IV)
	
	ciphertext = b''

	while len(plaintext) > 0:
	
		block = plaintext[0: blocksize]
	
		block = c9.padder(block, blocksize)
		
		x = bytes(xor(feed, block))
		feed = cipher.encrypt(x)

		ciphertext = ciphertext + feed
	
		del plaintext[0: blocksize]

	return(ciphertext)

def decryptor(ciphertext, IV):

	feed = bytearray(IV)

	plaintext = ""
	
	while len(ciphertext) > 0:
	
		block = ciphertext[0: blocksize]
	
		block = c9.padder(block, blocksize)

		x = cipher.decrypt(bytes(block))	

		plaintext = "".join([plaintext, xor(feed, x).decode("utf-8")])

		feed = block

		del ciphertext[0: blocksize]

	return(plaintext)

#decrypted = decryptor(text, IV)
#print(decrypted)
#print(base64.b64encode(encryptor(bytearray(decrypted, "utf-8"), IV)))
