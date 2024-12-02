class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_digits = 0
        for digit in str(n):
            product *= int(digit)
            sum_digits += int(digit)
        return product - sum_digits