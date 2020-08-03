#********************************************************
#*                                                  
#* File:        sandbox_options.py
#* Description: Defines system options for the RSA sandbox
#*
#* Author: Aron Schwartz
#* Last Edit: 2/8/2020
#*
#********************************************************



class sandbox_options():

	#Define the system options as toggleable booleans
	def __init__(self):
		self.verbose_output = False
		self.hex_mode_display = False
		self.hex_mode_plaintext = False
		
		
	def check_verbose(self):
		return self.verbose_output
	
	def check_hex_display(self):
		return self.hex_mode_display
	
	def check_hex_plaintext(self):
		return self.hex_mode_plaintext
	
	def toggle_verbose(self):
		if self.verbose_output == True:
			self.verbose_output = False
		else:
			self.verbose_output = True
		return
		
	def toggle_hex_display(self):
		if self.hex_mode_display == True:
			self.hex_mode_display = False
		else:
			self.hex_mode_display = True
		return 
	
	def toggle_hex_plaintext(self):
		if self.hex_mode_plaintext == True:
			self.hex_mode_plaintext = False
		else:
			self.hex_mode_plaintext = True
		return 
	def display_options_status(self):
		print("Verbose mode       - ", str(self.verbose_output))
		print("Hex Display mode   - ", str(self.hex_mode_display))
		print("Hex Plaintext Mode - ", str(self.hex_mode_plaintext))