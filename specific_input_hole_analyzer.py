#Program: Checks for totient hot bit vs transparency
#Author: Aron Schwartz
#Last Edit: 10/25/2019

import encrypt
import time
import csv
import traceback

#Function takes a RSA object and returns a list of all holes from 0 to n-1
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

#Loads primes from input file
def load_primes(file_name):
	primes = []
	f = open(file_name, 'r')
	for line in f:
		if len(line) > 1:
			split = line.split(" ")
			for val in split:
				if val.isnumeric():
					primes.append(int(val))
	f.close()
	return primes

#Get prime input from user
def get_first_prime():
	#Loop until valid input entered
		while(1):
			choice = input("Enter 1st prime: ")
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
		
#Get prime input from user
def get_second_prime():
	#Loop until valid input entered
		while(1):
			choice = input("Enter 2nd prime: ")
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


def run():
	
	#Load first million primes
	prime_list = load_primes("primes1.txt")
	
	#Get user choice for primes to analyze
	start_choice = get_first_prime()
	end_choice = get_second_prime()
	print("Analyzing prime ", start_choice, " with prime ", end_choice)
	time.sleep(3)
	
	#Create an output file
	file_name = "./Excel_Data/prime_" + str(start_choice) + "_and_" + str(end_choice) + "_specific_analysis.csv"
	header = ["p, q, n, Phi, e, k, d", "N", "Totient", "E", "Transparency Percentage"]
	with open(file_name, "w") as csv_file:
		writer = csv.writer(csv_file,  dialect='excel')
		writer.writerow(header)
    
	#Load our chosen primes
	p_list = [start_choice]
	q_list = [end_choice]
	#Test all valid e from 0 to 65537.  
	e_list = prime_list[0:6541]

	#Loop through all p/q combinations trying each e-value for all combinations
	start_time = time.time()
	counter = 0
	for p_val in p_list:
		for q_val in q_list:
			for e_val in e_list:
				counter +=1
				if (counter % 1000 == 0):
					print("Evaluating E: ", e_val)
				
				try:
					#Make a temp object for the current septuple
					temp_object = encrypt.encryption_set(p=p_val, q=q_val, custom_e=e_val)
				
					sept = temp_object.get_septuple();
									
					#Analyze the holes in the septuple
					holes_num = search_septuple(temp_object)				
					transparency = round((float(holes_num)/(temp_object.n -1))*100, 2)
					
					#Append to the output file 
					with open(file_name, "a", newline='') as csv_file:
						writer = csv.writer(csv_file,  dialect='excel')
						csv_entry = [sept, temp_object.n, temp_object.totient, e_val, transparency]
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
	
	