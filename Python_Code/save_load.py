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
import json
import encrypt


#************************************
#									*
#            Save Functions     	*
#									*
#************************************

#Function to save all loaded septuples
def save_encryption_objects(folder_name, data):
	with open("./" + str(folder_name) + "/septuples.json", 'w')  as f:
		for object in data:
			json.dump(object.get_septuple(), f)
			f.write("\n")
	return

#Function to save the list of prime numbers
def save_primes_data(folder_name, data):
	with open("./" + str(folder_name) + "/primes_data.json", 'w')  as f:
		json.dump(data, f)
	return

#Function to save the encryption key dictionary
def save_key_data(folder_name, data):

	with open("./" + str(folder_name) + "/keys.json", 'w')  as f:
		for key, value in data.items():
			json.dump([key.get_septuple(), data[key]], f)
			f.write("\n")
	return

#Function to save the active object at time of saving
def save_active_object_data(folder_name, data):
	#Save the key data
	with open("./" + str(folder_name) + "/active_septuple.json", 'w')  as f:
		json.dump(data.get_septuple(), f)
	return

#************************************
#									*
#            Load Functions     	*
#									*
#************************************

#Function to load the septuple data
def load_encryption_objects(folder_name):
	septuple_list = []
	with open("./" + str(folder_name) + "/septuples.json")  as f:
		for line in f:
			data = json.loads(line)
			septuple = encrypt.encryption_set(p=int(data[0]),q=int(data[1]), custom_e=int(data[4]), custom_d=int(data[5]), custom_k=int(data[6]))
			septuple_list.append(septuple)
	return septuple_list

#Function to load the encryption key dictionary
def load_key_data(folder_name):
	encryption_keys = {}
	with open("./" + str(folder_name) + "/keys.json", 'r')  as f:
		for line in f:
			data = json.loads(line)
			septuple = encrypt.encryption_set(p=data[0][0],q=data[0][1], custom_e=data[0][4], custom_d=data[0][5], custom_k=data[0][6])
			encryption_keys[septuple] = data[1]
	return encryption_keys

#Function to load the primes list
def load_primes_data(folder_name):
	with open("./" + str(folder_name) + "/primes_data.json", 'r')  as f:
		prime_list=json.load(f)
	return prime_list

#Function to load the active object
def load_active_object_data(folder_name):
	with open("./" + str(folder_name) + "/active_septuple.json", 'r')  as f:
		for line in f:
			data = json.loads(line)
			active_encryption_object = encrypt.encryption_set(p=int(data[0]),q=int(data[1]), custom_e=int(data[4]), custom_d=int(data[5]), custom_k=int(data[6]))
	return active_encryption_object
