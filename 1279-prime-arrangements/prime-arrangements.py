class Solution:
  def numPrimeArrangements(self, n: int) -> int:
    MOD = 1_000_000_007

    def factorial(n: int) -> int:
      fact = 1
      for i in range(2, n + 1):
        fact = fact * i % MOD
      return fact

