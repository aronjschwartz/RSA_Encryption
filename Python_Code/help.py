#********************************************************
#*                                                  
#* File:        help.py
#* Description: Implements the help functionality for the 
#* 				RSA sandbox application
#*
#* Author: Aron Schwartz
#* Last Edit: 1/28/2020
#*
#********************************************************

#************************************
#									*
#            Help Functions     	*
#									*
#************************************

def encryption_decryption_no_padding_help():
	print("************* Encryption/Decryption without paddng Help Overview **************")
	print("\n The encryption/decryption (no padding) option allows a user to encrypt and/or decrypt plaintext")
	print("from an input file, as well as encrypt/decrypt an input string without using a padding scheme.")
	print("The active septuple is used by default, and the plain text, cipher text, and decrypted cipher text is displayed.")
	print("Encrypting plaintext files will also generate a cipher text file and output to the cipher text folder.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
	
	
def encryption_padding_help():
	print("************* Encryption/Decryption with paddng Help Overview **************")
	print("\n The encryption/decryption option allows a user to encrypt and/or decrypt plaintext")
	print("from an input file, as well as encrypt/decrypt an input string using a formal padding scheme.")
	print("The active septuple is used by default, and the plain text, cipher text, and decrypted cipher text is display")
	print("Encrypting plaintext files will also generate a cipher text file and output to the cipher text folder.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def manage_keys_help():
	print("************* Manage Keys Help Overview **************")
	print("\nThe manage keys option allows a user to create, delete, and view public keys")
	print("for any loaded encryption object.  The functionality is implemented as a dictionary")
	print("allowing any number of keys to be associated with a given encryption object.  Users can")
	print("view the keys of the object, add/delete keys, and swap out the 'active' key for an object")
	print("using the menu options, create keys from prime numbers, etc.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def manage_primes_help():
	print("************* Manage Primes Help Overview **************")
	print("\nThe manage primes option allows a user to create, delete, and manipulate an internal list ")
	print("of prime numbers.  These numbers can be used in enhance hole analysis flexibility, in addition ")
	print("to allowing encryption objects  and keys to be created from filtered ranges of prime numbers.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def analyze_holes_help():
	print("************* Fixed Point Analysis Help Overview **************")
	print("\nThe fixed point analysis menu allows the analysis of keys and septuple combinations with")
	print("regards to fixed point occurence.  Users can analyze a specific septuple, compare all loaded")
	print("septuples, and compare all keys for a septuple")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def manage_septuples_help():
	print("************* Septuple Management Help Overview **************")
	print("The septuple management menu allows user to create septuples, as well as change the active septuple")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def plaintext_selection_help():
	print("Plaintext help")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def display_system_data_help():
	print("Display data help")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def save_load_data_help():
	print("Save load help")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def RSA_Sandbox_overview():
	print("overview help")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")