#Program: This file implements the RSA python encyrption object code
#Author: Aron Schwartz
#Last edit: 12/9/2019


from math import gcd as bltin_gcd
import random
import math
import time

#Simple function to check for co-primality 
def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1

#Encryption object
class encryption_set():

	#Need P and Q at minimum to initialize the object
	def __init__(self, p, q, custom_e=None, custom_d=None, custom_k =None):
		#Assign p, q, n, and totient
		self.p = p
		self.q = q
		self.n = p*q
		self.totient = self.generate_totient(p, q)
		
		self.valid_e_list =[]
		#Debug mode default to false
		self.debug = False
			
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
	
	#Function to make a list of all valid E from 2 to N
	def generate_all_possible_e(self):
		if (self.debug == True):
			print("Generating all possible e-values")
		for i in range(2, self.n):
			if (check_coprimality(self.totient, i)):
				self.valid_e_list.append(i)
		
	#Function to generate all D/K combinations
	def generate_all_d_k_combinations(self, temp_e):
		
		dk_list = []		
		possible_d = 1
		if (self.debug):
			print("Generating all possible d/k combinations")
		#Check all 'k' values from 2 to n.  Extract all valid k/d combinations
		for possible_k in range(2, self.n):
			possible_d = (1 + (possible_k)*(self.totient))/temp_e
			#If the potential decryption-key comes out as a whole integer, it will work as a valid decryption key
			if (possible_d.is_integer()):
				dk_list.append([int(possible_d), int(possible_k)])			
			possible_k +=1				
		return dk_list
	
	#Function to generate a valid E
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
		if (self.debug == True):
			print("Generated e: ", str(rand_num))
		return rand_num	
	
	#Function to generate a valid D
	def generate_random_valid_d(self):
		possible_d = 1
		possible_k = 1
		if (self.debug == True):
			print("Generating valid value for d")
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
				
			#Catch infinite loop 
			if (possible_d > self.n):
				self.d = 1
				self.k = 1
				break
		#Return the key
		if (self.debug == True):
			print("Generated d value: ", int(possible_d))
		return int(possible_d)
	
	#Return the totient defined as (p-1)*(q-1)
	def generate_totient(self, p, q):
		return ((p-1)*(q-1))
		
	#Function to encrypt an int and return the cipher-value
	def encrypt_int(self, val):
		if (self.debug == True):
			print("Encrypting int: ", val)
		
		return pow(val, self.e, self.n)
		
	
	#Function to decrypt an int and return the plain-value
	def decrypt_int(self, val):
		if (self.debug == True):
			print("Decrypting int: ", val)
		return pow(val, self.d, self.n)
		
	
	#Function to dump out internal variables for the encryption object
	def to_String(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		print("N: ", self.n)
		print("T: ", self.totient)
		print("E: ", self.e)
		print("D: ", self.d)
		print("K: ", self.k)
	
	#Function to print out P, Q, N, Totient
	def print_p_q_n_t(self):
		print("P: ", self.p)
		print("Q: ", self.q)
		print("N: ", self.n)
		print("T: ", self.totient)
	
	#Functions to enable or disable debug printing
	def enable_debug_mode(self):
		self.debug = True
		
	def disable_debug_mode(self):
		self.debug = False
	
	#Function to fetch N
	def get_n(self):
		return self.n
	
	def get_e(self):
		return self.e
	
	#Function to obtain the full septuple as a list of form [P, Q, N, Totient, E, K, D]
	def get_septuple(self):
		return [self.p, self.q, self.n, self.totient, self.e, self.k, self.d]
	
	def to_list(self):
		return [self.p, self.q, self.n, self.totient, self.e, self.d, self.k]