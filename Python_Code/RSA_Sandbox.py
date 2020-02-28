#********************************************************
#*                                                  
#* File:        RSA_sandbox.py
#* Description: The RSA Sandbox allows free reign to experiment with, 
#* create, analyze, and explore RSA encryption objects and their associated
#* strength with regards to fixed point occurence.
#*
#* Author: Aron Schwartz
#* Last Edit: 2/2/2020
#*
#********************************************************

#Import all required libraries
from encrypt import encryption_set
from encrypt import check_coprimality
from menus_prompts import *
from encryption_test import *
from save_load import *
from help import *
from datetime import datetime
from sandbox_options import *
import time
import math
import shutil
import random
import collections

class RSA_sandbox():
	
	#************************************
	#									*
	#            Init function     		*
	#									*
	#************************************

	def __init__(self):
		#Internal data variables
		
		#Internal variables to store plain/cipher text and files
		self.plain_text = None
		self.plain_text_file = None
		self.cipher_text = None
		self.cipher_text_file = None
		self.active_encryption_object = None
		
		#Instantiate the system options
		self.options = sandbox_options()
		
		#Store the encryption objects and primes inside internal lists
		self.encryption_objects = []
		self.prime_list = []
		
		#The encryption keys exist in a dictionary 
		self.encryption_keys = {} 
		self.public_keys = [3, 5, 17, 257, 65537]
		try:
			#Make the profiles folder if it doesn't exist
			if not os.path.exists("./Profiles/"):
				os.mkdir("./Profiles/")
		except Exception as e:
			print("Error creating folder 'Profiles': ", str(e))
		
		try:
			#Make the plaintext folder if it doesn't exist
			if not os.path.exists("./Plaintext/"):
				os.mkdir("./Plaintext/")
		except Exception as e:
			print("Error creating folder 'Profiles': ", str(e))
			
		#Set the plaintext folder variable
		self.plaintext_folder = "./Plaintext/"
		
		#Make the ciphertext folder if it doesn't exist
		if not os.path.exists("./Ciphertext/"):
			os.mkdir("./Ciphertext/")
		
		#Set the ciphertext folder variable
		self.ciphertext_folder = "./Ciphertext/"
		#Make the results folder if it doesn't exist
		if not os.path.exists("./Results/Septuple_Comparisons"):
			os.mkdir("./Results/Septuple_Comparisons")
		if not os.path.exists("./Results/Transparency_Profiles"):
			os.mkdir("./Results/Transparency_Profiles")
			
	
		#Finish the initialization with the welcome message and display the main menu 
		self.welcome_message()
		self.display_main_menu()
		
	#************************************************************************************
	#																					*
	#        Menu calling functions: Calls relevant function from menus_prompts.py   	*
	#																					*
	#************************************************************************************
	
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
	
	#****************************************************************************************
	#																						*
	#      Prompt calling functions. Calls the relevant function from menu_prompts.py    	*
	#																						*
	#****************************************************************************************
	
	def main_menu_selection_prompt(self):
		selection = main_menu_selection_prompt()
		return selection
	
	def selection_prompt(self):
		selection = selection_prompt()
		return selection
	
	
	#************************************************************************************
	#																					*
	#  save_data(): Obtains a folder name from user and saves all system data to 		*
	#               directory with provided the input name								*
	#																					*
	#************************************************************************************
	
	def save_data_profile(self):
		#Get folder name to save data from the user
		folder_name = input("Enter profile folder name (Ex: Arons_Settings): ")
		
		#If folder already exists, remove it so we can overwrite
		if os.path.exists("./Profiles/" + str(folder_name)):
			for root, dirs, files in os.walk("./" + str(folder_name)):
				for file in files:
					os.remove(os.path.join(root, file))
		else:
			os.makedirs("./Profiles/" + folder_name)
		#Call the functions to save all system data: objects, keys, primes, plaintext, etc
		save_encryption_objects(folder_name, self.encryption_objects)
		save_key_data(folder_name, self.encryption_keys)
		save_primes_data(folder_name, self.prime_list)
		save_active_object_data(folder_name, self.active_encryption_object)
		
		#TODO: Implement plain text saving		
		
		print("**** Save Successful! ****")
		return
	
	#************************************************************************************
	#																					*
	#  load_data(): Loads system data from a folder name provided from user input		*
	#																					*
	#************************************************************************************
	
	def load_data_profile(self):
		#Get the folder name from the user
		folder_name = input("Enter profile folder name (Ex: Arons_Settings): ")
		#See if it exists
		if os.path.isdir("./Profiles/" + str(folder_name)):
			#Indicate if the folder was found
			print("Folder '", str(folder_name), "' found! Loading settings...")
			#Call the load functions to reload system data
			self.encryption_objects = load_encryption_objects(folder_name)
			self.encryption_keys = load_key_data(folder_name)
			self.prime_list = load_primes_data(folder_name)
			self.active_encryption_object = load_active_object_data(folder_name)
			
			#Load up keys for the loaded septuples, in case some were added manually.  This ensures each septuple has its key entered in the system dictionary
			for septuple in self.encryption_objects:
				self.add_key_to_septuple(septuple, septuple.get_e())
			print("******** Load Successful! **********")
		#Error message if folder not found
		else:
			print("Folder '", str(folder_name), "' does not exist! Data load failed")
		return
	
	
	def create_ciphertext_file(self, file_name, ciphertext):
		with open(self.ciphertext_folder + str(file_name) + ".txt", 'w')  as f:
			f.write(str(ciphertext))
			f.close()
		return
	
	def display_plaintext_folder_contents(self):
		for index, file in enumerate(os.listdir(self.plaintext_folder)):
			print(str(index), " - ", str(file))
		return
		
	def load_plaintext_select_file(self):
		#Display message and return None if nothing exists in the plaintext folder
		if len(os.listdir(self.plaintext_folder)) == 0:
			return None
		#Otherwise, display the contents of the folder
		else:
			valid = False
			#Show all the files contained in the plaintext folder
			self.display_plaintext_folder_contents()
			choice = selection_prompt()
			#Loop until they select a valid file
			while(1):
				for index, file in enumerate(os.listdir(self.plaintext_folder)):
					try:
						if int(choice) == index:
							file_to_open = file
							valid = True
							break
					except ValueError:
						print("Invalid entry!")
						return "INVALID"
				if (valid == True):
					break
				else:
					print("Invalid choice!")
					self.display_plaintext_folder_contents()
					choice = selection_prompt()
		return file_to_open
	#*************************************************************************************************
	#																								 *
	#  system_data_management(): Handles various options related to saving and loading system data   *
	#																								 *
	#*************************************************************************************************
	
	def system_data_management(self):
		#Call the system data management menu
		system_data_menu()
		choice = selection_prompt()
		while(1):
			#Save data to profile
			if (choice == "1"):
				self.save_data_profile()
				system_data_menu()
				choice = selection_prompt()
			#Load data from profile
			elif(choice == "2"):
				self.load_data_profile()
				system_data_menu()
				choice = selection_prompt()
			#Quit to main menu
			elif((choice == "q") or (choice == "Q")):
				break
			#Invalid otherwise, reprompt for valid choice
			else:
				print("Invalid choice!")
				system_data_menu()
				choice = selection_prompt()
		return
	
	#************************************************************************************
	#																					*
	#  display_system_data(): Displays all septuples, encryption keys, and prime number *
	#						  data currently loaded in the program     					*
	#																					*
	#************************************************************************************
	
	def display_system_data(self):
		#Septuples with keys, tabbed output
		choice = input("View keys verbosely? [Y/N]:")
		if ((choice == "y") or (choice == "Y")):
			print("******* DISPLAYING SYSTEM DATA ********")
			self.view_septuples_with_keys()

		else:
			self.view_septuples()
		#Primes
		print("************ Primes *************")
		if len(self.prime_list) > 0:
				first_last = [self.prime_list[0], self.prime_list[-1]]
				print("All primes between: ", str(first_last))
				print()
		print("Plaintext loaded from file: ", str(self.plain_text_file))
		print()
		return
		
	#************************************************************************************
	#																					*
	#  view_septuples(): Displays all septuples loaded innto system data, as well as    *
	#					 information regarding the active septuple						*
	#															    					*
	#************************************************************************************
	
	def view_septuples(self):
		#Loop through the septuple list and print, catch the active septuple and indicate with extra characters
		print("\n*** Displaying septuple list (" + str(len(self.encryption_objects)) + " loaded) ***")
		for index, object in enumerate(self.encryption_objects):
			if self.active_encryption_object is not None:
				if self.active_encryption_object.get_septuple() == object.get_septuple():
					print(index, " - ", str(object.get_septuple()) + " *** active ***")
				else:
					print(index, " - ", str(object.get_septuple()))
			else:
				print(index, " - ", str(object.get_septuple()))
		print()
		
	#***********************************************************************************************
	#																							   *
	#  view_septuples_with_keys(): Displays all septuples loaded innto system data, as well as     *
	#					 information regarding the active septuple and all keys for each septuple  *
	#															    					           *
	#***********************************************************************************************
	
	def view_septuples_with_keys(self):
		print("\n*** Displaying septuple list (" + str(len(self.encryption_objects)) + " loaded) ***")
		for index, object in enumerate(self.encryption_objects):
			if self.active_encryption_object is not None:
				if (self.active_encryption_object.get_septuple() == object.get_septuple()):
					print(index, " - ", str(object.get_septuple()) + " *** active ***")
					self.show_keys_for_septuple(object)
				else:
					print(index, " - ", str(object.get_septuple()))
					self.show_keys_for_septuple(object)
			else:
				print(index, " - ", str(object.get_septuple()))
				self.show_keys_for_septuple(object)
		print()
	
	
	#***************************************************************************************************
	#																								   *
	#  primes(): Generates a list of primes in a given range utilizing the sieve of erasthones method  *
	#  Original Author: Professor Glenn Shirley, PSU												   *
	#																								   *
	#***************************************************************************************************
	
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
	
	#From stack overflow
	def is_prime(self, n):
		if n == 2:
			return True
		if n % 2 == 0 or n <=1:
			return False
		sqr = int(math.sqrt(n)) + 1
		for divisor in range(3, sqr, 2):
			if n % divisor == 0:
				return False
		return True
	
	
	
	#************************************************************************************
	#																					*
	#  create_septuple_user_input(): Creates a septuple from user input.  Allows for    *
	#                                selection of primes and e value					*
	#																					*
	#************************************************************************************
	
	def create_septuple_user_input(self):
		if len(self.prime_list) == 0:
			print("No primes list loaded")
		p_choice = input("Enter p: ")
		try:
			p_choice = int(p_choice)
			
		except ValueError:
			print("'", str(p_choice), "' is not a valid integer!")
			return None
			
		if not self.is_prime(p_choice):
			print(str(p_choice), " is not a prime number!")
			return None
			
			
		q_choice = input("Enter q: ")
		try:
			q_choice = int(q_choice)
			
		except ValueError:
			print("'", str(q_choice), "' is not a valid integer!")
			return None
			
		if not self.is_prime(q_choice):
			print(str(q_choice), " is not a prime number!")
			return None
		
		choice = input("Specify e? Press enter to use default (65537) [Y/N]: ")
		if ((choice == "y") or (choice == "Y")):
			e_choice = input("Select e: ")
			print("The choice is: ", str(e_choice))
			try:
				val = int(e_choice)
			except ValueError:
				print("Integer input required!")
				return None
			if not check_coprimality((int(p_choice) - 1)*(int(q_choice) - 1), int(e_choice)):
				print("Co primality conditions not met!")
				return None
			else:
				septuple_object = encryption_set(p=p_choice, q=q_choice, custom_e = int(e_choice))
		else:
			septuple_object = encryption_set(p =p_choice, q=q_choice, custom_e = 65537)
		print("\nEncryption object created!")
		septuple_object.to_String()
		
		self.add_key_to_septuple(septuple_object, septuple_object.get_e())
		
		
		if self.active_encryption_object is None:
			self.active_encryption_object = septuple_object
		print()
		return septuple_object
	
	
	
	#****************************************************************************************
	#																						*
	#  encryption_decryption_no_padding(): Allows for encyryption of strings or plaintext   *
	#									   using system data without using padding 			*
	#																						*
	#****************************************************************************************
	
	def encryption_decryption_no_padding(self):
		print("Encrypt/Decrypt without padding selected")
		#Check for an active septuple
		if self.active_encryption_object is None:
			print("No active encryption object detected, generating...")
			#Get p and q from the user, and see if they want to specify other values
			septuple = self.create_septuple_user_input()
			if septuple is None:
				print("*** Object creation failed! ***")
				return 
			print("Encryption object created!")
			self.active_encryption_object = septuple
			self.encryption_objects.append(self.active_encryption_object)
		else:
			print("Active septuple: ", self.active_encryption_object.get_septuple())
			
		#See what the user wants to encrypt
		self.encryption_selection_menu()
		choice = self.selection_prompt()
		while(1):
			#Encrypt the plaintext, if it exists
			if (choice == "1"):
				if self.plain_text is None:
					print("No plain text selected!")
					check_contents = self.manage_plaintext()
					if check_contents is None:
						return
				else:
					self.manage_plaintext()
				choice = input("Use active object? " + str(self.active_encryption_object.get_septuple()) + "? [Y/N]: ")
				if((choice == "Y") or (choice == "y")):
					self.cipher_text = self.active_encryption_object.encrypt_int_list(get_ascii_list(self.plain_text))
					decrypted = self.active_encryption_object.decrypt_int_list(self.cipher_text)
					self.create_ciphertext_file("cipher_" + str(self.plain_text_file) + "_(" + str(self.active_encryption_object.get_n()) + "," + str(self.active_encryption_object.get_e()) + ")", get_string_from_ascii(self.cipher_text).encode('utf-8'))
					
					print("\n\nThe plain text is: ", self.plain_text)
					print("\nThe ciphertext is: ", get_string_from_ascii(self.cipher_text))
					print("\nDecrypted: ", get_string_from_ascii(decrypted))
					print()
					break
				else:
					self.view_septuples()
					choice = input("Select septuple encrypt plaintext: ")
					try:
						septuple = self.encryption_objects[int(choice)]
					except Exception:
						print("Invalid selection")
						break
					self.cipher_text = septuple.encrypt_int_list(get_ascii_list(self.plain_text))
					decrypted = septuple.decrypt_int_list(self.cipher_text)
					self.create_ciphertext_file("cipher_" + str(self.plain_text_file) + "_(" + str(septuple.get_n()) + "," + str(septuple.get_e()) + ")", get_string_from_ascii(self.cipher_text).encode('utf-8'))
					
					print("\n\nThe plain text is: ", self.plain_text)
					print("\nThe ciphertext is: ", get_string_from_ascii(self.cipher_text))
					print("\nDecrypted: ", get_string_from_ascii(decrypted))
					print()
					break
					
				self.encryption_selection_menu()
				choice = self.selection_prompt()
			#Encrypt an input string from the user
			elif (choice == "2"):
				print("The active: ", self.active_encryption_object.get_septuple())
				#Lists to hold values
				plain_text_ascii = []
				cipher_text_ascii = []
				decrypted_cipher_ascii = []
				
				#Prompt the user to input a string to be encrypted
				plain_text_string = input("Enter string to encrypt: ")
				#Converte the string to a list of equivalent ascii integers
				plain_text_ascii = get_ascii_list(plain_text_string)
				#Encrypt each number in the plain-text ascii list to obtain the cipher-ascii list
				cipher_text_ascii = self.active_encryption_object.encrypt_int_list(plain_text_ascii)
				#Generate the cipher text string from the cipher-ascii list
				cipher_text_string = get_string_from_ascii(cipher_text_ascii)
				decrypted_cipher_ascii= self.active_encryption_object.decrypt_int_list(cipher_text_ascii)
				#Generate the resulting string after decrypting the cipher text list 
				decrypted_ciphertext_string = get_string_from_ascii(decrypted_cipher_ascii)
				#Display the original plain text, cipher text, and the decrypted_cipher_text (which should equal the plain text)
				print("\n\nPlain text: ", plain_text_string)
				print("\nCipher text: ", cipher_text_string)
				print("\nDecrypted cipher text: ", decrypted_ciphertext_string)
				print()
		
				self.encryption_selection_menu()
				choice = self.selection_prompt()
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				self.encryption_selection_menu()
				choice = self.selection_prompt()
		return
		
			
			
			
	#****************************************************************************************
	#																						*
	#  encryp_padding(): Allows for encyryption of strings or plaintext   *
	#									   using system data with padding enabled 			*
	#																						*
	#****************************************************************************************
	
	def encrypt_padding(self):
		print("Encryption with padding selected")
	
	#*********************************************************************************************
	#																							 *
	#  show_keys_for_septuple(): Displays all keys loaded in system data for a given septuple    *
	#																							 *
	#*********************************************************************************************
	
	def show_keys_for_septuple(self, septuple):
		for key, value in self.encryption_keys.items():
			if key.get_septuple() == septuple.get_septuple():
				for encryption_key in value:
					print("(", key.get_n(), ",",encryption_key, ")")
		return
	
	
	
	#*********************************************************************************************
	#																							 *
	#  add_key_to_septuple(): Appends a key to a given septuple in the system data dictionary    *
	#																							 *
	#*********************************************************************************************
	
	def add_key_to_septuple(self, septuple, key):
		need_to_add = True
		for dict_key, value in self.encryption_keys.items():
			#Septuple exists already
			if septuple.get_septuple() == dict_key.get_septuple():
				if key in value:
					need_to_add = False
					break
				else:
					self.encryption_keys[dict_key].append(key)
					need_to_add = False
					break		
		if (need_to_add == True):	
			self.encryption_keys[septuple] = [key]
		return
	
	#****************************************************************
	#																*
	#  manage_keys(): Handles the key management functionality	    *
	#																*
	#****************************************************************
	
	def manage_keys(self):  
		self.key_generation_menu()
		choice = selection_prompt()
		while(1):
			#Add key to a loaded septuple
			if (choice == "1"):
				#Ensure atleast one septuple is loaded
				if (len(self.encryption_objects) == 0):
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					self.view_septuples()
					choice = input("Select septuple to add key: ")
					try:
						septuple = self.encryption_objects[int(choice)]
					except Exception:
						print("Invalid selection")
						break
					
					
					
					e_choice = input("Enter e value: ")
					try:
						val = int(e_choice)
					except ValueError:
						print("Integer input required!")
						break
					if not check_coprimality(((int(septuple.get_p()) -1)*(int(septuple.get_q()) - 1)), int(e_choice)):
						print("Co primality conditions not met!")
						break
					self.add_key_to_septuple(self.encryption_objects[int(choice)], int(e_choice))
					self.key_generation_menu()
					choice = selection_prompt()
			#Swap keys
			elif (choice == "2"):
				if (len(self.encryption_objects) == 0):
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					self.view_septuples()
					sept_choice = input("Select septuple to swap key: ")
					try:
						self.show_keys_for_septuple(self.encryption_objects[int(sept_choice)])
					except IndexError:
						print("Invalid choice!")
						break
					key_choice = selection_prompt()
					old_septuple = self.encryption_objects[int(sept_choice)]
					found = False
					for key, value in self.encryption_keys.items():
						for encryption_key in value:
							#Key exists, dont need to add to the dictionary.  Just swap out in septuple list, and replace in the key dictionary
							if int(key_choice) == encryption_key:
								print("Key already exists, swapping...")
								#Check that the e value meets coprimality
								if(self.encryption_objects[int(sept_choice)].verify_e_swap(int(key_choice)) == True):
									new_sept = encrypt.encryption_set(old_septuple.get_p(), old_septuple.get_q(), int(key_choice))
									#Replace the old septuple with the new one in the encryption object list
									
									for index, septuple in enumerate(self.encryption_objects):
										if septuple.get_septuple() == old_septuple.get_septuple():
											self.encryption_objects[index] = new_sept
									
								
									for key, value in self.encryption_keys.items():
										if key.get_septuple() == old_septuple.get_septuple():
											self.encryption_keys[new_sept] = self.encryption_keys[key]
											del self.encryption_keys[key]
											break
									self.encryption_objects[int(sept_choice)].swap_out_e_value(int(key_choice))
									print("Success!")
									
									#If the old sept was the active, make the new one the active
									if self.active_encryption_object is None:
										self.active_encryption_object = new_sept
									elif (self.active_encryption_object.get_septuple() == old_septuple.get_septuple()):
										self.active_encryption_object = new_sept
								found = True
								break
						if found == True:
							break
					if(found == False):
						print("Key doesnt exist, adding to data and swapping...")
						if check_coprimality(int(key_choice), ((old_septuple.get_p()-1)*(old_septuple.get_q()-1))):
							new_sept = encrypt.encryption_set(old_septuple.get_p(), old_septuple.get_q(), int(key_choice))
							#Replace the old septuple with the new one in the encryption object list
							
							for index, septuple in enumerate(self.encryption_objects):
								if septuple.get_septuple() == old_septuple.get_septuple():
									self.encryption_objects[index] = new_sept
							
						
							for key, value in self.encryption_keys.items():
								if key.get_septuple() == old_septuple.get_septuple():
									self.encryption_keys[new_sept] = self.encryption_keys[key]
									self.encryption_keys[new_sept].append(int(key_choice))
									del self.encryption_keys[key]
									break
							self.encryption_objects[int(sept_choice)].swap_out_e_value(int(key_choice))
							print("Success!")
							
							#If the old sept was the active, make the new one the active
							if self.active_encryption_object is None:
								self.active_encryption_object = new_sept
							elif (self.active_encryption_object.get_septuple() == old_septuple.get_septuple()):
								self.active_encryption_object = new_sept
							print("Success!")
						else:
							print("Value ", str(key_choice), " does not satisify coprimality!")
				self.show_key_list()	
				self.key_generation_menu()
				choice = selection_prompt()
						
			elif (choice == "3"):
				#Clear keys
				print("Clear keys")
				self.key_generation_menu()
				choice = selection_prompt()
			elif (choice == "4"):
				self.view_septuples()
				choice = input("Select septuple to view keys: ")
				try:
					self.show_keys_for_septuple(self.encryption_objects[int(choice)])
				except IndexError:
					print("Invalid choice!")
					break
				self.key_generation_menu()
				choice = selection_prompt()
			#Add primes to specific septuple
			elif (choice == "5"):
				if len(self.prime_list) == 0:
					print("No primes generated!")
					self.key_generation_menu()
					choice = selection_prompt()
				elif len(self.encryption_objects) == 0:
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					self.view_septuples()
					choice = input("Select septuple to add keys: ")
					try:
						val = self.encryption_objects[int(choice)]
					except ValueError:
						print("Invalid selection!")
						break
					for prime in self.prime_list:					
						self.add_key_to_septuple(self.encryption_objects[int(choice)], prime)
					self.key_generation_menu()
					choice = selection_prompt()
			#Add primes to keys of all septuples
			elif (choice == "6"):
				if len(self.prime_list) == 0:
					print("No primes generated!")
					self.key_generation_menu()
					choice = selection_prompt()
				elif len(self.encryption_objects) == 0:
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					for septuple in self.encryption_objects:
						for prime in self.prime_list:
							self.add_key_to_septuple(septuple, prime)
					self.key_generation_menu()
					choice = selection_prompt()
			elif ((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				self.key_generation_menu()
				choice = selection_prompt()
	
	
	def show_key_list(self):
		for key, value in self.encryption_keys.items():
			print("Key: ", key.get_septuple(), " Value: ", value)
	
	#*************************************************************************
	#																		 *
	#  manage_primes(): Handles the prime number management functionality	 *
	#																		 *
	#*************************************************************************
	
	def manage_primes(self):
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
				print("\nGenerated ", str(len(prime_list)), " primes")
				print()
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
	
	def format_results_with_keys(self, septuple, holes_num, transparency, holes_list):
		if self.options.check_verbose():
			result_string = "Septuple: " + str(septuple) + ", Key: " + str(septuple[4]) + ", Holes found: " + str(holes_num) + ", Transparency: " + str(transparency) + "%\n" + str(holes_list)
		else:
			result_string = "Septuple: " + str(septuple) + ", Key: " + str(septuple[4]) + ", Holes found: " + str(holes_num) + ", Transparency: " + str(transparency)
		return result_string
		
	def format_results(self, septuple, holes_num, transparency, holes_list):
		if self.options.check_verbose():
			result_string = "Septuple: " + str(septuple) + ", Holes found: " + str(holes_num) + ", Transparency: " + str(transparency) + "%\n" + str(holes_list)
		else:
			result_string = "Septuple: " + str(septuple) + ", Holes found: " + str(holes_num) + ", Transparency: " + str(transparency)
		return result_string
	
	#****************************************************************
	#																*
	#  analyze_holes(): Handles the hole analysis functionality	 	*
	#															    *
	#****************************************************************
	
	def analyze_holes(self):
		holes_search_menu()
		choice = selection_prompt()
		while(1):
			#Analyze the active septuple
			if(choice == "1"):
				if self.active_encryption_object is None:
					if len(self.encryption_objects) == 0:
						choice = input("No objects loaded! Create one? [Y/N]: ")
						if ((choice == "y") or (choice == "Y")):
							septuple = self.create_septuple_user_input()
							if septuple is None:
								print("Object creation failed!")
								break
							else:
								self.encryption_objects.append(septuple)

					elif len(self.encryption_objects) >= 1:
						self.active_encryption_object = self.encryption_objects[0]
					else:
						print("Returning to main menu")
						break
				print("Analyzing active septuple: ", self.active_encryption_object.get_septuple())
				#Analyze the holes in the septuple
				holes_num, holes_list = self.active_encryption_object.search_holes()
				#Round transparency to nearest hundreth
				transparency = round((float(holes_num)/(self.active_encryption_object.n -1))*100, 2)
				print("***** Results *****: ")
				print(self.format_results(self.active_encryption_object.get_septuple(), holes_num, transparency, holes_list))
				
				holes_search_menu()
				choice = selection_prompt()
			#Compare all septuples, display results sorted by transparency
			elif(choice == "2"):
				result_transparency_dict = {}
				
				now = datetime.now()
				current_time = now. strftime("%H_%M_%S")
				#Gather results for all the septuples
				with open("./Results/Septuple_Comparisons/Sept_Compare_" + str(current_time) + ".csv", 'w', newline='')  as f:
					writer = csv.writer(f)
					writer.writerow(["Septuple", "E Value", "Holes Found", "Transparency", "Holes List"])
					for index, septuple in enumerate(self.encryption_objects):
						print(str(round((index/len(self.encryption_objects)*100), 2)), "% complete")
						#Analyze the holes in the septuple
						holes_num, holes_list = septuple.search_holes()
						#Round transparency to nearest hundreth
						transparency = round((float(holes_num)/(septuple.n -1))*100, 2)
						result_string = self.format_results(septuple.get_septuple(), holes_num, transparency, holes_list)
		
						if transparency not in result_transparency_dict:
							result_transparency_dict[transparency] = [result_string]
						else:
							result_transparency_dict[transparency].append(result_string)
							
							
							
						writer.writerow([septuple.get_septuple(), septuple.get_e(), holes_num, transparency, holes_list])
				#Display the results sorted by transparency and write to output folder
				print("\n\n*********** RANKED RESULTS **************")
				for key in reversed(sorted(result_transparency_dict)):
					for entry in result_transparency_dict[key]:
						print(entry) 
				holes_search_menu()
				choice = selection_prompt()
			#Generate transparency profile
			elif(choice == "3"):
			
				result_transparency_dict = {}
			
				for index, object in enumerate(self.encryption_objects):
					print(str(index) + " - " + str(object.get_septuple()))
				choice = input("Select septuple: ")
				try:
					sept = self.encryption_objects[int(choice)]
				except IndexError:
					print("Invalid choice!")
					break
				now = datetime.now()
				current_time = now. strftime("%H_%M_%S")
				with open("./Results/Transparency_Profiles/Trans_Profile_" + str(current_time) + ".csv", 'w', newline='')  as f:
					writer = csv.writer(f)
					writer.writerow(["Septuple", "Holes_Found", "E Value", "Transparency", "Holes List"])
					for key, value in self.encryption_keys.items():
						if key.get_septuple() == sept.get_septuple():
							for index, encryption_key in enumerate(value):
								print("Checking key: ", str(encryption_key), "(", str(round((index/len(value)*100), 2)), "% complete)")
								temp_sept = encrypt.encryption_set(p=sept.get_p(), q=sept.get_q(), custom_e=int(encryption_key))
								holes_num, holes_list = temp_sept.search_holes()
		
								#Round transparency to nearest hundreth
								transparency = round((float(holes_num)/(sept.n -1))*100, 2)
								result_string = self.format_results_with_keys(temp_sept.get_septuple(), holes_num, transparency, holes_list)
								if transparency in result_transparency_dict:
									result_transparency_dict[transparency].append(result_string)
								else:
									result_transparency_dict[transparency] = [result_string]
								writer.writerow([temp_sept.get_septuple(),  holes_num, temp_sept.get_e(), transparency, holes_list])
				#Display the results sorted by transparency
				print("\n\n*********** RANKED RESULTS **************")
				for key, value in reversed(sorted(result_transparency_dict.items())):
					for entry in value:
						print(entry)
		
							
				
				holes_search_menu()
				choice = selection_prompt()
				
			
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				holes_search_menu()
				choice = selection_prompt()
		
		return	

	#*************************************************************************
	#																		 *
	#  manage_septuples():  Handles the septuple management functionality 	 *
	#															    	     *
	#*************************************************************************
	
	def manage_septuples(self):
		if len(self.encryption_objects) < 20:
			self.view_septuples()
		else:
			print("\n**** ", str(len(self.encryption_objects)), " septuples loaded ****")
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
				if septuple is None:
					print("Object creation failed!")
				else:
					self.encryption_objects.append(septuple)
					if len(self.encryption_objects) == 1:
						self.active_encryption_object = septuple
				
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			#Create septs from primes
			elif (choice == "3"):
				print("\nGenerating septuples....")
				created = 0
				for index, i in enumerate(self.prime_list):
					print(str(round((index/len(self.prime_list)*100), 2)), "% complete")
					for j in self.prime_list:
						if j > i:
							e_val = int(random.choice(self.public_keys))
							temp_object = encrypt.encryption_set(p=i, q=j, custom_e=e_val)	
														
							found = False
							for sept in self.encryption_objects:
								if temp_object.get_septuple() == sept.get_septuple():
									found = True
									break
							if not found:
								self.encryption_objects.append(temp_object)
							self.add_key_to_septuple(temp_object, e_val)
							created +=1
							#print("Created septuple: ", temp_object.get_septuple())
				print("\nGenerated ", str(created), " septuples")
				print()
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif (choice == "4"):
				confirm = input("Erase all seputples? [Y/N]: ")
				if ((confirm == "y") or (confirm == "Y")):
					self.encryption_objects = []
					self.active_encryption_object = None
					self.encryption_keys = {}
					print("**** Septuple and Key data erased *****")
				self.encryption_objects.clear()
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif (choice == "5"):
				self.view_septuples()
				self.septuple_selection_menu()
				choice = self.selection_prompt()
			elif ((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				choice = self.selection_prompt()
		return
	
	def system_options(self):
		system_options_menu()
		self.options.display_options_status()
		choice = self.selection_prompt()
		while(1):
			if (choice == "1"):
				self.options.toggle_verbose()
				system_options_menu()
				self.options.display_options_status()
				choice = self.selection_prompt()
			elif (choice == "2"):
				self.options.toggle_hex()
				system_options_menu()
				self.options.display_options_status()
				choice = self.selection_prompt()
			elif ((choice == "Q") or (choice == "q")):
				break
			else:
				print("Invalid choice!")
				system_options_menu()
				self.options.display_options_status()
				choice = self.selection_prompt()
	def analyze_septuples(self):	
		print("Analyze septuple selected")
		
	def manage_plaintext(self):
		plaintext_file = self.load_plaintext_select_file()
		if plaintext_file == None:
			print("Plaintext folder is empty!")
			return None
		elif plaintext_file == "INVALID":
			return None
		else:
			with open(self.plaintext_folder + "/" + plaintext_file) as f:
				self.plain_text = f.read()
				self.plain_text_file = plaintext_file
				self.plain_text_file = self.plain_text_file.replace(".txt", "")
			print("\nPlaintext set to file: ", str(plaintext_file))
		return ""
	
	
	#******************************************************************************************
	#																		 				  *
	#  help_topics():  Allows user to obtain information regarding all program capabilities   *
	#															    	     				  *
	#******************************************************************************************
	
	def help_topics(self):
		print("Help topics selected")
		while(1):
			help_menu()
			choice = selection_prompt()
			if (choice == "1"):
				encryption_decryption_no_padding_help()
			elif(choice == "2"):
				encryption_padding_help()
			elif(choice == "3"):
				manage_septuples_help()
			elif(choice == "4"):
				manage_keys_help()
			elif(choice == "5"):
				manage_primes_help()
			elif(choice == "6"):
				plaintext_selection_help()
			elif(choice == "7"):
				analyze_holes_help()
			elif(choice == "8"):
				display_system_data_help()
			elif(choice == "9"):
				save_load_data_help()
			elif(choice == "10"):
				RSA_Sandbox_overview()
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
		return
		
	
	#*************************************************************************************************
	#																		 				  		 *
	#  run():  Top level function that runs the RSA sandbox program.  Displays all program options	 *
	#  		   and dictates program flow															 *
	#															    	     				  		 *
	#*************************************************************************************************
	
	def run(self):
		while(1):
			choice = self.main_menu_selection_prompt()
			if (choice == "1"):
				self.encryption_decryption_no_padding()
			elif(choice == "2"):
				self.encrypt_padding()
			elif(choice == "3"):
				self.manage_septuples()			
			elif(choice == "4"):
				self.manage_keys()
			elif(choice == "5"):
				self.manage_primes()
			elif(choice == "6"):
				self.manage_plaintext()
			elif(choice == "7"):
				self.analyze_holes()
			elif(choice == "8"):
				self.display_system_data()
			elif(choice == "9"):
				self.system_data_management()
			elif(choice == "10"):
				self.system_options()
			elif((choice == "M") or (choice == "m")):
				self.display_main_menu()
			elif((choice == "H") or (choice == "h") or (choice == "help")):
				self.help_topics()
			elif((choice == "q") or (choice == "Q")):
				print("Goodbye!")
				break
			else:
				print("Invalid input! Please choose from menu")
		return
		
#Run the program
sandbox = RSA_sandbox()
sandbox.run()