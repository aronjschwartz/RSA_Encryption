#Program: Finds all holes for a given RSA object
#Author: Aron Schwartz
#Last Edit: 10/21/2019


import encrypt


def analyze_holes(list):
	print("Holes found: ", len(list))
	for i in list:
		print(i)


def main():
	test_object = encrypt.encryption_set(p=17, q=23, custom_e=7, custom_d=31, custom_k=9)
	test_object.to_String()
	
	holes = []
	integer_list = [i for i in range(2, test_object.n-1)]
	encrypted_integers = []
	
	for i in integer_list:
		encrypted_integers.append(int(test_object.encrypt_int(i)))
		
	for index, val in enumerate(integer_list):
		if integer_list[index] == encrypted_integers[index]:
			holes.append(val)
			
	print("The valid e list: ")
	print(test_object.valid_e_list)
	
	#analyze_holes(holes)
	
	
main()