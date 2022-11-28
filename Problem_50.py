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
	
def findMaxPrimeSum2(n):
    max_terms = 0
    primes = efficientPrimeGenerator(n)
    nbPrimes = len(primes)
    for nbTerms in range(2,nbPrimes):
        print("Sums of ",nbTerms," primes")
        sum=0
        # FRIST SUM
        for i in range(nbTerms):
                sum=sum+primes[i]
        if sum in primes:
            max_terms = nbTerms
            print("\t",sum," is prime. It's a ",max_terms,"terms sum")
        elif sum>n:
            break
        else:
        
                # NEXT SUMS
            for start in range(1,nbPrimes-nbTerms):
                #print("\tSum starting with ",start,"th prime")
                sum=sum-primes[start-1]+primes[start+nbTerms-1]
                #print("\t\tSUM=SUM - ",primes[start-1]," + ",primes[start+nbTerms-1])
               # print("\tSum = ",sum)
                if sum in primes:
                    max_terms = nbTerms
                    print("\t",sum," is prime. It's a ",max_terms,"terms sum starting with",primes[start])
                    break
                elif sum>n:
                    break
    return max_terms
	
a=findMaxPrimeSum2(1000000)
print(a)
	
