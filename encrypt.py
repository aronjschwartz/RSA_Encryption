#Program: This file encrypts an integer using the RSA method
#Author: Aron Schwartz
#Last edit: 10/5/2019

#Found this on stack overflow, efficient and quick way to check for co-primality
from math import gcd as bltin_gcd
import random
import math
import time
#Simple function to check for co-primality 
def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1

#Class to generate all required numbers for an RSA encryption instance.  Needs the two primes for initialization
class encryption_set():

	#Need the original primes to initialize the object
	def __init__(self, p, q, custom_e=None, custom_d=None, custom_k =None):
		#Assign p, q, n, and totient
		self.p = p
		self.q = q
		self.n = p*q
		self.totient = self.generate_totient(p, q)
		
		self.valid_e_list =[]
			
		
		
		#Make randomly valid keys if none are passed in, otherwise set the the specified value
		if (custom_e == None):
			self.e = self.generate_random_valid_e()
		else:
			self.e = custom_e
		if (custom_d == None):
			self.d = self.generate_random_valid_d()
		else:
			self.d = custom_d
			
		#Set the k if a custom one is passed, otherwise it will be generated when we create a valid d
		if custom_k != None:
			self.k = custom_k
	

	def generate_all_possible_e(self):
		for i in range(2, self.n):
			if (check_coprimality(self.totient, i)):
				self.valid_e_list.append(i)
		
		
	def generate_all_d_k_combinations(self, temp_e):
		
		dk_list = []		
		possible_d = 1
		#Check all 'k' values from 2 to n.  Extract all valid k/d combinations
		for possible_k in range(2, self.n):
			possible_d = (1 + (possible_k)*(self.totient))/temp_e
			#If the potential decryption-key comes out as a whole integer, it will work as a valid decryption key
			if (possible_d.is_integer()):
				dk_list.append([int(possible_d), int(possible_k)])
				
			possible_k +=1
				
				
		return dk_list
	
	#Function to generate a valid public key (encryption key)
	def generate_random_valid_e(self):   
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
	def generate_random_valid_d(self):
		possible_d = 1
		possible_k = 1
		
		#Loop until we find a decryption key that will work.  Must satisfy d = (1 + (k)(totient))/e
		while(1):		
			possible_d = (1 + (possible_k)*(self.totient))/self.e
			#If the potential decryption-key comes out as a whole integer, it will work as a valid decryption key.  Assign appopriately and break 
			if (possible_d.is_integer()):		
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
	
	def print_p_q_n_t(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		print("N: ", self.n)
		print("T: ", self.totient)
	
	
	def get_septuple(self):
		return [self.p, self.q, self.n, self.totient, self.e, self.k, self.d]
	
	def to_list(self):
		return [self.p, self.q, self.n, self.totient, self.e, self.d, self.k]