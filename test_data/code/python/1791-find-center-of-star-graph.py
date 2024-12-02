class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for edge in edges:
            if edge[0] in edges or edge[1] in edges:
                return edge[0]