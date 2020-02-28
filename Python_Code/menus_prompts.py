#********************************************************
#*                                                  
#* File:        menus_prompts.py
#* Description: Defines menu, submenu, and prompt structure
#*              for all program routines
#*
#* Author: Aron Schwartz
#* Last Edit: 1/26/2020
#*
#********************************************************

#************************************
#									*
#            Prompt Functions     	*
#									*
#************************************

def main_menu_selection_prompt():
	selection = input("Enter selection (M/m to reload menu): ") 
	return selection

def selection_prompt():
	selection = input("Enter selection (q to quit): ")
	return selection

#************************************
#									*
#            Menu Functions     	*
#									*
#************************************

def display_main_menu():
	print("\n\n************ MAIN MENU *************\n")
	print("1  - Encrypt/Decrypt without padding")
	print("2  - Encrypt/Decrypt with padding")
	print("3  - Manage Septuples")
	print("4  - Manage Keys")
	print("5  - Manage Prime Numbers")
	print("6  - Manage Plaintext")
	print("7  - Analyze Fixed Points")
	print("8  - Display System Data")
	print("9  - Save/Load System data")
	print("10 - System Options")
	print("M  - Reload main menu")
	print("H  - Help Topics")
	print("Q  - Exit program\n")
	return

def help_menu():
	print("\n\n************ HELP MENU *************\n")
	print("1  - Encrypt/Decrypt without padding")
	print("2  - Encrypt/Decrypt with padding")
	print("3  - Manage Septuples")
	print("4  - Manage Keys")
	print("5  - Manage Prime Numbers")
	print("6  - Manage Plaintext")
	print("7  - Analyze Fixed Points")
	print("8  - Display System Data")
	print("9  - Save/Load System data")
	print("10 - RSA Sandbox Overview Help")
	print("Q  - Return to main menu\n")
	return
	
def encryption_selection_menu():
	print("\n\n******** ENCRYPTION MENU ********\n")
	print("1 - Encrypt plain text file")
	print("2 - Encrypt an input string")
	print("Q - Return to main menu\n")
	return 
	
def septuple_selection_menu():
	print("\n\n******** SEPTUPLE MANAGEMENT MENU ********\n")
	print("1 - Change active septuple")
	print("2 - Add Septuple")
	print("3 - Create septuples from primes")
	print("4 - Clear septuples")
	print("5 - View septuples")
	print("Q - Return to main menu\n")
	return
	
def primes_selection_menu():
	print("\n\n******** PRIMES MANAGEMENT MENU ********\n")
	print("1 - Generate prime list")
	print("2 - Generate prime list (display only)")
	print("3 - Clear prime list")
	print("4 - Display prime list")
	print("Q - Return to main menu\n")
	return
	
def holes_search_menu():
	print("\n\n******** FIXED POINT ANALYSIS MENU ********\n")
	print("1 - Analyze active septuple")
	print("2 - Compare all septuples")
	print("3 - Generate transparency profile")
	print("Q - Return to main menu\n")
	return
	
def system_data_menu():
	print("\n\n******** SYSTEM DATA MANAGEMENT MENU ********\n")
	print("1 - Save data to profile")
	print("2 - Load data from profile")
	print("Q - Return to main menu\n")
	return
	
def key_generation_menu():
	print("\n\n******** KEY MANAGEMENT MENU ********\n")
	print("1 - Add keys")
	print("2 - Swap keys")
	print("3 - Clear keys")
	print("4 - View keys")
	print("5 - Add keys from prime list")
	print("6 - Add keys to all septuples from prime list")
	print("Q - Return to main menu\n")
	return 

def system_options_menu():
	print("\n\n******** SYSTEM OPTIONS MENU ********\n")
	print("1 - Toggle Verbose mode")
	print("2 - Toggle Hex Mode")
	print("Q - Return to main menu\n")
	return 

def welcome_message():
	print("*********************************************************")
	print("*                                                       *")
	print("*          Welcome to the RSA Encyrption Sandbox        *")
	print("*                                                       *")
	print("*********************************************************")
	print()
	return