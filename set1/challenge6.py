import challenge3 as c3

message1 = "this is a test"
message2 = "wokka wokka!!!"

def hamming_distance(a, b):

	return(int(c3.xor(a, b)))

m1 = int(bytearray(message1, "utf-8").hex(), 16)
m2 = int(bytearray(message2, "utf-8").hex(), 16)

print(m1)

print(hamming_distance(message1, message2))
