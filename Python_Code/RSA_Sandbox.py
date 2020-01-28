#********************************************************
#*                                                  
#* File:        RSA_sandbox.py
#* Description: The RSA Sandbox allows free reign to experiment with, 
#* create, analyze, and explore RSA encryption objects and their associated
#* strength with regards to fixed point occurence.
#*
#* Author: Aron Schwartz
#* Last Edit: 1/26/2020
#*
#********************************************************

from encrypt import encryption_set
from menus_prompts import *
from encryption_test import *
from save_load import *
from configparser import ConfigParser
import time
import math
	
class RSA_sandbox():
	
	def __init__(self):
		self.plain_text = None
		self.active_encryption_object = None
		self.encryption_objects = []
		self.prime_list = []
		self.encryption_keys = {} #Dict to associate with sept
		self.public_keys = [3, 5, 17, 257, 65537]
		self.welcome_message()
		self.display_main_menu()
		
	#Menu and prompt functions
	def display_main_menu(self):
		display_main_menu()
		
	def encryption_selection_menu(self):
		encryption_selection_menu()
	
	def septuple_selection_menu(self):
		septuple_selection_menu()
	
	def primes_selection_menu(self):
		primes_selection_menu()
	
	def key_generation_menu(self):
		key_generation_menu()
	
	def welcome_message(self):
		welcome_message()
		
	def main_menu_selection_prompt(self):
		selection = main_menu_selection_prompt()
		return selection
	
	def selection_prompt(self):
		selection = selection_prompt()
		return selection
	
	def save_data(self):
		#Get folder name to save data from the user
		folder_name = input("Enter folder name (Ex: Arons_Settings): ")
		os.mkdir(folder_name)
		save_encryption_objects(folder_name, self.encryption_objects)
		save_key_data(folder_name, self.encryption_keys)
		save_primes_data(folder_name, self.prime_list)
		save_active_object_data(folder_name, self.active_encryption_object)
		
		#TODO: Implement plain text saving		
		
		print("Save Complete")
		return
		
	def load_data(self):
		folder_name = input("Enter folder name (Ex: Arons_Settings): ")
		if os.path.isdir("./" + str(folder_name)):
			print("Folder '", str(folder_name), "' found! Loading settings...")
			self.encryption_objects = load_encryption_objects(folder_name)
			self.encryption_keys = load_key_data(folder_name)
			self.prime_list = load_primes_data(folder_name)
			self.active_encryption_object = load_active_object_data(folder_name)
			print("Load Complete")
		else:
			print("Folder '", str(folder_name), "' does not exist! Data load failed")
		return
		
	def system_data_management(self):
		system_data_menu()
		choice = selection_prompt()
		while(1):
			if (choice == "1"):
				self.save_data()
				system_data_menu()
				choice = selection_prompt()
			elif(choice == "2"):
				self.load_data()
				system_data_menu()
				choice = selection_prompt()
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				system_data_menu()
				choice = selection_prompt()
		return
		
	def display_system_data(self):
		#Septuples with keys, tabbed output
		count = 1
		print("******* Septuples and keys ********")
		for key, value in self.encryption_keys.items():
			print(str(count), " - ", key.get_septuple())
			for encryption_key in value:
				print("\t", "(", str(key.get_n()), ",", str(encryption_key), ")")
		#Primes
		print("************ Primes *************")
		if len(self.prime_list) > 0:
			first_last = [self.prime_list[0], self.prime_list[-1]]
			print("All primes between: ", str(first_last))
		return
		
		
		
	
	#Borrowed from provided code from Professor Shirley (ElementalNumberTheory.py)
	def primes(self, lower_bound, upper_bound):
		if upper_bound <= 1:
			return []
		#Even lower bound, need to make it odd 
		elif (lower_bound % 2 == 0):
			lower_bound = lower_bound + 1
		X = [i for i in range(lower_bound, upper_bound + 1, 2)]                         # (1)
		P = []                                                     # (2)
		sqrt_upper_bound = math.sqrt(upper_bound)                                       # (3)
		while len(X) > 0 and X[0] <= sqrt_upper_bound:                        # (4)
			p = X[0]                                                # (5)
			P.append(p)                                             # (6)
			X = [a for a in X if a % p != 0]                        # (7)
		return P + X                                                # (8)

	def create_septuple_user_input(self):
		if len(self.prime_list) == 0:
			print("No primes list loaded")

		p_choice = int(input("Enter p: "))
		q_choice = int(input("Enter q: "))
		choice = input("Specify e? [Y/N]: ")
		if ((choice == "y") or (choice == "Y")):
			e_choice = int(input("Select e: "))
			septuple_object = encryption_set(p=p_choice, q=q_choice, custom_e = e_choice)
		else:
			septuple_object = encryption_set(p =p_choice, q=q_choice, custom_e = 65537)
		print("\nEncryption object created!")
		septuple_object.to_String()
		
		self.add_key_to_septuple(septuple_object, septuple_object.get_e())
		print()
		return septuple_object
	
	def encryption_decryption_no_padding(self):
		print("Encrypt/Decrypt without padding selected")
		#Check for an active septuple
		if self.active_encryption_object is None:
			print("No active encryption object detected, generating...")
			#Get p and q from the user, and see if they want to specify other values
			septuple = self.create_septuple_user_input()
			print("Encryption object created!")
			self.active_encryption_object = septuple
			self.encryption_objects.append(self.active_encryption_object)
		else:
			print("Active septuple: ", self.active_encryption_object.get_septuple())
		#See what the user wants to encrypt
		self.encryption_selection_menu()
		choice = self.selection_prompt()
		
		if (choice == "1"):
			print("Encrypting plain text...")
		elif (choice == "2"):
			plain_text_ascii = []
			cipher_ascii = []
			decrypted_cipher_ascii = []
			decrypted_cipher_text = ""
			plain_text_string = input("Enter string to encrypt: ")
			#Obtain a list of ascii values for the plain text
			plain_text_ascii = get_ascii_list(plain_text_string)

			#Encrypt each number in the plain-text ascii list to obtain the cipher-ascii list
			for i in plain_text_ascii:
				cipher_ascii.append(int(self.active_encryption_object.encrypt_int(i)))
				
			#Generate the cipher text from the cipher-ascii list
			cipher_text = get_string_from_ascii(cipher_ascii)
			
			
			#Decrypt the cipher-ascii.  This should result back to the original plain-ascii list
			for i in cipher_ascii:
				decrypted_cipher_ascii.append(self.active_encryption_object.decrypt_int(i))
			
			#Generate the plain-text from the plain-ascii
			for i in decrypted_cipher_ascii:
				decrypted_cipher_text += chr(int(i))
			
			#Display the original plain text, cipher text, and the decrypted_cipher_text (which should equal the plain text)
			print("\n\nPlain text: ", plain_text_string)
			print("\nCipher text: ", cipher_text)
			print("\nDecrypted cipher text: ", decrypted_cipher_text)
			print()
				
	def encrypt_padding(self):
		print("Encryption with padding selected")
	
	
	def show_keys_for_septuple(self, septuple):
		print("\n****Displaying keys for septuple ", septuple.get_septuple(), " *****")
		for encryption_key in self.encryption_keys[septuple]:
			print("(", septuple.get_n(), ",",encryption_key, ")")
		return
	
	def add_key_to_septuple(self, septuple, key):
		if septuple not in self.encryption_keys:
			self.encryption_keys[septuple] = [key]
			print("Key ", str(key), " added to septuple ", str(septuple.get_septuple()))
		elif key in self.encryption_keys[septuple]:
			print("Key ", str(key), " already exists!")
		else:
			self.encryption_keys[septuple].append(key)
			print("Key ", str(key), " appended to septuple ", str(septuple.get_septuple()))
		return
	
	
	
	def generate_keys(self):  
		print("Key generation selected")
		self.key_generation_menu()
		choice = selection_prompt()
		while(1):
			if (choice == "1"):
				if (len(self.encryption_objects) == 0):
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					self.view_septuples()
					choice = input("Select septuple to add key: ")
					e_choice = input("Enter e value: ")
					self.add_key_to_septuple(self.encryption_objects[int(choice)], int(e_choice))
					self.key_generation_menu()
					choice = selection_prompt()
					
				
				
			elif (choice == "2"):
				#Clear keys
				print("Clear keys")
				self.key_generation_menu()
				choice = selection_prompt()
			elif (choice == "3"):
				self.view_septuples()
				choice = input("Select septuple to view keys: ")
				self.show_keys_for_septuple(self.encryption_objects[int(choice)])
				self.key_generation_menu()
				choice = selection_prompt()
			elif ((choice == "q") or (choice == "Q")):
				break

	def generate_primes(self):
		print("Prime number generation selected...")
		self.primes_selection_menu()
		while(1):
			choice = self.selection_prompt()
			if (choice == "1"):		
				lower_limit = input("Enter lower limit for prime generation: ")
				upper_limit = input("Enter upper limit for prime generation: ")
				prime_list = self.primes(int(lower_limit), int(upper_limit))
				for val in prime_list:
					self.prime_list.append(val)
				print(prime_list)
			elif (choice == "2"):
				lower_limit = input("Enter lower limit for prime generation: ")
				upper_limit = input("Enter upper limit for prime generation: ")
				prime_list = self.primes(int(lower_limit), int(upper_limit))
				print(prime_list)
			elif (choice == "3"):
				print("Erasing prime list...")
				self.prime_list = []
			elif(choice == "4"):
				if len(self.prime_list) > 0:
					print(self.prime_list)
				else:
					print("List is empty!")
			elif ((choice == "Q") or (choice == "q")):
				break
			else:
				print("Invalid input!")
				self.primes_selection_menu()
				choice = self.selection_prompt()
		return

	def hole_search(self):
		holes_search_menu()
		choice = selection_prompt()
		while(1):
			if(choice == "1"):
				print("Analyze septuple")
				print("Hole search selected, analyzing the active septuple ", self.active_encryption_object.get_septuple())
				#Analyze the holes in the septuple
				holes_num = self.search_septuple(self.active_encryption_object)
				
				#Round transparency to nearest hundreth
				transparency = round((float(holes_num)/(self.active_encryption_object.n -1))*100, 2)
				print("***** Results *****: ")
				print("Septuple: ", self.active_encryption_object.get_septuple())
				print("Holes found: ", holes_num, " Transparency: ", transparency, "%")
				print()
				
				holes_search_menu()
				choice = selection_prompt()
				
			elif(choice == "2"):
				print("Compare all septuples")
				
				
				holes_search_menu()
				choice = selection_prompt()
				
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				holes_search_menu()
				choice = selection_prompt()
		
		return
		
		
		


	def output_results(self):
		print("Result output and visualization selected")
	
	
	def view_septuples(self):
		print("*** Displaying septuple list (" + str(len(self.encryption_objects)) + " loaded) ***")
		for index, object in enumerate(self.encryption_objects):
			if (self.active_encryption_object == object):
				print(index, " - ", str(object.get_septuple()) + "*** active ***")
			else:
				print(index, " - ", str(object.get_septuple()))
	
	def specify_septuples(self):
		print("Specify septuples selected")
		self.view_septuples()
		self.septuple_selection_menu()
		choice = self.selection_prompt()
		while(1):
			if (choice == "1"):
				print("Changing active septuple...")
				if (len(self.encryption_objects) == 0):
					print("No septuples loaded!")
				else:
					for index, object in enumerate(self.encryption_objects):
						print(str(index) + " - " + str(object.get_septuple()))
					choice = input("Select new active septuple: ")
					self.active_encryption_object = self.encryption_objects[int(choice)]
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif (choice == "2"):
				print("Creating septuple..")
				septuple = self.create_septuple_user_input()
				self.encryption_objects.append(septuple)
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif (choice == "3"):
				print("Clearing septuple list...")
				self.encryption_objects.clear()
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif (choice == "4"):
				self.view_septuples()
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif ((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				choice = self.selection_prompt()
		return
		
		
	def analyze_septuple(self):	
		print("Analyze septuple selected")
		
	def set_plaintext(self):
		print("Plaintext customization selected")
	
	
	
	
	def help_topics(self):
		help_menu()
		choice = selection_prompt()
		print("Help topics selected")
		
	def search_septuple(self, rsa_object):
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

	#Primary program loop
	def run(self):
		while(1):
			choice = self.main_menu_selection_prompt()
			if (choice == "1"):
				self.encryption_decryption_no_padding()
			elif(choice == "2"):
				self.encrypt_padding()
			elif(choice == "3"):
				self.generate_keys()
			elif(choice == "4"):
				self.generate_primes()
			elif(choice == "5"):
				self.hole_search()
			elif(choice == "6"):
				self.output_results()
			elif(choice == "7"):
				self.specify_septuples()
			elif(choice == "8"):
				self.analyze_septuple()			
			elif(choice == "9"):
				self.set_plaintext()
			elif(choice == "10"):
				print("Ciphertext choice selected")
			elif(choice == "11"):
				self.display_system_data()
			elif(choice == "12"):
				self.system_data_management()
			elif((choice == "M") or (choice == "m")):
				self.display_main_menu()
			elif((choice == "H") or (choice == "h")):
				self.help_topics()
			elif((choice == "q") or (choice == "Q")):
				print("Goodbye!")
				break
			else:
				print("Invalid input! Please choose from menu")


sandbox = RSA_sandbox()
sandbox.run()