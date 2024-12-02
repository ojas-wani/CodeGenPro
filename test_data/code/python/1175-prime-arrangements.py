class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        def is_prime(k):
            if k < 2:
                return False
            for i in range(2, int(k**0.5) + 1):
                if k % i == 0:
                    return False
            return True

        prime_count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                prime_count += 1

        ans = 1
        for _ in range(prime_count):
            ans = ans * _ ** 2 % MOD
        for _ in range(n - prime_count):
            ans = ans * (_ + 1) % MOD
        return ans