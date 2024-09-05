#!/usr/bin/python3  

def isWinner(x, nums):  
    """Function to determine the number of prime numbers up to n using  
     the Sieve of Eratosthenes  """
    def count_primes(n):  
        if n < 2:  
            return 0  
        is_prime = [True] * (n + 1)  
        is_prime[0] = is_prime[1] = False  
        for i in range(2, int(n**0.5) + 1):  
            if is_prime[i]:  
                for j in range(i * i, n + 1, i):  
                    is_prime[j] = False  
        return sum(is_prime)  

    maria_wins = 0  
    ben_wins = 0  

    for n in nums:  
        prime_count = count_primes(n)  
        """ If prime count is odd, Maria wins (as she goes first)  
         If prime count is even, Ben wins  """
        if prime_count % 2 == 1:  
            maria_wins += 1  
        else:  
            ben_wins += 1  

    if maria_wins > ben_wins:  
        return "Maria"  
    elif ben_wins > maria_wins:  
        return "Ben"  
    else:  
        return None
