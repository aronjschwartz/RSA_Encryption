#Program: Analyzes all holes for all possible septuple combinations up to the end of the prime list
#Author: Aron Schwartz
#Last Edit: 12/9/2019

import encrypt
import time
import csv
import traceback

#Function takes a RSA object and returns a list of all holes from 2 to n-2
def search_septuple(rsa_object):
	#Hole counter
	holes = 0
	count = 2
	while(1):
		if ((int(rsa_object.encrypt_int(count))) == count):
			holes +=1
		count +=1
		if count == rsa_object.n-1:
			break
	return holes

#Function to load primes from input file
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

#Function to prompt user for the starting prime index
def get_start_prime():
	#Loop until valid input entered
		while(1):
			choice = input("Enter start prime: ")
			try:
				if int(choice) > 0:
					return int(choice)
				else:
					print("Positive numbers only")
					choice = input("Enter start prime:  ")
			except Exception as e:
				print("Exception occured: ", str(e))
				continue
		return choice

#Function to prompt user for the ending prime index	
def get_end_prime():
	#Loop until valid input entered
		while(1):
			choice = input("Enter end prime: ")
			try:
				if int(choice) > 0:
					return int(choice)
				else:
					print("Positive numbers only")
					choice = input("Enter end prime:  ")
			except Exception as e:
				print("Exception occured: ", str(e))
				continue
		return choice
	
	
#Primary execution function
def run():
	#Get handle to prime list file
	prime_list = load_primes("primes1.txt")
	#Get the start and end choice
	start_choice = get_start_prime()
	end_choice = get_end_prime()
	print("Analyzing prime ", start_choice, " to prime ", end_choice, " in first million primes")
	time.sleep(3)
	
	#Create file name from the start/end choices
	file_name = "./Excel_Data/prime_" + str(start_choice) + "_to_" + str(end_choice) + "_holes.csv"
	header = ["p, q, n, Phi, e, k, d", "n", "totient", "e", "# holes", "Transparency Percentage"]
	with open(file_name, "w") as csv_file:
		writer = csv.writer(csv_file,  dialect='excel')
		writer.writerow(header)
    
	
	#Create our prime lists
	p_list = prime_list[start_choice-1:end_choice-1]
	q_list = prime_list[start_choice-1:end_choice-1]
	print("Start val: ", prime_list[start_choice-1], " End val: ", prime_list[end_choice -1])
	pub_keys = [3, 5, 17, 257, 65537]
	#Loop through all p/q combinations trying each e-value for all combinations
	start_time = time.time()
	for p_val in p_list:
		for q_val in q_list:
			for e_val in pub_keys:
				#Ignore repeat cases and cases where p==q
				if q_val > p_val:
					try:
						#Make a temp object for the current septuple
						temp_object = encrypt.encryption_set(p=p_val, q=q_val, custom_e=e_val)
						#temp_object.enable_debug_mode()
					
						sept = temp_object.get_septuple();
						
						#Analyze the holes in the septuple
						holes_num = search_septuple(temp_object)
						
						#Round transparency to nearest hundreth
						transparency = round((float(holes_num)/(temp_object.n -1))*100, 2)
						print("Analyzing sept: ", sept, " Holes - ", holes_num)
						#Append to the output file each iteration
						with open(file_name, "a", newline='') as csv_file:
							writer = csv.writer(csv_file,  dialect='excel')
							csv_entry = [sept,temp_object.get_n(), temp_object.totient, e_val,holes_num, transparency]
							writer.writerow(csv_entry)
					
					except Exception as e: 
						print("Exception occured: ", str(e))
						traceback.print_exc()
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
	
	