class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Calculate total distance to find nearest multiple of destination - start
        total_distance = sum(distance)
        # First try going in the forward direction
        forward_distance = sum(distance[start:destination % len(distance) + 1])
        # Second try going in the backward direction
        backward_distance = total_distance - forward_distance
        # Return the smaller of the two distances
        return min(forward_distance, backward_distance)