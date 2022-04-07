import base64
import random
from Crypto.Cipher import AES

# I did it!!!!!

secrettext = base64.b64decode("".join([x.strip("\n") for x in open("12.txt", "r").readlines()]))

def int_to_bytes(num):

	return(num.to_bytes((num.bit_length() + 7) // 8, byteorder = "big"))

def padder(byts, number):

	return(byts + b'\x04' * (number - (len(byts) % number)))

def genrandombytes(i):

	x = b''

	for i in range(i):

		x += int_to_bytes(random.randint(0,255))

	return(x)

key = genrandombytes(16)
prepend = genrandombytes(random.randint(0, 16))

cipher = AES.new(key, AES.MODE_ECB)

def oracle(plaintext):

	padded_text = prepend + plaintext + secrettext 
	return(cipher.encrypt(padder(padded_text, 16)))

def size_detector():

	i = -1
	diff = 0

	while diff == 0:

		i += 1
		diff = len(oracle(bytes("A" * (i + 1), "utf-8"))) - len(oracle(bytes("A" * i, "utf-8")))

	return(diff, i)

blocksize = size_detector()[0]
number = size_detector()[1]

def cnt(l):

	return(l["count"])

def freq_count(l):

	things = []

	thindex = []

	for thing in l:


		if thing not in thindex:

			things.append({"item": thing, "count": 1})
			thindex.append(thing)

		else:

			for i in things:

				if i["item"] == thing:

					i["count"] += 1
	
	things.sort(key = cnt)
	return(things)

def length_finder():

	blocks = []
	i = -1

	text = oracle(bytes("", "utf-8"))

	blocktext = []

	for i in range((len(text) // blocksize)):
				
		blocktext.append(text[blocksize*i:blocksize*(i + 1)])

	blocks = freq_count(blocktext)

	while blocks[-1]["count"] <= 1:

		i += 1
		
		text = oracle(bytes("A"*i, "utf-8"))

		blocktext = []

		for j in range((len(text) // blocksize)):
				
			blocktext.append(text[blocksize*j:blocksize*(j + 1)])

		blocks = freq_count(blocktext)

	return(i)

extrapadding = length_finder()

def bytefinder():
	
	## to do

print(bytefinder())
