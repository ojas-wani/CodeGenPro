class SubtractProductAndSum:
    """
    A solution class for the problem of subtracting the product and sum of digits of an integer.
    """
    def subtract_product_and_sum(self, num: int) -> int:
        """
        This method calculates the difference between the product and sum of the digits of a given number.

        Args:
            num (int): The input number.

        Returns:
            int: The difference between the product and sum of the digits of the input number.
        """
        product = 1
        sum_digits = 0
        for digit in str(num):
            product *= int(digit)
            sum_digits += int(digit)
        return product - sum_digits

************* Module 1281-subtract-the-product-and-sum-of-digits-of-an-integer