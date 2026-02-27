def fib(n):
    """
    Calculates the nth Fibonacci number using a recursive approach.
    
    Args:
        n: The position in the Fibonacci sequence to calculate.
    
    Returns:
        The nth Fibonacci number.
    """
  if n <= 1:
    return 1
  return fib(n - 1) + fib(n - 2)
