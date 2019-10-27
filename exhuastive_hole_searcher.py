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
	p_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	q_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	e_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
	
	for p_val in p_list:
		for q_val in q_list:
			for e_val in e_list:
			
				#Ignore repeat cases and cases where p==q
				if q_val > p_val:
					try:
						temp_object = encrypt.encryption_set(p=p_val, q=q_val, custom_e=e_val)
						sept = temp_object.get_septuple();
						holes_list = search_septuple(temp_object)
						holes_num = len(holes_list)
						left_holes = []
						right_holes = []
						for index, val in enumerate(holes_list):
							if (index < (len(holes_list)/2)):
								left_holes.append(val)
							else:
								right_holes.append(val)
						print("Analyzing sept: ", sept)
						
						with open("holes.csv", "a", newline='') as csv_file:
							writer = csv.writer(csv_file,  dialect='excel')
							csv_entry = [sept, holes_num, left_holes, right_holes]
							writer.writerow(csv_entry)
					
					except Exception as e: 
						print("Exception occured: ", str(e))
								
run()	
	
	