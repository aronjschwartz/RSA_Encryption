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
	print("Encryption no padding help")
	
def encryption_padding_help():
	print("Encryption padding help")

def manage_keys_help():
	print("************* Manage Keys Help Overview **************")
	print("\nThe manage keys option allows a user to create, delete, and view public keys")
	print("for any loaded encryption object.  The functionality is implemented as a dictionary")
	print("allowing any number of keys to be associated with a given encryption object.  Users can")
	print("view the keys of the object, add/delete keys, and swap out the 'active' key for an object")
	print("using the menu options.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def manage_primes_help():
	print("************* Manage Primes Help Overview **************")
	print("\nThe manage primes option allows a user to create, delete, and manipulate an internal list ")
	print("of prime numbers.  These numbers can be used in enhance hole analysis flexibility, in addition ")
	print("to allowing encryption objects to be created from filtered ranges of prime numbers.")
	print("\nFor a more detailed overview, please see the RSA Sandbox user manual.\n")

def analyze_holes_help():
	print("Analayze hols help")


def output_results_help():
	print("Output help")


def manage_septuples_help():
	print("Manage septuples help")


def plaintext_selection_help():
	print("Plaintext help")

def display_system_data_help():
	print("Display data help")

def save_load_data_help():
	print("Save load help")

def RSA_Sandbox_overview():
	print("overview help")
