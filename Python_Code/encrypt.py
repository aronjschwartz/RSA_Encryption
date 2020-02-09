#********************************************************
#*                                                  
#* File:        encrypt.py
#* Description: Implements the RSA encryption algorithm as a 
#* 				python class.  
#*
#* Author: Aron Schwartz
#* Last Edit: 2/2/2020
#*
#********************************************************

from math import gcd as bltin_gcd
import random
import math
import time
import json


#Simple function to check for co-primality 
def check_coprimality(a, b):
    return bltin_gcd(a, b) == 1

#Define the RSA encryption object
class encryption_set():

	#Initialization function accepts, at minimum, the p and q values.  Allows customization or automatic generation of other variables
	def __init__(self, p, q, custom_e=None, custom_d=None, custom_k =None):
		#Assign the P and Q values
		self.p = p
		self.q = q
		
		#Assign the n value, which is the product of P and Q
		self.n = p*q
		
		#Assign the totient value
		self.totient = self.generate_totient(p, q)
		
		#Debug mode is false as the default
		self.debug = False
			
		#If no e value is specified, generate a valid one
		if (custom_e == None):
			self.e = self.generate_random_valid_e()
		#Otherwise set the e value to the custom value that was passed in
		else:
			self.e = custom_e
		
		#If no d value is passed in, generate a valid one
		if (custom_d == None):
			self.d = self.generate_random_valid_d()
		#Otherwise set the d value to the custom value that was passed in
		else:
			self.d = custom_d
			
		#Set the k if a custom one is passed, otherwise it will be generated when we create a valid d
		if custom_k != None:
			self.k = custom_k
		
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
	
	def verify_e_swap(self, new_e_value):
		if check_coprimality(self.totient, new_e_value):
			return True
		return False
	#Function to swap out the E value for use in the RSA sandbox
	def swap_out_e_value(self, new_e_value):
		self.e = new_e_value
		self.d = self.generate_random_valid_d()   #Generate a new d value based on the new e value
		return 
	
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
	
	#Function to encrypt a list of integers
	def encrypt_int_list(self, plaintext_list):
		cipher_list = []
		for i in plaintext_list:
			cipher_list.append(self.encrypt_int(int(i)))
		return cipher_list
	
	#Function to decrypt a list of integers
	def decrypt_int_list(self, cipher_list):
		plaintext_list = []
		for i in cipher_list:
			plaintext_list.append(self.decrypt_int(int(i)))
		return plaintext_list
	
	#Function to search for all fixed points in the septuple
	def search_holes(self):
		#Hole counter
		holes = 0
		count = 2
		while(1):
			if ((int(self.encrypt_int(count))) == count):
				holes +=1
			count +=1
			if count == int((self.n)/2):   #Take advantage of symmetry for faster search, only search up to n/2 and double it
				break
		return holes*2
	
	
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
	
	#Function to disable debug mode
	def disable_debug_mode(self):
		self.debug = False
	
	#Function to fetch N
	def get_n(self):
		return self.n
	
	#Function to fetch P
	def get_p(self):
		return self.p
		
	#Function to fetch Q
	def get_q(self):
		return self.q
	
	
	#Function to fetch e
	def get_e(self):
		return self.e
	
	#Function to obtain the full septuple as a list of form [P, Q, N, Totient, E, K, D]
	def get_septuple(self):
		return [self.p, self.q, self.n, self.totient, self.e, self.k, self.d]
	