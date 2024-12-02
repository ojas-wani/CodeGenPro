class TimeSolver:
    """
    Solve the issue of replacing hidden digits in a given time string to get the latest valid time.
    """

    def solve(self, time: str) -> str:
        """
        This function takes a time string as input, replace the hidden digits with their maximum possible values, 
        and return the latest valid time.
        
        Args:
        time (str): A time string in the format 'hh:mm' with some digits replaced by '?'.
        
        Returns:
        str: The latest valid time string by replacing the hidden digits.
        """
        
        res = list(time)
        if res[0] == '?':
            res[0] = '2'
        if res[1] == '?':
            res[1] = '3'
        if res[3] == '?':
            res[3] = '5' if res[0] == '2' else '9'
        if res[4] == '?':
            res[4] = '0' if res[0] == '2' else '9'
        return ''.join(res)


# add a newline character at the end of the file