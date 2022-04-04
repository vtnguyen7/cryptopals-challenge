import challenge3 as c3
import challenge1 as c1

key = "ICE"

message = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

def splitter(lenk, m):

	l = []

	for i in range(lenk):

		l.append([])

	for i in range(len(m)):

		l[i % lenk].append(m[i])

	for i in range(lenk):

		l[i] = bytearray("".join(l[i]), "utf-8")

	return(l)

def combiner(lenk, marray):

	outbyte = b''

	for i in range(len(marray[0])):

		for j in range(lenk):

			try:
				outbyte += c1.int_to_bytes(marray[j][i])
			except:
				pass

	return(outbyte)

def repeating_key_xorer(k, m):

	ms = splitter(len(k), m)
	
	l = []

	for i in range(len(k)):

		repeater = bytearray(k[i] * len(ms[i]), "utf-8")
		l.append(c3.xor(repeater, ms[i]))

	return(l)

#print(combiner(len(key), repeating_key_xorer(key, message)).hex())
