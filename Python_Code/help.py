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
	print("The septuple management menu allows user to create septuples, change the active septuple,")
	print("create septuples from primes, clear the septuple data, or simply view all septuples")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def plaintext_selection_help():
	print("************* Plaintext Management Help Overview **************")
	print("The plaintext managment menu allows a user to select a plaintext file to encrypt")
	print("The files are read out of the Plaintext folder, and should be text files")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def display_system_data_help():
	print("************* Display System Data Help Overview **************")
	print("The display system data option allows a user to view all septuples, primes,")
	print("keys, and plaintext data loaded into the program.  Users can choose to display")
	print("data verbosely, which will show key data for each septuple")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def save_load_data_help():
	print("************* Save/Load System Data Help Overview **************")
	print("The save/load menu allows saving or loading of user profiles containing")
	print("system data.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
def RSA_Sandbox_overview():
	print("************* RSA Sandbox Help Overview **************")
	print("The RSA Sandbox is a research tool that enables users to explore and experiment with the RSA")
	print("encryption algorithm.  The program allows a user to create RSA encryption 'septuples', generate ")
	print("prime numbers, create encryption keys, and combine the three to search for fixed point patterns.")
	print("In addition, users can encrypt plaintext to file, output results in comma separated format, and ")
	print("save all system data to a user profile to pick up again later.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")
	
	
	
	
	
	
	
	
	