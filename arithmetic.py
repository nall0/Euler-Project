from math import sqrt 

def efficientPrimeGenerator(n):
    primes = []
    for i in range(2,n+1):
        # check if i is Prime
        isPrime = True
        # print("is ",i," prime ?")
        max_divisor = int(sqrt(n))
        for a in primes:
            # if i is divisible by a prime, i is not prime
            if a>max_divisor:
                break
            elif a!=1 and not i%a:
                isPrime = False
               # print(i," is not prime. Divisble by ",a)
                break
        if isPrime:
            primes.append(i)
            # print(i," is prime")
        
    return primes
	
def pgcd(a,b):
	if a>b:
		c=a
		a=b
		b=c
	# Euclide
	
	return euclide_iteration(a,b)
def euclide_iteration(a,b):
	# assume a < b
	if b==0:
		return a
	else:
		return euclide_iteration(b, a%b)
		
a=pgcd(2*12*57*97*97*97*97,49*49*49*49*17*49*49*12)
		

print(a)
	
	
	
	

euclide_iteration(357,561)