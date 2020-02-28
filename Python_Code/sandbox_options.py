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
		self.verbose_output = True
		self.hex_mode = True
		
	def check_verbose(self):
		return self.verbose_output
	
	def check_hex(self):
		if self.hex_mode == True:
			return True
	
	def toggle_verbose(self):
		if self.verbose_output == True:
			self.verbose_output = False
		else:
			self.verbose_output = True
		return
		
	def toggle_hex(self):
		if self.hex_mode == True:
			self.hex_mode = False
		else:
			self.hex_mode = True
		return 
	
	def display_options_status(self):
		print("Verbose mode - ", str(self.verbose_output))
		print("Hex mode     - ", str(self.hex_mode))