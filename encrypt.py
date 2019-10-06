#Program: This file encrypts an integer using the RSA method
#Author: Aron Schwartz
#Last edit: 10/5/2019

#Found this on stack overflow, efficient and quick way to check for co-primality
from math import gcd as bltin_gcd
import random

def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1
	
	
	
#This class accepts 2 prime numbers and generates/stores all associated values to perform the RSA encryption method
class encryption_set():
	#Need the original primes to initialize the object
	def __init__(self, p, q):
		self.p = p
		self.q = q
		self.n = p*q
		self.totient = (p-1)*(q-1)
		self.e = self.generate_e(self.totient)
		self.m = 87  #value to encrypt as test
		self.k = 
		
	#e must be a value that is: less than n, coprime with the totient, satisfies m^e > n where 'm' is the integer to be transformed

	def generate_e(self, totient):   
		candidate_found = False
		while(candidate_found == False):
			rand_num = random.sample(range(1, self.n), 1)[0]
			if ((rand_num < self.n) and (check_coprimality(totient, rand_num)) and (self.m^rand_num < self.n)):
				print("CANDIDATE FOUND: ", rand_num)
				break
			else:
				print("BAD CANDIDATE: ", rand_num)
		return rand_num	
	
	
	def encrypt_int(self):
		return 1 #placeholder
	
	def decrypt_int(self):
		return 1 #placeholder
	
def main():
	test = encryption_set(17, 23)
	
	print("The value of e is: ", test.e)
	
main()