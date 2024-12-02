from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        Given the array `paths`, where `paths[i] = [cityAi, cityBi]` means there exists a direct path going from `cityAi` to `cityBi`. 
        Return the destination city, that is, the city without any path outgoing to another city.

        :param paths: The array of paths
        :return: The destination city
        """
        start = set()
        dest = set()
        for p in paths:
            start.add(p[0])
            dest.add(p[1])
        return list(dest - start)[0]