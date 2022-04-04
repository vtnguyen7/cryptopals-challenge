import challenge3 as c3

file = open("4.txt", "r")
strings = file.readlines()

topscore = []

for string in strings:

	s = bytearray.fromhex(string)
	result = c3.getscores(c3.repeating_key(s))

	if result != None:
		topscore.append(c3.getscores(c3.repeating_key(s)))

topscore.sort(key=c3.k)

print(topscore[-1])
