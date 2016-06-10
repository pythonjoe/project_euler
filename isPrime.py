def isPrime(num):
	if num == 1:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False
	
	return True
	

def largestPrimeFactor(num):
	for i in range(num, 1, -1):
		if num % i == 0 and isPrime(i):
			return i

print(largestPrimeFactor(13195))


