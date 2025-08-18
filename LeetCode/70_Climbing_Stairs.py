class Solution(object):
    @staticmethod
    def nCr(n, r):
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        total_ways = 0
        for y in range(n // 2 + 1):
            x = n - 2*y
            total_ways += Solution.nCr(x + y, y)
        return total_ways


"""
dont need to create a list of all combinations, just count the number of ways to climb the stairs.
ncr(n, r) is used to calculate the number of combinations of n items taken r at a time.
 in our case, n is the total number of steps and r is the number of 2-steps taken.
the formula for combinations is n! / (r! * (n - r)!)
"""