#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):  
    """ If the total is 0 or less, we need 0 coins """ 
    if total <= 0:  
        return 0  
    
    """ Initialize dp array  """
    dp = [float('inf')] * (total + 1)  
    
    """ Base case: No coins are needed to make 0  """
    dp[0] = 0  
    
    """ Fill the dp array  """
    for coin in coins:  
        for j in range(coin, total + 1):  
            if dp[j - coin] != float('inf'):  
                dp[j] = min(dp[j], dp[j - coin] + 1)  

    """ If we cannot make change for the total amount, return -1  """
    if dp[total] == float('inf'):  
        return -1  
    
    return dp[total]  
