from typing import List

class OrderedStream:

    def __init__(self, n: int):
        """
        Initiates an n-capacity stream to store strings in an ordered manner.
    
        Args:
            n (int): The maximum capacity of the stream.
        """
        self.n = n
        self.stream = [""] * (n + 1)

    def insert(self, idKey: int, value: str) -> List[str]:
        """
        Inserts a string into the stream and returns the largest possible chunk 
        of currently inserted values that appear next in the order.
        
        Args:
            idKey (int): The ID key of the string to be inserted.
            value (str): The string to be inserted.
        
        Returns:
            List[str]: The largest possible chunk of currently inserted values 
            that appear next in the order.
        """
        result = []
        while idKey <= self.n and self.stream[idKey] != "":
            result.append(self.stream[idKey])
            idKey += 1
        self.stream[idKey - 1] = value
        return result