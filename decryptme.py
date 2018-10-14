#importsssss
try:
	import string
	import base64
	import sys
except ImportError:
	exit(1)

def rot13_text():
	rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	plaintext = string.translate(cipher, rot13)
	print plaintext
	exit(1)

def base64_text():
	plaintext = base64.b64decode(cipher)
	print plaintext
	exit(1)

#creating vars and handling exceptions
try:
	whatisit = sys.argv[1]
	encryption = sys.argv[2]
	cipher = sys.argv[3]
except IndexError:
	print "usage: "
	print "decryptme -f <encryption> <file>"
	print "or"
	print "decryptme -t <encryption> 'ciphertext'"

def main():
	if whatisit == "-t":
		if encryption == "rot13":
			rot13_text()
		elif encryption == "base64":
			base64_text()
		else:
			exit(1)
	elif whatisit == "-f":
		if encryption == "rot13":
			rot13_file()
		elif encryption == "base64":
			base64_file()
		else:
			exit(1)

main()
