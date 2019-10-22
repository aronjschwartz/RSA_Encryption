#Program: Finds all holes for a given RSA object
#Author: Aron Schwartz
#Last Edit: 10/21/2019


#Interesting post: https://security.stackexchange.com/questions/2335/should-rsa-public-exponent-be-only-in-3-5-17-257-or-65537-due-to-security-c

import encrypt
import csv


public_keys = [3, 5, 17, 257, 65537]

def analyze_holes(list):
	print("Holes found: ", len(list))
	for i in list:
		print(i)


#Function takes a RSA object and returns a list of all holes from 2 to n-2
def search_septuple(rsa_object):
	
	#List to hold the holes
	holes = []
	#Generate the plaintext list of integers
	integer_list = [i for i in range(2, rsa_object.n-1)]
	#List to hold the encrypted integers
	encrypted_integers = []
	
	#Encrypt all the integers and store them in the encrypted integer list
	for i in integer_list:
		encrypted_integers.append(int(rsa_object.encrypt_int(i)))
	
	#Loop through the original list and check for all cases where the plaintext=cipher text
	for index, val in enumerate(integer_list):
		if integer_list[index] == encrypted_integers[index]:
			holes.append(val)
	return holes
	
def run():
	
	
	#EVEN N IS NOT GOOD!  ANY EVEN N HAS 1 prime factor = 2! This pair caused 3 holes....but I know why now
	three_holes_pair = [2,19]
	test_pair = [3,19]
	holes_list = []
	
	#Reference object to access original p,q,n,t
	reference_object = encrypt.encryption_set(p=test_pair[0], q=test_pair[1])
	
	header = "P=" + str(reference_object.p) + " Q=" + str(reference_object.q) + " N=" + str(reference_object.n) + " T=" + str(reference_object.totient)
	
	#First obtain a list of all possible public keys for the object undergoing test
	valid_e_list = reference_object.valid_e_list
	
	#Welcome message and print out the p,q,n, t that we are about to analyze
	print("********* Analyzing data ***********")
	print(reference_object.print_p_q_n_t())
	
	
	#Loop through all potential public keys
	#For each public key, find all possible d/k combos that work for that key, and see how many holes the septuple has
	for public_key in valid_e_list:
		combos = []
		holes_in_pair = 0
		
		#Create an encryption object with the current public key being checked
		temp_object = encrypt.encryption_set(p=test_pair[0], q=test_pair[1], custom_e=public_key)
		
		#Get all the d/k combos that could work with the public key being checked
		combos = temp_object.generate_all_d_k_combinations(public_key)
	
		print("\nTesting public key: ", public_key)
		for pair in combos:
			
			temp_object_two = encrypt.encryption_set(p=test_pair[0], q=test_pair[1], custom_e=public_key, custom_d = pair[0], custom_k = pair[1])
			holes_in_pair = search_septuple(temp_object_two)
			print("Pair d=", pair[0], " k=", pair[1], " has ", len(holes_in_pair), " holes")

		
	
	
	
	with open('csvfile.csv','w') as file:
		file.write(header)
		file.write('\n')
		file.write('E-D-K:')
		#file.write(str(test_object.e) + " " + str(test_object.d) + " " + str(test_object.k))
		#file.write(',Holes: ' + str(len(holes_list)))
	
	
run()	
	
	
	
	
	
	
	
	
	
