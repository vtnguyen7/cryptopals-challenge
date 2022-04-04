from Crypto.Cipher import AES

f = open("8.txt", "r")
ciphertexts = [bytearray.fromhex(x.strip("\n")) for x in f.readlines()]

blocktexts = []

for t in range(len(ciphertexts)):

	blocktexts.append([])

	for i in range((len(ciphertexts[t]) // 16)):
		
		blocktexts[t].append(ciphertexts[t][16*i:16*(i + 1)])

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

freqs = []

for i in range(len(blocktexts)):
	
	freqs.append({"text": blocktexts[i], "frequency_count": freq_count(blocktexts[i])})

for i in freqs:

	if i["frequency_count"][-1]["count"] > 1:

		print("".join([x.hex() for x in i["text"]]))
