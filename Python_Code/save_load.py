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

import pickle
import os


#Save functions
def save_encryption_objects(folder_name, data):
	#Save the septuple data
	with open("./" + str(folder_name) + "/septuple_data", 'wb') as f:
		print("Saving septuple data...")
		pickle.dump(data, f)
		f.close()
	return
	
def save_primes_data(folder_name, data):
	with open("./" + str(folder_name) + "/primes_data", 'wb') as f:
		print("Saving primes data...")
		pickle.dump(data, f)
		f.close()
	return
	
def save_key_data(folder_name, data):
	#Save the key data
	with open("./" + str(folder_name) + "/key_data", 'wb') as f:
		print("Saving encryption key data...")
		pickle.dump(data, f)
		f.close()
	return
	
def save_active_object_data(folder_name, data):
	#Save the key data
	with open("./" + str(folder_name) + "/active_object", 'wb') as f:
		print("Saving encryption key data...")
		pickle.dump(data, f)
		f.close()
	return

#Load functions
def load_encryption_objects(folder_name):
	with open("./" + str(folder_name) + "/septuple_data", 'rb') as f:
		print("Loading encryption objects...")
		encryption_objects = pickle.load(f)
	return encryption_objects

def load_key_data(folder_name):
	#Load the key data
	with open("./" + str(folder_name) + "/key_data", 'rb') as f:
		print("Loading key data...")
		encryption_keys = pickle.load(f)
	return encryption_keys

def load_primes_data(folder_name):
	#Load the primes data
	with open("./" + str(folder_name) + "/primes_data", 'rb') as f:
		print("Loading primes data...")
		prime_list = pickle.load(f)
	return prime_list

def load_active_object_data(folder_name):
	#Load the active object data
	with open("./" + str(folder_name) + "/active_object", 'rb') as f:
		print("Loading active object data...")
		active_encryption_object = pickle.load(f)
	return active_encryption_object
