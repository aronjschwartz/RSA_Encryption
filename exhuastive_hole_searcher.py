#Program: Analyzes all holes for all possible septuple combinations up to the end of the prime list
#Author: Aron Schwartz
#Last Edit: 10/25/2019

import encrypt
import time
import csv

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
	
	
	header = ["p, q, n, Phi, e, k d","# holes", "Left Holes","Right Holes"]
	with open("holes.csv", "w") as csv_file:
		writer = csv.writer(csv_file,  dialect='excel')
		writer.writerow(header)

            
	#List of the first few primes 
	p_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
	q_list = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
	e_list_1 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
	e_list_2 =  [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
	p_index = 0
	q_index = 0
	e_index = 0
	
	
	
	
	active_e_list = []
	for p_val in p_list:
		for q_val in q_list:
			
			e_index = 0
			if (active_e_list == e_list_1):
				print("LIST IS 1, BECOMING 2")
				active_e_list = e_list_2
			elif (active_e_list == e_list_2):
				print("LIST IS 2, BECOMING 1")
				active_e_list = e_list_1
			else:
				active_e_list = e_list_1
			#Check all the public keys for each p/q combination
			reference_object = encrypt.encryption_set(p=p_val, q=q_list[q_index])
			reference_object.generate_all_possible_e()
			#e_list = reference_object.valid_e_list
			
			while(1):
				temp_object = encrypt.encryption_set(p=p_list[p_index], q=q_list[q_index], custom_e=active_e_list[e_index])
				sept = temp_object.get_septuple();
				holes_list = search_septuple(temp_object)
				holes_num = len(holes_list)
				
				#csv_entry = [
				print(sept, " holes = ", holes_list)
				
				
				
				e_index +=1
				if (e_index == (len(active_e_list) - 1)):
					break
		q_index +=1
run()	
	
	