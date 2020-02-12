#********************************************************
#*                                                  
#* File:        save_load.py
#* Description: Defines the save and load functions to save
#* and restore septuple, key, primes, and other program data
#*
#* Author: Aron Schwartz
#* Last Edit: 1/27/2020
#*
#********************************************************

import os
import csv
import encrypt
import ast

#************************************
#									*
#            Save Functions     	*
#									*
#************************************

#Function to save all loaded septuples
def save_encryption_objects(folder_name, data):
	try:
		with open("./" + str(folder_name) + "/septuples.csv", 'w', newline='')  as f:
			writer = csv.writer(f)
			for object in data:
				writer.writerow([object.get_septuple()])
	except Exception as e:
		print("Error saving septuple data: ", str(e))
	return

#Function to save the list of prime numbers
def save_primes_data(folder_name, data):
	try:
		with open("./" + str(folder_name) + "/primes_data.csv", 'w')  as f:
			writer = csv.writer(f)
			writer.writerow([data])
	except Exception as e:
		print("Error saving primes data: ", str(e))
	return

#Function to save the encryption key dictionary
def save_key_data(folder_name, data):
	try:
		with open("./" + str(folder_name) + "/keys.csv", 'w', newline='')  as f:
			writer = csv.writer(f)
			for key, value in data.items():
				writer.writerow([key.get_septuple(), value])
	except Exception as e:
		print("Error saving key data: ", str(e))
	return

#Function to save the active object at time of saving
def save_active_object_data(folder_name, data):
	#Save the key data
	try:
		with open("./" + str(folder_name) + "/active_septuple.csv", 'w')  as f:
			writer = csv.writer(f)
			writer.writerow([data.get_septuple()])
	except Exception as e:
		print("Error saving active object: ", str(e))
	return

#************************************
#									*
#            Load Functions     	*
#									*
#************************************

#Function to load the septuple data
def load_encryption_objects(folder_name):
	septuple_list = []
	try:
		with open("./" + str(folder_name) + "/septuples.csv")  as f:
			reader = csv.reader(f)
			for line in reader:
				data = ast.literal_eval(line[0])
				septuple = encrypt.encryption_set(p=int(data[0]),q=int(data[1]), custom_e=int(data[4]), custom_k=int(data[5]), custom_d=int(data[6]))
				septuple_list.append(septuple)
	except Exception as e:
		print("Error loading septuple data: ", str(e))
	return septuple_list

#Function to load the encryption key dictionary
def load_key_data(folder_name):
	encryption_keys = {}
	try:
		with open("./" + str(folder_name) + "/keys.csv", 'r')  as f:
			reader = csv.reader(f)
			for line in reader:
				sept_list = ast.literal_eval(line[0])
				keys = ast.literal_eval(line[1])
				septuple = encrypt.encryption_set(p=sept_list[0],q=sept_list[1], custom_e=sept_list[4], custom_k=sept_list[5], custom_d=sept_list[6])
				encryption_keys[septuple] = keys
	except Exception as e:
		print("Error loading key data: ", str(e))
	return encryption_keys

#Function to load the primes list
def load_primes_data(folder_name):
	prime_list = []
	try:
		with open("./" + str(folder_name) + "/primes_data.csv", 'r')  as f:
			reader = csv.reader(f)
			for line in reader:
				if len(line) > 0:
					prime_list = ast.literal_eval(line[0])
	except Exception as e:
		print("Error loading primes data: ", str(e))
	return prime_list

#Function to load the active object
def load_active_object_data(folder_name):
	active_encryption_object = None
	try:
		with open("./" + str(folder_name) + "/active_septuple.csv", 'r')  as f:
			reader = csv.reader(f)
			for line in reader:
				if len(line) > 0:
					data = ast.literal_eval(line[0])
					active_encryption_object = encrypt.encryption_set(p=int(data[0]),q=int(data[1]), custom_e=int(data[4]), custom_k=int(data[5]), custom_d=int(data[6]))
	except Exception as e:
		print("Error loading active object: ", str(e))
	return active_encryption_object
