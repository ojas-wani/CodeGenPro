Python
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = set()
        start = set()
        for p in paths:
            start.add(p[0])
            dest.add(p[1])
        return list(dest - start)[0]