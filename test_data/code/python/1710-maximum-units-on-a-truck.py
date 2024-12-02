from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for numBoxes, numUnits in boxTypes:
            if truckSize >= numBoxes:
                totalUnits += numBoxes * numUnits
                truckSize -= numBoxes
            else:
                totalUnits += truckSize * numUnits
                truckSize = 0
                break
        return totalUnits