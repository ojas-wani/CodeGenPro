class Solution:
    """
    This class contains the method to reformat a phone number.
    """
    def reformatNumber(self, number: str) -> str:
        """
        Reformat the telephone number.

        Firstly, remove all spaces and dashes. Then, group the digits from left to right
        into blocks of length 3 until there are 4 or fewer digits. The final digits are then
        grouped as follows:
            * 2 digits: A single block of length 2.
            * 3 digits: A single block of length 3.
            * 4 digits: Two blocks of length 2 each.

        The blocks are then joined by dashes. Notice that the reformatting process should
        never produce any blocks of length 1 and produce at most two blocks of length 2.

        Args:
            number (str): The phone number to be reformatted.

        Returns:
            str: The reformatted phone number.
        """
        # Remove all spaces and dashes
        number = number.replace('-', '').replace(' ', '')

        # Initialize an empty list to store the blocks
        blocks = []

        # Initialize the index to 0
        i = 0

        # Loop until all digits are processed
        while i < len(number):
            # If there are 3 or more digits, add a block of 3
            if i + 2 < len(number):
                blocks.append(number[i:i+3])
                i += 3
            # If there are 2 or fewer digits remaining, add the remaining digits
            else:
                blocks.append(number[i:])
                break

        # If there are 2 blocks, add a dash between them
        if len(blocks) == 2:
            blocks.insert(1, '-')

        # Join the blocks with dashes
        return '-'.join(blocks)