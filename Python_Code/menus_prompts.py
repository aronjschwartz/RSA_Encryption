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
#Prompts
def main_menu_selection_prompt():
	selection = input("Enter selection (M/m to reload menu): ") 
	return selection

def selection_prompt():
	selection = input("Enter selection (q to quit): ")
	return selection

#Menus
def display_main_menu():
	print("1  - Encrypt/Decrypt without padding")
	print("2  - Encrypt with padding")
	print("3  - Manage Keys")
	print("4  - Manage Prime Numbers")
	print("5  - Analyze Holes")
	print("6  - Output Results")
	print("7  - Manage Septuples")
	print("8  - Analyze Septuples")
	print("9  - Plaintext Message Selection")
	print("10 - Specify Ciphertext")
	print("11 - Display System Data")
	print("12 - Save/Load System data")
	print("M  - Reload main menu")
	print("H  - Help Topics")
	print("Q  - Exit program\n")
	return

def help_menu():
	print("\n\n************ HELP MENU *************")
	print("1  - Encrypt/Decrypt without padding")
	print("2  - Encrypt with padding")
	print("3  - Manage Keys")
	print("4  - Manage Prime Numbers")
	print("5  - Analyze Holes")
	print("6  - Output Results")
	print("7  - Manage Septuples")
	print("8  - Analyze Septuples")
	print("9  - Plaintext Message Selection")
	print("10 - Specify Ciphertext")
	print("11 - Display System Data")
	print("12 - Save/Load System data")
	print("Q  - Return to main menu\n")
	return
	
def encryption_selection_menu():
	print("1 - Encrypt plain text file")
	print("2 - Encrypt an input string")
	print("Q - Return to main menu\n")
	return 
	
def septuple_selection_menu():
	print("1 - Change active septuple")
	print("2 - Add Septuple")
	print("3 - Clear septuples")
	print("4 - View septuples")
	print("Q - Return to main menu\n")
	return
	
def primes_selection_menu():
	print("1 - Generate prime list")
	print("2 - Generate prime list (display only)")
	print("3 - Clear prime list")
	print("4 - Display prime list")
	print("Q - Return to main menu\n")
	return
	
def holes_search_menu():
	print("1 - Analyze septuple")
	print("2 - Compare all septuples")
	print("Q - Return to main menu\n")
	return
	
def system_data_menu():
	print("1 - Save data")
	print("2 - Load data")
	print("Q - Return to main menu\n")
	return
	
def key_generation_menu():
	print("1 - Add keys")
	print("2 - Clear keys")
	print("3 - View keys")
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