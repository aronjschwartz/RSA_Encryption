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
	test_pair = [2, 19]
	holes_list = []
	
	#Reference object stores original p, q, n, t
	reference_object = encrypt.encryption_set(p=test_pair[0], q=test_pair[1])
	header = "P=" + str(reference_object.p) + " Q=" + str(reference_object.q) + " N=" + str(reference_object.n) + " T=" + str(reference_object.totient)
	#First obtain a list of all possible public keys for the object undergoing test
	valid_e_list = reference_object.valid_e_list


	#Loop through all potential public keys
	#For each public key, find all possible d/k combos that work for that key
	#For each valid d/k combo found, check how many holes there are from 2 to n-2
	
	print("********* Analyzing data ***********")
	print(reference_object.print_p_q_n_t())
	
	for public_key in valid_e_list:
		combos = []
		combos = temp_object.generate_all_d_k_combinations(public_key)
		temp_object = encrypt.encryption_set(p=test_pair[0], q=test_pair[1], custom_e=public_key)

		print("\nTesting key: ", public_key)
		print("\tValid d/k combos: ", end='')
		for pair in combos:
			print(pair, end=" ")
		
	
	
	
	with open('csvfile.csv','w') as file:
		file.write(header)
		file.write('\n')
		file.write('E-D-K:')
		#file.write(str(test_object.e) + " " + str(test_object.d) + " " + str(test_object.k))
		#file.write(',Holes: ' + str(len(holes_list)))
	
	
run()	
	
	
	
	
	
	
	
	
	
