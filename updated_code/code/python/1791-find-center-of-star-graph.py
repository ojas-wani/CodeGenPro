from typing import List

class Solution:
    """
    This class finds the center of a star graph, which is a graph where there is one 
    center node and exactly n - 1 edges that connect the center node with every other node.
    
    Args:
    edges (List[List[int]]): A 2D integer array where each edges[i] = [ui, vi] indicates 
        that there is an edge between the nodes ui and vi.

    Returns:
    int: The center of the star graph.
    """
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        This function finds the center of the star graph by checking which node appears 
        in all edges.

        Args:
        edges (List[List[int]]): A 2D integer array where each edges[i] = [ui, vi] 
            indicates that there is an edge between the nodes ui and vi.

        Returns:
        int: The center of the star graph.
        """
        n = len(edges)
        for edge in edges:
            u, v = set(edge)
            if len(u) == 1:
                return u.pop()