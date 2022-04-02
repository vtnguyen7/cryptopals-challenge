# Single gyte xor

import base64
import challenge1 as tools

hex_string = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# define a list of outputs and write to the outputs each xor

outs = []

for i in range(256):

	outs.append("".join([chr(int(b) ^ i) for b in hex_string]))

letter_list = {"e": 11.16, "a": 8.50, "r":7.58 , "i": 7.54, "o": 7.16, "t": 6.85, "n": 6.65, "s": 5.74, "l": 5.49, "c": 4.54, "u": 3.63, "d": 3.38, "p": 3.17, "m": 3.01, "h": 3.00}



def score(string):

	s = 0

	for letter in string:
		
		try:
			s += letter_list[letter]
		except:
			pass
	
	return(s)

scores = []
big = 0

for entry in range(len(outs)):
	
	entry_score = score(outs[entry])	
	
	scores.append({"score": entry_score, "entry": outs[entry]})

def k(l):

	return(l["score"])

scores.sort(key=k)

for entry in scores:

	if entry["score"] > 0:
		
		print(entry["entry"])
