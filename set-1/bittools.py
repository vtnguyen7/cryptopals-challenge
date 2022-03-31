import base64

def code2int(s, b):

# (string, base) -> integer

	return(int(s, base=b))

def code2bits(s, b):

# (string, base) -> bit array

	return(bin(int(s, base=b)))
