# -*- coding:utf-8 -*-
# Count the number of prime numbers less than a non-negative number, n.
#
# Hint:
#
# Let's start with a isPrime function.
# To determine if a number is prime,
# we need to check if it is not divisible by any number less than n.
# The runtime complexity of isPrime function would be O(n) and
# hence counting the total prime numbers up to n would be O(n2).
# Could we do better?


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    def countPrimes_227ms(self, n):
        # https://github.com/Lubndub/LeetCode/blob/master/CountPrimes.py
        if n < 3:
            return 0
        "Return all primes <= n."
        # np1 = n + 1
        s = [True] * n
        s[0] = s[1] = False
        sqrtn = int(round(n**0.5))
        for i in xrange(2, sqrtn + 1):
            if s[i]:
                s[i*i: n:i] = [False] * len(xrange(i*i, n, i))
        return s.count(True)


# https://leetcode.com/discuss/35939/fast-python-solution
s = Solution()
print s.countPrimes(0)
print s.countPrimes(2)
print s.countPrimes(3)
print s.countPrimes(10000)
print s.countPrimes(499979)

# 解题方法就在第二个提示埃拉托斯特尼筛法Sieve of Eratosthenes中，
# 这个算法的过程如下图所示，我们从2开始遍历到根号n，先找到第一个质数2，
# 然后将其所有的倍数全部标记出来，然后到下一个质数3，标记其所有倍数，
# 一次类推，直到根号n，此时数组中未被标记的数字就是质数。
