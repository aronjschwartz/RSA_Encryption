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
from menus_prompts import *
from encryption_test import *
from save_load import *
from help import *
import time
import math
import shutil

class RSA_sandbox():
	
	#************************************
	#									*
	#            Init function     		*
	#									*
	#************************************

	def __init__(self):
		#Internal data
		self.plain_text = None
		self.plain_text_file = None
		self.cipher_text = None
		self.cipher_text_file = None
		self.active_encryption_object = None
		self.encryption_objects = []
		self.prime_list = []
		self.encryption_keys = {} 
		self.public_keys = [3, 5, 17, 257, 65537]
		
		if not os.path.exists("./Plaintext/"):
			os.mkdir("./Plaintext/")
		
		if not os.path.exists("./Ciphertext/"):
			os.mkdir("./Ciphertext/")
		
		if not os.path.exists("./Results/"):
			os.mkdir("./Results/")
		
		
		self.welcome_message()
		self.display_main_menu()
		
	#************************************
	#									*
	#        Menu calling functions    	*
	#									*
	#************************************
	
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
	
	#************************************
	#									*
	#      Prompt calling functions    	*
	#									*
	#************************************
	
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
		if os.path.exists("./" + str(folder_name)):
			shutil.rmtree("./" + str(folder_name))
		#Make the folder
		os.mkdir(folder_name)
		#Call the function to save the encryption object data
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
		if os.path.isdir("./" + str(folder_name)):
			print("Folder '", str(folder_name), "' found! Loading settings...")
			#Call the load functions to reload system data
			self.encryption_objects = load_encryption_objects(folder_name)
			self.encryption_keys = load_key_data(folder_name)
			self.prime_list = load_primes_data(folder_name)
			self.active_encryption_object = load_active_object_data(folder_name)
			print("******** Load Successful! **********")
		#Error message if folder not found
		else:
			print("Folder '", str(folder_name), "' does not exist! Data load failed")
		return
	
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
			#Load septuples
			elif(choice == "3"):
				print("Load septuples")
				system_data_menu()
				choice = selection_prompt()
			#Load keys
			elif(choice == "4"):
				print("Load keys")
				system_data_menu()
				choice = selection_prompt()
			#Load plaintext
			elif(choice == "5"):
				plaintext_folder = os.listdir("./Plaintext/")
				if len(plaintext_folder) == 0:
					print("Plaintext folder is empty!")
				else:
					for index, file in enumerate(plaintext_folder):
						print(str(index), " - ", str(file))
						choice = selection_prompt()
						try:
							self.plain_text_file = "./Plaintext/" + str(file)
							with open(self.plain_text_file) as f:
								self.plain_text = f.read()
						
						
						except IndexError:
							print("Invalid choice")
							pass
						
						
						
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
		count = 1
		print("******* DISPLAYING SYSTEM DATA ********")
		self.view_septuples_with_keys()
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
			if (self.active_encryption_object.get_septuple() == object.get_septuple()):
				print(index, " - ", str(object.get_septuple()) + " *** active ***")
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
			if (self.active_encryption_object.get_septuple() == object.get_septuple()):
				print(index, " - ", str(object.get_septuple()) + " *** active ***")
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
	
	#************************************************************************************
	#																					*
	#  create_septuple_user_input(): Creates a septuple from user input.  Allows for    *
	#                                selection of primes and e value					*
	#																					*
	#************************************************************************************
	
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
					print("No plaintext loaded!")
				else:
					print("Use active object? ", str(self.active_encryption_object.get_septuple()), "? [Y/N]: ")
					choice = selection_prompt()
					if((choice == "Y") or (choice == "y")):
						self.cipher_text = self.active_encryption_object.encrypt_int_list(get_ascii_list(self.plain_text))
						decrypted = self.active_encryption_object.decrypt_int_list(self.cipher_text)
						print("The plain text is: ", self.plain_text)
						print("The ciphertext is: ", get_string_from_ascii(self.cipher_text))
						print("Decrypted: ", get_string_from_ascii(decrypted))
						break
					else:
						print("Choose septuple")
				
				
				
				
				self.encryption_selection_menu()
				choice = self.selection_prompt()
			#Encrypt an input string from the user
			elif (choice == "2"):
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
				for encryption_key in self.encryption_keys[key]:
					print("(", key.get_n(), ",",encryption_key, ")")
		return
	
	
	
	#*********************************************************************************************
	#																							 *
	#  add_key_to_septuple(): Appends a key to a given septuple in the system data dictionary    *
	#																							 *
	#*********************************************************************************************
	
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
	
	#****************************************************************
	#																*
	#  manage_keys(): Handles the key management functionality	    *
	#																*
	#****************************************************************
	
	def manage_keys(self):  
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
			#Swap keys
			elif (choice == "2"):
				if (len(self.encryption_objects) == 0):
					print("No septuples loaded!")
					self.key_generation_menu()
					choice = selection_prompt()
				else:
					self.view_septuples()
					sept_choice = input("Select septuple to swap key: ")
					self.show_keys_for_septuple(self.encryption_objects[int(sept_choice)])
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
									if (self.active_encryption_object.get_septuple() == old_septuple.get_septuple()):
										self.active_encryption_object = new_sept
								found = True
								break
						if found == True:
							break
					if(found == False):
						print("Key doesnt exist, adding to data and swapping...")
						if (self.encryption_objects[int(sept_choice)].swap_out_e_value(int(key_choice)) == True):
							self.add_key_to_septuple(self.encryption_objects[int(sept_choice)], int(key_choice))
							self.encryption_keys[self.encryption_objects[int(sept_choice)]] = self.encryption_keys[old_septuple]
							del self.encryption_keys[old_septuple]
							print("Success!")
				print("THE KEY LIST IS: ")
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
				self.show_keys_for_septuple(self.encryption_objects[int(choice)])
				self.key_generation_menu()
				choice = selection_prompt()
			elif ((choice == "q") or (choice == "Q")):
				break
	
	
	
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
	
	def format_results_with_keys(self, septuple, holes_num, transparency):
		result_string = "Septuple: " + str(septuple) + ", Key: " + str(septuple[4]) + ", Holes found: " + str(holes_num) + ", Transparency: " + str(transparency)
		return result_string
		
	def format_results(self, septuple, holes_num, transparency):
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
					choice = input("No object loaded! Create one? [Y/N]: ")
					if ((choice == "y") or (choice == "Y")):
						septuple = self.create_septuple_user_input()
						self.encryption_objects.append(septuple)
				
						if len(self.encryption_objects) == 1:
							self.active_encryption_object = septuple
					else:
						print("Returning to main menu")
						break
				print("Analyzing active septuple: ", self.active_encryption_object.get_septuple())
				#Analyze the holes in the septuple
				holes_num = self.active_encryption_object.search_holes()
				
				#Round transparency to nearest hundreth
				transparency = round((float(holes_num)/(self.active_encryption_object.n -1))*100, 2)
				print("***** Results *****: ")
				print(self.format_results(self.active_encryption_object.get_septuple(), holes_num, transparency))
				
				holes_search_menu()
				choice = selection_prompt()
			#Compare all septuples, display results sorted by transparency
			elif(choice == "2"):
				result_transparency_dict = {}
				transparency_list = []
				#Gather results for all the septuples
				for septuple in self.encryption_objects:
					#Analyze the holes in the septuple
					holes_num = septuple.search_holes()
					#Round transparency to nearest hundreth
					transparency = round((float(holes_num)/(septuple.n -1))*100, 2)
					result_string = self.format_results(septuple.get_septuple(), holes_num, transparency)
					result_transparency_dict[transparency] = result_string
					transparency_list.append(transparency)
				
				#Display the results sorted by transparency
				print("\n\n*********** RANKED RESULTS **************")
				for transparency in list(reversed(sorted(transparency_list))):
					for key, value in result_transparency_dict.items():
						if key == transparency:
							print(value, "%")
				print()
				holes_search_menu()
				choice = selection_prompt()
			#Generate transparency profile
			elif(choice == "3"):
			
				result_transparency_dict = {}
				transparency_list = []
			
				for index, object in enumerate(self.encryption_objects):
					print(str(index) + " - " + str(object.get_septuple()))
				choice = input("Select septuple: ")
				sept = self.encryption_objects[int(choice)]
				for key, value in self.encryption_keys.items():
					if key.get_septuple() == sept.get_septuple():
						for encryption_key in value:
							temp_sept = encrypt.encryption_set(p=sept.get_p(), q=sept.get_q(), custom_e=int(encryption_key))
							holes_num = temp_sept.search_holes()
							#Round transparency to nearest hundreth
							transparency = round((float(holes_num)/(sept.n -1))*100, 2)
							result_string = self.format_results_with_keys(temp_sept.get_septuple(), holes_num, transparency)
							result_transparency_dict[transparency] = result_string
							transparency_list.append(transparency)
				
				#Display the results sorted by transparency
				print("\n\n*********** RANKED RESULTS **************")
				for transparency in list(reversed(sorted(transparency_list))):
					for key, value in result_transparency_dict.items():
						if key == transparency:
							print(value, "%")
							
				
				holes_search_menu()
				choice - selection_prompt()
				
			
			elif((choice == "q") or (choice == "Q")):
				break
			else:
				print("Invalid choice!")
				holes_search_menu()
				choice = selection_prompt()
		
		return
		
	def output_results(self):
		print("Result output and visualization selected")
	

	#*************************************************************************
	#																		 *
	#  manage_septuples():  Handles the septuple management functionality 	 *
	#															    	     *
	#*************************************************************************
	
	def manage_septuples(self):
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
				
				if len(self.encryption_objects) == 1:
					self.active_encryption_object = septuple
				
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
		
		
	def analyze_septuples(self):	
		print("Analyze septuple selected")
		
	def set_plaintext(self):
		plaintext_management_menu()
		choice = selection_prompt()
	
	
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
				manage_keys_help()
			elif(choice == "4"):
				manage_primes_help()
			elif(choice == "5"):
				analyze_holes_help()
			elif(choice == "6"):
				output_results_help()
			elif(choice == "7"):
				manage_septuples_help()
			elif(choice == "8"):
				plaintext_selection_help()
			elif(choice == "9"):
				print("Ciphertext help selected")
			elif(choice == "10"):
				display_system_data_help()
			elif(choice == "11"):
				save_load_data_help()
			elif(choice == "12"):
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
				self.manage_keys()
			elif(choice == "4"):
				self.manage_primes()
			elif(choice == "5"):
				self.analyze_holes()
			elif(choice == "6"):
				self.output_results()
			elif(choice == "7"):
				self.manage_septuples()			
			elif(choice == "8"):
				self.set_plaintext()
			elif(choice == "9"):
				self.display_system_data()
			elif(choice == "10"):
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
		return
		
#Run the program
sandbox = RSA_sandbox()
sandbox.run()