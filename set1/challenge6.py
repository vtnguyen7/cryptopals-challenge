# the output is kinda doge, but I see this as an absolute win!

import challenge5 as c5
import challenge3 as c3
import challenge1 as c1
import base64

message1 = "this is a test"
message2 = "wokka wokka!!!"

m1 = bytearray(message1, "utf-8")
m2 = bytearray(message2, "utf-8")

f = open("6.txt", "r")
opened = [x.strip("\n") for x in f.readlines()]
message = bytearray(base64.b64decode("".join(opened)))

def hamming_distance(l):

	ham = 0

	current = l[0]

	for i in range(1, len(l)):

		current = c3.xor(current, l[i])		

	run = int(current.hex(), 16)

	while run > 0:

		ham += run % 2

		run = run // 2

	return(ham)

def norm(x):

	return(x["normed_ham"])

def keysize_finder(m, values, n):

# takes in a message, keysizes to try, and number of blocks to xor

	dist = []

	for L_k in values:
		
		blocks = []

		for j in range(n):

			blocks.append(m[L_k*j: L_k*(j + 1)])
		
		dist.append({"size": L_k, "normed_ham": float(hamming_distance(blocks)) / (L_k)})

	dist.sort(key=norm)
	return(dist)

run1 = keysize_finder(message, range(1, 32), 2)
run2 = keysize_finder(message, [x["size"] for x in run1], 10)

# it looks like 29 is the keysize

def byte_splitter(lenk, m):

	l = []

	for i in range(lenk):

		l.append([])

	for i in range(len(m)):

		l[i % lenk] += c1.int_to_bytes(m[i])

	for i in range(len(l)):

		l[i] = bytearray(l[i])

	return(l)

splitted = byte_splitter(29, message)

newsplit = []

for i in splitted:

	newsplit.append(bytearray(c3.runner(i)["entry"], "ascii"))

print(c5.combiner(29, newsplit))
