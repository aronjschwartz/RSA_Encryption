#Program: This file encrypts an integer using the RSA method
#Author: Aron Schwartz
#Last edit: 10/5/2019

#Found this on stack overflow, efficient and quick way to check for co-primality
from math import gcd as bltin_gcd
import random
import math

def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1

def get_ascii_list(input_string):
	out = []
	for i in input_string:
		out.append(ord(i))
	return out
	
def get_string_from_ascii(input_list):
	out = ""
	for i in input_list:
		out += chr(i)	
	return out

#This class accepts 2 prime numbers and generates/stores all associated values to perform the RSA encryption method
class encryption_set():
	#Need the original primes to initialize the object
	def __init__(self, p, q):
		#self.m = 87  #TEMPORARY.  HOW ENSURE PARAMETERS SATISFIED IF THIS ALWAYS CHANGING????
		self.p = p
		self.q = q
		self.n = p*q
		self.k = 12   #For now, but how choose this?
		self.totient = self.generate_totient(p, q)
		self.e = 7
		#self.e = self.generate_e()  #Public key
		self.d = self.generate_d()  #Private key

		#self.d = self.generate_d()
		
	
	
	#Function to generate a valid public key (encryption key)
	def generate_e(self):   
		candidate_found = False
		while(candidate_found == False):
			rand_num = random.sample(range(2, self.n), 1)[0]
			if ((rand_num < self.n) and (check_coprimality(self.totient, rand_num))): 
				break
			else:
				print("BAD CANDIDATE: ", rand_num)
		return rand_num	
	
	#Function to generate a valid private key (decryption key)
	def generate_d(self):
		return int((1 + ((self.k)*(self.totient)))/self.e)
	
	def generate_totient(self, p, q):
		return ((p-1)*(q-1))
	
	
	def encrypt_int(self, val):
		return (val**self.e) % self.n
		
	def decrypt_int(self, val):
		return (val**self.d) % self.n
		
	def to_String(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		print("N: ", self.n)
		print("T: ", self.totient)
		print("E: ", self.e)
		print("D: ", self.d)
		print("K: ", self.k)
	
	
def main():
	#Create an RSA encryption set object
	RSA_object = encryption_set(2, 19)
	plain_text = "Aron is rather cool"
	plain_text_ascii = []
	cipher_ascii = []
	cipher_text = ""
	decrypted_cipher_ascii = []
	decrypted_cipher_text = ""
	encrytped_test_list = []
	decrypted_test_list = []
	
	RSA_object.to_String()
	
	#Obtain a list of ascii values for the plain text
	plain_text_ascii = get_ascii_list(plain_text)

	for i in plain_text_ascii:
		cipher_ascii.append(int(RSA_object.encrypt_int(i)))

	cipher_text = get_string_from_ascii(cipher_ascii)
	#Test now that decrpyting cipher text results in original plain text
	for i in cipher_ascii:
		decrypted_cipher_ascii.append(RSA_object.decrypt_int(i))
	
	for i in decrypted_cipher_ascii:
		decrypted_cipher_text += chr(int(i))

	print("\n\nPlain text: ", plain_text)
	print("\n\nCipher text: ", cipher_text)
	print("\n\nDecrypted cipher text: ", decrypted_cipher_text)
	
	#val = 9
	#test_list = range(2, 37)
	#for i in test_list:
	#	print("Encrypting val: ", i, "Result: ", int(RSA_object.encrypt_int(i)))
	#	encrytped_test_list.append(int(RSA_object.encrypt_int(i)))
	#print()
	#count = 0
	#for i in encrytped_test_list:
	#	print("Decrytping val: ", i, "Result: ", int(RSA_object.decrypt_int(i)), "Originally: ", test_list[count])
	#	count +=1
	

main()


