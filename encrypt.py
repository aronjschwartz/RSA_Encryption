#Program: This file encrypts an integer using the RSA method
#Author: Aron Schwartz
#Last edit: 10/5/2019

#Found this on stack overflow, efficient and quick way to check for co-primality
from math import gcd as bltin_gcd
import random
import math

#Simple function to check for co-primality 
def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1

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

#Class to generate all required numbers for an RSA encryption instance.  Needs the two primes for initialization
class encryption_set():

	#Need the original primes to initialize the object
	def __init__(self, p, q):
		#Assign p, q
		self.p = p
		self.q = q
		self.n = p*q
		self.totient = self.generate_totient(p, q)
		self.e = self.generate_e()
		self.d = self.generate_d()
			
	#Function to generate a valid public key (encryption key)
	def generate_e(self):   
		candidate_found = False
		while(candidate_found == False):
			#Generate a random number from 2 to n -1
			rand_num = random.sample(range(2, self.n), 1)[0]
			#Ensure the number is less than n and co-prime with totient as required
			if ((rand_num < self.n) and (check_coprimality(self.totient, rand_num))): 
				break
			else:
				continue
		return rand_num	
	
	#Function to generate a valid private key (decryption key)
	def generate_d(self):
		possible_d = 1
		possible_k = 1
		
		#Loop until we find a decryption key that will work
		while(1):
			possible_d = (1 + (possible_k)*(self.totient))/self.e
			#If the potential decryption-key comes out even, it will work.  Assign appopriately
			if (possible_d.is_integer()):
				print("D candidate found: ", possible_d, " with k value: ", possible_k)
				valid_d = True
				self.k = possible_k
				break
			else:
				#Otherwise increase the value of the k-constant and check again
				possible_k +=1
		#Return the key
		return int(possible_d)
	
	#Return the totient defined as (p-1)*(q-1)
	def generate_totient(self, p, q):
		return ((p-1)*(q-1))
		
	#Function to encrypt an int and return the cipher-value
	def encrypt_int(self, val):
		return (val**self.e) % self.n
	
	#Function to decrypt an int and return the plain-value
	def decrypt_int(self, val):
		return (val**self.d) % self.n
	
	#Function to dump out internal variables for the encryption object
	def to_String(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		print("N: ", self.n)
		print("T: ", self.totient)
		print("E: ", self.e)
		print("D: ", self.d)
		print("K: ", self.k)
	
	
def main():
	#Sample plain text to encrypt
	plain_text = "Aron is a very, VERY cool guy!"
	#Variables to store ascii-lists, plain-text lists, etc
	plain_text_ascii = []
	cipher_ascii = []
	cipher_text = ""
	decrypted_cipher_ascii = []
	decrypted_cipher_text = ""
	encrytped_test_list = []
	decrypted_test_list = []
	
	#Create an RSA encryption set object and print out the values it created for itself
	RSA_object = encryption_set(29, 59)
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
	print("Cipher text: ", cipher_text)
	print("Decrypted cipher text: ", decrypted_cipher_text)
	
main()


