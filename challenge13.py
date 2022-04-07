import base64
import random
from Crypto.Cipher import AES

def int_to_bytes(num):

	return(num.to_bytes((num.bit_length() + 7) // 8, byteorder = "big"))

def padder(byts, number):

	return(byts + b'\x04' * (number - (len(byts) % number)))

def parser(string):

	split = [""]

	for i in string:

		if i == "\\":

			pass

		elif i not in ("&"):

			split[-1] += i

		else:

			split.append("")

	entries = []

	for part in split:

		entry = [""]
		pos = 0
		key = ""

		part = part.replace("\x04", "") # removes our padding

		for letter in part:

			if letter == "=":

				if entry[0] == "": # simple check for corruption

					continue

				entry.append("")
				pos = 1

			else:

				entry[pos] += letter

		entries.append(entry)

	newdict = {}

	for e in entries:

		if len(e) != 2: # simple check for corruption

			pass			

		else:

			newdict[e[0]] = e[1]

	return(newdict)

def check_valid_email(email):

	if (isinstance(email, str) and ("@" in email)):

		return(email.replace("&", "").replace("=", ""))		

	else:

		raise Exception("bad email!!")

def profile_for(email):

	out_list = []

	email = check_valid_email(email)

	out_list.append(["email", email])
	out_list.append(["uid", 10])
	out_list.append(["role", "user"])

	running_string = ""

	for o in out_list:

		running_string += o[0] + "=" + str(o[1]) + "&"

	return(running_string[:-1])

key = int_to_bytes(random.randint(1, 256)) * 16

cipher = AES.new(key, AES.MODE_ECB)

def encryptor(x):

	return(cipher.encrypt(padder(bytes(profile_for(x), "utf-8"), 16)))

def size_detector():

	i = 0
	diff = 0

	while diff == 0:

		diff = len(encryptor("m@a" + ("A" * (i + 1)))) - len(encryptor("m@a" + ("A" * i)))
		i += 1

	return(diff)

blocksize = size_detector()

admintext = encryptor("m@a" + (blocksize - 9)*"A" + bytearray.decode(padder(bytearray("admin", "utf-8"), 16), "utf-8"))[16:32]

def remove_role():

	i = -1
	diff = 0

	while diff == 0:

		i += 1
		diff = len(encryptor("m@a" + ("A" * (i + 1)))) - len(encryptor("m@a" + ("A" * i)))

	return(encryptor("m@a" + ("A" * (i + 5)))[:-blocksize])

cut_and_pasted = remove_role() + admintext

print(parser(bytes.decode(cipher.decrypt(encryptor("foo@bar.com")))))
print(parser(bytes.decode(cipher.decrypt(cut_and_pasted), "utf-8")))
