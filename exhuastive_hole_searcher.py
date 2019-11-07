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
	
def load_primes(file_name):
	primes = []
	f = open(file_name, 'r')
	for line in f:
		if len(line) > 1:
			split = line.split(" ")
			for val in split:
				if val.isnumeric():
					primes.append(int(val))
	return primes

def get_number_primes_to_analyze():
	
		#Loop until valid input entered
		while(1):
			choice = input("Enter number of primes to check: ")
			try:
				if int(choice) > 0:
					return int(choice)
				else:
					print("Positive numbers only")
					choice = input("Enter number of primes to check:  ")
			except Exception as e:
				print("Exception occured: ", str(e))
				continue
		return choice

def run():
	
	prime_list = load_primes("primes1.txt")
	choice = get_number_primes_to_analyze()
	print("Analyzing the first ", choice, " primes")
	time.sleep(3)
	
	
	file_name = "./Excel_Data/first_" + str(choice) + "primes_holes.csv"
	header = ["p, q, n, Phi, e, k, d", "n", "e", "# holes", "Left Holes","Right Holes"]
	with open(file_name, "w") as csv_file:
		writer = csv.writer(csv_file,  dialect='excel')
		writer.writerow(header)
    
	

	p_list = prime_list[0:choice+1]
	q_list = prime_list[0:choice+1]
			  
	e_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
	
	#Loop through all p/q combinations trying each e-value for all combinations
	start_time = time.time()
	for p_val in p_list:
		for q_val in q_list:
			for e_val in e_list:
			
				#Ignore repeat cases and cases where p==q
				if q_val > p_val:
					try:
						#Make a temp object for the current septuple
						temp_object = encrypt.encryption_set(p=p_val, q=q_val, custom_e=e_val)
					#	temp_object.enable_debug_mode()
						sept = temp_object.get_septuple();
						
						#Analyze the holes in the septuple
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
						
						#Append to the output file 
						with open(file_name, "a", newline='') as csv_file:
							writer = csv.writer(csv_file,  dialect='excel')
							csv_entry = [sept,temp_object.get_n(), e_val, holes_num, left_holes, right_holes]
							writer.writerow(csv_entry)
					
					except Exception as e: 
						print("Exception occured: ", str(e))
	end_time = time.time()
	elapsed_time = end_time - start_time
	
	start_time_readable = time.ctime(int(start_time))
	end_time_readable = time.ctime(int(end_time))
	
	elapsed_time_minutes = round(float(elapsed_time)/60.0, 2)
	mins_string = str(elapsed_time_minutes) + " minutes"
	print("Start time: ", start_time_readable)
	print("End time: ", end_time_readable)
	print("Program duration: ", mins_string)
	
	time_header = ["Start Time", "End Time", "Elapsed time"]
	with open(file_name, "a", newline='') as csv_file:
		writer = csv.writer(csv_file,  dialect='excel')
		csv_entry = [start_time_readable, end_time_readable, mins_string]
		writer.writerow("")
		writer.writerow(time_header)
		writer.writerow(csv_entry)
run()	
	
	