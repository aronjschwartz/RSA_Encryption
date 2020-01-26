#Program: Simply program to ensure the functionality of the RSA encryption.  Enrypts a plaintext, shows the cipher, and decrypts back to original plain text
#Author: Aron Schwartz
#Last edit: 12/9/2019

import encrypt

#Function to return an ascii list from a string
def get_ascii_list(input_string):
	out = []
	for i in input_string:
		out.append(ord(i))
	return out

#Function to return a string from an ascii list
def get_string_from_ascii(input_list):
	out = ""
	for i in input_list:
		out += chr(i)	
	return out

def main():
	#Sample plain text to encrypt
	plain_text = "But soft, what light from yonder window breaks? It is the East...and Juliet is the Sun"
	
	
	#Variables to store ascii-lists, plain-text lists, etc
	plain_text_ascii = []
	cipher_ascii = []
	cipher_text = ""
	decrypted_cipher_ascii = []
	decrypted_cipher_text = ""
	encrytped_test_list = []
	decrypted_test_list = []
	
	#Create an RSA encryption set object and print out the values it created for itself
	RSA_object = encrypt.encryption_set(47, 59)
	RSA_object.to_String()
	
	#Obtain a list of ascii values for the plain text
	plain_text_ascii = get_ascii_list(plain_text)

	#Encrypt each number in the plain-text ascii list to obtain the cipher-ascii list
	for i in plain_text_ascii:
		cipher_ascii.append(int(RSA_object.encrypt_int(i)))
		
	#Generate the cipher text from the cipher-ascii list
	cipher_text = get_string_from_ascii(cipher_ascii)
	
	
	#Decrypt the cipher-ascii.  This should result back to the original plain-ascii list
	for i in cipher_ascii:
		decrypted_cipher_ascii.append(RSA_object.decrypt_int(i))
	
	#Generate the plain-text from the plain-ascii
	for i in decrypted_cipher_ascii:
		decrypted_cipher_text += chr(int(i))
	
	#Display the original plain text, cipher text, and the decrypted_cipher_text (which should equal the plain text)
	print("\n\nPlain text: ", plain_text)
	print("\nCipher text: ", cipher_text)
	print("\nDecrypted cipher text: ", decrypted_cipher_text)
	

