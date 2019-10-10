#Program: This file encrypts an integer using the RSA method
#Author: Aron Schwartz
#Last edit: 10/5/2019

#Found this on stack overflow, efficient and quick way to check for co-primality
from math import gcd as bltin_gcd
import random
import math
import mod


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
		self.totient = self.generate_totient(p, q)
		self.e = 7
		self.d = 31
		#self.e = self.generate_e(self.totient)
		#self.d = self.generate_d()
		
	#e must be a value that is: less than n, coprime with the totient, satisfies m^e > n where 'm' is the integer to be transformed

	def generate_e(self, totient):   
		candidate_found = False
		while(candidate_found == False):
			rand_num = random.sample(range(2, self.n), 1)[0]
			if ((rand_num < self.n) and (check_coprimality(totient, rand_num))): #and ((math.pow(127, rand_num) > self.n))): #128 for ascii
				print("CANDIDATE FOUND: ", rand_num)
				break
			else:
				print("BAD CANDIDATE: ", rand_num)
				#print("N: ", self.n)
				#print("TOTIENT" , self.totient)
				#print("Coprimaility: ", check_coprimality(totient, rand_num))
				#print("M** ", rand_num, ": ", math.pow(self.m, rand_num))
		return rand_num	
	
	def generate_totient(self, p, q):
		return ((p-1)*(q-1))
	
	def generate_d(self):
		return (mod.Mod(1, self.totient))/self.e
	
	def generate_cypher(self, val):
		return mod.Mod(math.pow(val, self.e), self.n)
	
	def generate_plain(self, val):
		return mod.Mod(math.pow(val, self.e), self.n)
	
	def to_String(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		#print("M: ", self.m)
		print("N: ", self.n)
		print("T: ", self.totient)
		print("E: ", self.e)
		print("D: ", self.d)
	
	
def main():
	#Create an RSA encryption set object
	RSA_object = encryption_set(2, 19)
	plain_text = "Aron is rather cool"
	
	#List to hold the ascii values for each character in the plain text
	plain_text_ascii = []
	
	#List to hold the transformed ascii value for each character in the cypher text
	cipher_ascii = []
	
	#Var to hold the cipher text equivalent of the plain text
	cipher_text = ""
	
	decrypted_cipher_ascii = []
	#Var to hold the decyrpted cipher text, which should equal the plain text if functioning properly
	decrypted_cipher_text = ""
	
	
	
	RSA_object.to_String()
	
	#Obtain a list of ascii values for the plain text
	plain_text_ascii = get_ascii_list(plain_text)
	
	for i in plain_text_ascii:
		cipher_ascii.append(int(RSA_object.generate_cypher(i)))

	
	cipher_text = get_string_from_ascii(cipher_ascii)
	#Test now that decrpyting cipher text results in original plain text
	for i in cipher_ascii:
		decrypted_cipher_ascii.append(RSA_object.generate_plain(i))
	
	for i in decrypted_cipher_ascii:
		decrypted_cipher_text += chr(int(i))

		
	print("Plain text: ", plain_text)
	print("Cipher text: ", cipher_text)
	print("Decrypted cipher text: ", decrypted_cipher_text)
	
	val = 9
	test_list = range(2, 37)
	encrytped_test_list = []
	decrypted_test_list = []
	for i in test_list:
		print("Encrypting val: ", i, "Result: ", int(RSA_object.generate_cypher(i)))
		encrytped_test_list.append(int(RSA_object.generate_cypher(i)))
		
	for i in encrytped_test_list:
		print("Decrytping val: ", i, "Result: ", int(RSA_object.generate_plain(i)))
main()


