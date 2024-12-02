Python
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        return [price - discount for i, price in enumerate(prices) for j, discount in enumerate(prices) if j > i and price >= discount]