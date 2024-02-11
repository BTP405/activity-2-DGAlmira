def isPrime(n):
    """Returns if a number is prime (true) or not (false)."""
    isPrime = True;
    for num in range(2, n):
        if (n % num) == 0:
            isPrime = False; 
            break;
    return isPrime;
    
def getPrimeNumbers(n):
    """Return a list of all prime numbers within the range 2 and n."""
    primes = [x for x in range(2, n + 1) if isPrime(x)];
    return primes;

a = getPrimeNumbers(11);
print(a);