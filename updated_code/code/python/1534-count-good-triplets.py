Python
class CountGoodTriplets:
    """
    This class counts the number of good triplets in an array.

    Attributes:
    None

    Methods:
    count_good_triplets(arr, a, b, c) -> int: Returns the number of good triplets.
    """

    def count_good_triplets(self, arr: list, a: int, b: int, c: int) -> int:
        """
        Counts the number of good triplets in the array.

        A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
        * 0 <= i < j < k < arr.length
        * |arr[i] - arr[j]| <= a
        * |arr[j] - arr[k]| <= b
        * |arr[i] - arr[k]| <= c

        Args:
            arr (list): The array of integers.
            a (int): The first limit value.
            b (int): The second limit value.
            c (int): The third limit value.

        Returns:
            int: The number of good triplets.
        """
        res = 0  # Initialize the result
        n = len(arr)  # Get the length of the array

        # Initialize the left and right pointers
        i, j, k = 0, 0, 0

        # Sort the array
        arr.sort()

        # Check all possible triplets
        while j < n - 1:
            while k < n - 1:
                # Check if the current triplet is good
                while i < j and arr[i] + a >= arr[j]:
                    i += 1
                while k < n - 1:
                    if arr[j] + b >= arr[k]:
                        break
                    k += 1

                # If the current triplet is good, increment the result
                if arr[i] + a >= arr[j] and arr[j] + b >= arr[k]:
                    res += k - j

                k += 1
            j += 1

        return res