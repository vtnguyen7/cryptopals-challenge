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

key = genrandombytes(16)

cipher = AES.new(key, AES.MODE_ECB)

def oracle(plaintext):

	padded_text = plaintext + secrettext 
	return(cipher.encrypt(padder(padded_text, 16)))

# Part I: Detect block size

def size_detector():

	i = 0
	diff = 0

	while diff == 0:

		diff = len(oracle(bytes("A" * (i + 1), "utf-8"))) - len(oracle(bytes("A" * i, "utf-8")))
		i += 1

	return(diff)

blocksize = size_detector()

print("out blocksize is " + str(blocksize))

# Part II: Detect ECB

def guesser():
	
	text = oracle(bytes("A"*256, "utf-8"))

	blocktext = []

	for i in range((len(text) // 16)):
			
		blocktext.append(text[16*i:16*(i + 1)])

	freqs = freq_count(blocktext)

	if freqs[-1]["count"] > 1:

		return("ECB")

	else:

		return("CBC")

print("we are in " + guesser())

def bytefinder():

	biglen = len(oracle(bytes("", "utf-8")))
	next_letter = b''
	
	for i in range(1, biglen - 1):

		m = []
		for j in range(1, 255):
			
			b = int_to_bytes(j)
			k = bytes("A"*(biglen - i), "utf-8") + next_letter + b
			m.append({"key": b, "output": oracle(k)})

		actual = oracle(bytes("A"*(biglen - i), "utf-8"))[0:biglen]

		for entry in m:

			if actual == entry["output"][0:biglen]:

				next_letter += entry["key"]

	return(next_letter)

print(bytefinder())
