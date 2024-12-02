Python
def Solution():
    """
    The Solution class.
    """

    def tribonacci(n: int) -> int:
        """
        The Tribonacci sequence Tn is defined as follows:
        T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
        Given `n`, return the value of Tn.
        
        Parameters:
        n (int): The Tribonacci number to return.

        Returns:
        int: The Tribonacci number.
        """
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        else:
            tribonacci_term1, tribonacci_term2, tribonacci_term3 = 0, 1, 1
            for _ in range(3, n + 1):
                tribonacci_term1, tribonacci_term2, tribonacci_term3 = tribonacci_term2, tribonacci_term3, tribonacci_term1 + tribonacci_term2 + tribonacci_term3
            return tribonacci_term3

if __name__ == "__main__":
    # Add your main code here
    print(Solution().tribonacci(4))