# fixed xor

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

print(hex(int(hex_string1, 16) ^ int(hex_string2, 16)))
