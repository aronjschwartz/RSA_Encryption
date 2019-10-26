#Program: Analyzes all holes for all possible septuple combinations up to the end of the prime list
#Author: Aron Schwartz
#Last Edit: 10/25/2019

import encrypt


#Function takes a RSA object and returns a list of all holes from 2 to n-2
def search_septuple(rsa_object):
	
	#List to hold the holes
	holes = []
	#Generate the plaintext list of integers
	integer_list = [i for i in range(2, rsa_object.n-1)]
	#List to hold the encrypted integers
	encrypted_integers = []
	
	#Encrypt all the integers and store them in the encrypted integer list
	for i in integer_list:
		encrypted_integers.append(int(rsa_object.encrypt_int(i)))
	
	#Loop through the original list and check for all cases where the plaintext=cipher text
	for index, val in enumerate(integer_list):
		if integer_list[index] == encrypted_integers[index]:
			holes.append(val)
	#Return a list of all holes found for the given septuple
	return holes
	
	
def run():
	
	

	#List of the first few primes 
	p_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
	q_list = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
	e_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
	
	p_index = 0
	q_index = 0
	e_index = 0
	for p_val in p_list:
		q_index = 0
		for q_val in q_list:
			print("Checking q_val: ", q_val, " q index is: ", q_index)
			e_index = 0
			#Check all the public keys for each p/q combination
			while(1):
				temp_object = encrypt.encryption_set(p=p_list[p_index], q=q_list[q_index], custom_e=e_list[e_index])
				sept = temp_object.get_septuple();
				print(sept)
				e_index +=1
				
				if (e_index == (len(e_list) - 1)):
					print("BREAK REACHED")
					break
			q_index +=1
		p_index +=1
	
	
	
	#with open('csvfile.csv','w') as file:
	#	file.write(header)
	#	file.write('\n')
	#	file.write('E-D-K:')
		#file.write(str(test_object.e) + " " + str(test_object.d) + " " + str(test_object.k))
		#file.write(',Holes: ' + str(len(holes_list)))
	
	
run()	
	
	