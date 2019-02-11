from multiprocessing import Pool
import time

def sum_prime(n):
	sum_p = 0
	current_n = 2
	while current_n <= n:
		if is_prime(current_n):
			sum_p += current_n
		current_n += 1
	return sum_p

def is_prime(n):
	if n <= 1:
		return False
	elif n <= 3:
		return True
	elif num%2 == 0 or num%3 == 0:
		return False
	i = 5
	while i**2 <= n:
		if n%i == 0 or n%(i+2) == 0:
			return False
		i += 6
	return True

if __name__ = '__main__':
	start = time.time()
	with Pool(1) as p:
		print(p.map(sum_prime), [1000000, 2000000, 3000000])
	print("Time taken = {0:.5f}".format(time.time() - start))