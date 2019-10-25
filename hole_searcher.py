#Program: Finds all holes for a given RSA object
#Author: Aron Schwartz
#Last Edit: 10/21/2019


#Interesting post: https://security.stackexchange.com/questions/2335/should-rsa-public-exponent-be-only-in-3-5-17-257-or-65537-due-to-security-c

import encrypt
import csv



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
	#Return a list of all holes found for the given septuple
	return holes
	
def run():
	
	
	#Even N have only 3 holes, but trivial factoring.  Not useful
	three_holes_pair = [2,19]
	#Standard test pair
	test_pair = [47,59]
	#A bigger pair, takes a while to finish
	huge_pair = [101 , 127]
	huge_pair_1 = [71, 89]
	#Absolutly massive pair.  More computation needed to analyze.  Conda? Fast math libraries for modular/exponents? Other?
	massive_pair  = [3203, 3331]
	
	#These are the common public keys that are commonly used
	public_keys = [3, 5, 17, 257, 65537]
	
	#active_pair = test_pair
	#active_pair = three_holes_pair
	#active_pair = huge_pair
	active_pair = huge_pair
	holes_list = []
	
	
	#Reference object to access original p,q,n,t
	reference_object = encrypt.encryption_set(p=active_pair[0], q=active_pair[1])
	
	#Header for the output file
	header = "P=" + str(reference_object.p) + " Q=" + str(reference_object.q) + " N=" + str(reference_object.n) + " T=" + str(reference_object.totient)
	
	#First obtain a list of all possible public keys for the object undergoing test
	valid_e_list = reference_object.valid_e_list
	#Welcome message and print out the p,q,n, t that we are about to analyze
	print("********* Analyzing data ***********")
	print(reference_object.print_p_q_n_t())
	print("\nThis object has ", len(valid_e_list)," valid public keys\n")
	
	
	
	
	#Loop through all potential public keys
	for public_key in valid_e_list:
		combos = []
		holes_in_pair = 0
		
		#Create an encryption object with the current public key being checked
		temp_object = encrypt.encryption_set(p=active_pair[0], q=active_pair[1], custom_e=public_key)
		
		#Get all the d/k combos that could work with the public key being checked
		combos = temp_object.generate_all_d_k_combinations(public_key)
	
		print("\nTesting public key: ", public_key)
		for pair in combos:
			
			temp_object_two = encrypt.encryption_set(p=active_pair[0], q=active_pair[1], custom_e=public_key, custom_d = pair[0], custom_k = pair[1])
			holes_in_pair = search_septuple(temp_object_two)
			print("Pair d=", pair[0], " k=", pair[1], " has ", len(holes_in_pair), " holes")
			break #THIS BREAK STATEMENT WILL CAUSE STOP AFTER EACH PUBLIC key
			#Public keys ALWAYS have the same number of holes regardless of d/k.  Interesting
			#Mathematical relations? How do hole numbers relate to public keys? There are answers in the math
		
	#temp_object = encrypt.encryption_set(p=active_pair[0], q=active_pair[1], custom_e=17, custom_d=157, custom_k=1)
	#holes_in_pair = search_septuple(temp_object)
	#print("Found ", len(holes_in_pair), " holes")
	#print(holes_in_pair)
	
	with open('csvfile.csv','w') as file:
		file.write(header)
		file.write('\n')
		file.write('E-D-K:')
		#file.write(str(test_object.e) + " " + str(test_object.d) + " " + str(test_object.k))
		#file.write(',Holes: ' + str(len(holes_list)))
	
	
run()	
	
	
	
	
	
	
	
	
	