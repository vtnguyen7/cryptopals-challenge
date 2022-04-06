from Crypto.Cipher import AES
import random
import challenge8 as c8
import base64

def xor(a, b):

	x = bytearray()

	for i, j in zip(a, b):

		x.append(i ^ j)
	
	return(x)

def int_to_bytes(num):

	return(num.to_bytes((num.bit_length() + 7) // 8, byteorder = "big"))

def padder(byts, number):

	return(byts + b'\x04' * (number - (len(byts) % number)))

def encryptor(plaintext, IV, cipher):

	feed = bytearray(IV)

	blocksize = len(feed)
	
	ciphertext = b''

	while len(plaintext) > 0:
	
		block = plaintext[0: blocksize]
	
		block = padder(block, blocksize)
		
		x = bytes(xor(feed, block))
		feed = cipher.encrypt(x)

		ciphertext = ciphertext + feed
	
		del plaintext[0: blocksize]

	return(ciphertext)

plaintext = "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a"

def genrandombytes(i):

	x = b''

	for i in range(i):

		x += int_to_bytes(random.randint(0,255))

	return(x)

def randomcryptor(plaintext):

	key = genrandombytes(16)
	cipher = AES.new(key, AES.MODE_ECB)
	padded_text = padder(genrandombytes(random.randint(5, 10)) + bytes(plaintext, "utf-8") + genrandombytes(random.randint(5, 10)), 16)

	if random.randint(0,1):

		print("I used CBC!")

		randiv = genrandombytes(16)
		return(encryptor(bytearray(padded_text), randiv, cipher))

	else:

		print("I used ECB!")

		return(cipher.encrypt(padded_text))

def guesser(plaintext):

	
	text = randomcryptor(plaintext)	

	blocktext = []

	for i in range((len(text) // 16)):
			
		blocktext.append(text[16*i:16*(i + 1)])

	freqs = c8.freq_count(blocktext)

	if freqs[-1]["count"] > 1:

		return("ECB")

	else:

		return("CBC")

# print(guesser(plaintext))
