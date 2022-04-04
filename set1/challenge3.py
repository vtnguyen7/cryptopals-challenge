# Single gyte xor

import base64
import challenge1 as tools

#hex_string = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

# define a list of outputs and write to the outputs each xor

def xor(a, b):

	x = bytearray()

	for i, j in zip(a, b):

		x.append(i ^ j)
	
	return(x)

def repeating_key(barray):

	outs = []
	
	for i in range(1, 256):

		repeater = [i] * len(barray)
	
		try:
			outs.append(bytearray.decode(xor(repeater, barray), "utf-8"))
		except:
			pass
	
	return(outs)

letter_list = {}
letter_list["a"] = 8.2
letter_list["b"] = 1.5
letter_list["c"] = 2.7
letter_list["d"] = 4.7
letter_list["e"] = 13.0
letter_list["f"] = 2.2
letter_list["g"] = 2.0
letter_list["h"] = 6.2
letter_list["i"] = 6.9
letter_list["j"] = 0.26
letter_list["k"] = 0.81
letter_list["l"] = 4.0
letter_list["m"] = 2.7
letter_list["n"] = 6.7
letter_list["o"] = 7.8
letter_list["p"] = 1.9
letter_list["q"] = 0.11
letter_list["r"] = 5.9
letter_list["s"] = 6.2
letter_list["t"] = 9.6
letter_list["u"] = 2.7
letter_list["v"] = 0.97
letter_list["w"] = 2.4
letter_list["x"] = 0.15
letter_list["y"] = 2.0
letter_list["z"] = 0.078
letter_list[" "] = 5

def score(string):

	s = 0

	for letter in string:
		
		try:
			s += letter_list[letter.lower()]
		except:
			pass
	
	return(s)

def k(l):
	
	return(l["score"])

def getscores(data):

	scores = []
	big = 0
	
	for entry in range(len(data)):
		
		entry_score = score(data[entry])	
		
		scores.append({"score": entry_score, "entry": data[entry]})
	
	scores.sort(key=k)

	try:
		return(scores[-1])
	except:
		pass

def runner(x):

	outs = repeating_key(x)
	return(getscores(outs))

# print(runner(hex_string))
