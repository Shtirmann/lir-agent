def fib(n):
    """
    Calculates the nth Fibonacci number using dynamic programming.
    
    Args:
        n: The position in the Fibonacci sequence to compute.
    
    Returns:
        int: The nth Fibonacci number.
    """
  dp = [0, 1]
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[n]
