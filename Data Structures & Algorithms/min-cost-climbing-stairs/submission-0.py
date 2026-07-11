class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_ahead = 0
        two_ahead = 0

        for i in range(len(cost) - 1, -1, -1):
            current = cost[i] + min(one_ahead, two_ahead)
            two_ahead = one_ahead
            one_ahead = current

        return min(one_ahead, two_ahead)