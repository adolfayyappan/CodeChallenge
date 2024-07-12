class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        m = n
        if n < 0:
            n = n * -1

        y = x
        for i in range(1, n):
            y = y * x

        if m < 0:
            return 1 / y
        else:
            return y


ob = Solution()
print(ob.myPow(0.00001, 2147483647))
