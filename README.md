# RSA_Encryption
A Python based implementation of RSA encryption for fixed point analysis


File overview:

encrypt.py ---- File containing RSA object implementation

encryption_test.py ---- Encrypts a string to test algorithm

exhaustive_hole_searcher.py --- Takes starting/ending index from user 
and generates transparency data to excel file

totient_bit_analyzer.py ---- Same as exhaustive_hole_searcher.py 
with optimized outputs to visualize totient bit patterns

primes1.txt ---- Text file of the first one million prime numbers


Specific_input_hole_analyzer.py ---- Takes two specific prime numbers,
and generates the transparency profile for E values

Excel Data----Contains all data

	-Transparency profile data: All transparency profile data organized
	by totient and pattern of the profile
	
	primes_1_to_100_holes.csv: Contains hole data for first 100 primes1
	
	primes_1_to_100_totient_patterns.csv: Same file as primes_1_to_100_holes.csv
	with totient optimized output



#Last edit: 12/9/2019 by Aron Schwartz