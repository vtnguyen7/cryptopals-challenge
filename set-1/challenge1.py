# convert hex to base64

import base64

byt = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex_to_base64(string):

	intrep = int(string, 16)

	byterep = intrep.to_bytes((intrep.bit_length() + 7) // 8, byteorder = "big")

	return(base64.b64encode(byterep))

print(hex_to_base64(byt).decode("ascii"))

## explanation: we use the to_bytes function, it requires number of bytes (number of bites + 7 ensures we have enough mod 8) and endianness (big!)

## we encode the output into base64 and then decode the bytes to ascii
