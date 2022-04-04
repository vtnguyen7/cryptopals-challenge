text = "YELLOW SUBMARINE"

def padder(byts, number):

	diff = number - len(byts)

	if diff < 0:
		
		raise Exception("your input is too big!!!")

	else:

		return(byts + b'\x04' * diff)

#print(padder(bytearray(text, "utf-8"), 20))	
