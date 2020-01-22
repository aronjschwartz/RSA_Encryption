#********************************************************
#*                                                  
#*                     RSA Sandbox 
#*
#********************************************************

from encrypt import encryption_set
import time
import math
	
class RSA_sandbox():
	
	def __init__(self):
		self.plain_text = None
		self.active_encryption_object = None
		self.encryption_objects = []
		self.public_keys = [3, 5, 17, 257, 65537]
		self.welcome_message()
		self.display_main_menu()
		
		
	def display_main_menu(self):
		print("1  - Encrypt/Decrypt without padding")
		print("2  - Encrypt with padding")
		print("3  - Generate Keys")
		print("4  - Generate Prime Numbers")
		print("5  - Find Holes")
		print("6  - Output Results")
		print("7  - Create/View Septuples")
		print("8  - Analyze Septuple")
		print("9  - Plaintext Message Selection")
		print("10 - Specify Ciphertext")
		print("M  - Reload main menu")
		print("H  - Help Topics")
		print("Q  - Exit program\n")
		
	def encryption_selection_menu(self):
		print("1 - Encrypt plain text file")
		print("2 - Encrypt an input string")
	
	def septuple_selection_menu(self):
		print("1 - Change active septuple")
		print("2 - Add Septuple")
		print("3 - Clear septuples")
		print("4 - View septuples")
		print("Q - Return to main menu")
		
	
	#Borrowed from provided code from Professor Shirley (ElementalNumberTheory.py)
	def primes(self, n):
		if n <= 1:
			return []
		X = [i for i in range(3, n + 1, 2)]                         # (1)
		P = [2]                                                     # (2)
		sqrt_n = math.sqrt(n)                                       # (3)
		while len(X) > 0 and X[0] <= sqrt_n:                        # (4)
			p = X[0]                                                # (5)
			P.append(p)                                             # (6)
			X = [a for a in X if a % p != 0]                        # (7)
		return P + X                                                # (8)

	def welcome_message(self):
		print("*********************************************************")
		print("*                                                       *")
		print("*          Welcome to the RSA Encyrption Sandbox        *")
		print("*                                                       *")
		print("*********************************************************")
		print()
		
	def main_menu_selection_prompt(self):
		selection = input("Enter selection (M/m to reload menu): ") 
		return selection
	
	def selection_prompt(self):
		selection = input("Enter selection: ")
		return selection
	
	def create_septuple_user_input(self):
		p_choice = int(input("Enter p: "))
		q_choice = int(input("Enter q: "))
		choice = input("Specify e? [Y/N]: ")
		if ((choice == "y") or (choice == "Y")):
			e_choice = int(input("Select e: "))
			septuple_object = encryption_set(p=p_choice, q=q_choice, custom_e = e_choice)
		else:
			septuple_object = encryption_set(p =p_choice, q=q_choice, custom_e = 65537)
		print("/nEncryption object created!")
		septuple_object.to_String()
		print()
		return septuple_object
	
	def encryption_decryption_no_padding(self):
		print("Encrypt/Decrypt without padding selected")
		#Check for an active septuple
		if self.active_encryption_object is None:
			print("No active encryption object detected, generating...")
			#Get p and q from the user, and see if they want to specify other values
			p_choice = int(input("Enter p: "))
			q_choice = int(input("Enter q: "))
			choice = input("Specify e? [Y/N]: ")
			if ((choice == "y") or (choice == "Y")):
				e_choice = int(input("Select e: "))
				self.active_encryption_object = encryption_set(p=p_choice, q=q_choice, custom_e = e_choice)
			else:
				self.active_encryption_object = encryption_set(p =p_choice, q=q_choice, custom_e = 65537)
			print("Encryption object created!")
			self.active_encryption_object.to_String()
		else:
			print("Active septuple: ", self.active_encryption_object.get_septuple())
		self.encryption_objects.append(self.active_encryption_object)
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
			plain_text_ascii = self.get_ascii_list(plain_text_string)

			#Encrypt each number in the plain-text ascii list to obtain the cipher-ascii list
			for i in plain_text_ascii:
				cipher_ascii.append(int(self.active_encryption_object.encrypt_int(i)))
				
			#Generate the cipher text from the cipher-ascii list
			cipher_text = self.get_string_from_ascii(cipher_ascii)
			
			
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
			
	#Function to return an ascii list from a string
	def get_ascii_list(self, input_string):
		out = []
		for i in input_string:
			out.append(ord(i))
		return out

	#Function to return a string from an ascii list
	def get_string_from_ascii(self, input_list):
		out = ""
		for i in input_list:
			out += chr(i)	
		return out

		
	def encrypt_padding(self):
		print("Encryption with padding selected")

	def generate_keys(self):  
		print("Key generation selected")

	def generate_primes(self):
		print("Prime number generation selected")
		n = input("Enter upper limit for prime generation: ")
		prime_list = self.primes(int(n))
		print(prime_list)

	def hole_search(self):
		print("Hole search selected, analyzing the active septuple ", self.active_encryption_object.get_septuple)
		#Analyze the holes in the septuple
		holes_num = self.search_septuple(self.active_encryption_object)
		
		#Round transparency to nearest hundreth
		transparency = round((float(holes_num)/(self.active_encryption_object.n -1))*100, 2)
		print("***** Results *****: ")
		print("Septuple: ", self.active_encryption_object.get_septuple())
		print("Holes found: ", holes_num, " Transparency: ", transparency, "%")
		print()

	def output_results(self):
		print("Result output and visualization selected")
	
	
	def view_septuples(self):
		print("*** Displaying septuple list (" + str(len(self.encryption_objects)) + " loaded) ***")
		for index, object in enumerate(self.encryption_objects):
			print(index + 1, " - ", object.get_septuple())
	
	def specify_septuples(self):
		print("Specify septuples selected")
		self.view_septuples()
		self.septuple_selection_menu()
		choice = self.selection_prompt()
		while(1):
			if (choice == "1"):
				print("1")
				#Change active
			elif (choice == "2"):
				print("Creating septuple..")
				septuple = self.create_septuple_user_input()
				self.encryption_objects.append(septuple)
				choice = self.selection_prompt()
			elif (choice == "3"):
				print("Clearing septuple list...")
				self.encryption_objects.clear()
				choice = self.selection_prompt()
			elif (choice == "4"):
				self.view_septuples()
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