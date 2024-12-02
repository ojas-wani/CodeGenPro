from typing import List

class Solution:
    """
    Module that solves the problem of finding the earliest year with the maximum population.
    """
    
    def maximum_population(self, logs: List[List[int]]) -> int:
        """
        Function to find the earliest year with the maximum population.

        Args:
        logs (List[List[int]]): A 2D integer array where each log represents the birth and death years of a person.

        Returns:
        int: The earliest year with the maximum population.
        """
        
        births = [(log[0], i) for i, log in enumerate(logs)]
        deaths = [(log[1], i) for i, log in enumerate(logs)]
        
        births.sort()
        deaths.sort()
        
        population = {}
        alive = set()
        for death, i in deaths:
            population[death] = population.get(death, 0) - 1
            alive.discard(i)
        for birth, i in births:
            population[birth] = population.get(birth, 0) + 1
            alive.add(i)
        
        max_pop = 0
        earliest_year = 0
        for year, count in population.items():
            if count > max_pop:
                max_pop = count
                earliest_year = year
        return earliest_year