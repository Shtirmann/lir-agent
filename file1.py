def fib(a):
  """
  Calculates the Fibonacci number at the specified position.

  Args:
      a: The position in the Fibonacci sequence for which to calculate the Fibonacci number.

  Returns:
      The Fibonacci number at the given position.
  """
  if a <= 1:
    return 1
  return fib(a - 1) + fib(a - 2)
