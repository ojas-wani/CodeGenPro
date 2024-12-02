class PascalTriangle:
    """Class to generate Pascal's triangle.
    
    Args:
    numRows (int): The number of rows to generate.
    
    Returns:
    list[list[int]]: The generated Pascal's triangle.
    """
    
    def __init__(self):
        pass
    
    def generate(self, num_rows: int) -> list[list[int]]:
        """Generate the first num_rows of Pascal's triangle.
        
        Args:
        num_rows (int): The number of rows to generate.
        
        Returns:
        list[list[int]]: The generated Pascal's triangle.
        """
        triangle = [[1 for _ in range(i+1)] for i in range(num_rows)]
        for i in range(2, num_rows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle

if __name__ == "__main__":
    solution = PascalTriangle()
    result = solution.generate(num_rows=5)
    print(result)