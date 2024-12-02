def add_binary(a: str, b: str) -> str:
    """
    Adds two binary strings and returns their sum as a binary string.
    
    Parameters:
    a (str): The first binary string.
    b (str): The second binary string.
    
    Returns:
    str: The sum of the two binary strings as a binary string.
    """
    return bin(int(a, 2) + int(b, 2))[2:]