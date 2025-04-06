from typing import List


# Sieve of Eratosthenes & Sorting
class Solution:
    def getPrimes(self, limit: int) -> List[int]:
        isPrime = [True] * (limit + 1)
        primes = []
        
        for num in range(2, limit + 1):
            if isPrime[num]:
                primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    isPrime[multiple] = False
        
        return primes

    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        primeScores = [0] * n
        maxElement = max(nums)
        primes = self.getPrimes(maxElement)
        
        # Tính prime score cho từng phần tử
        for i in range(n):
            num = nums[i]
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    primeScores[i] += 1
                    while num % prime == 0:
                        num //= prime
            if num > 1:
                primeScores[i] += 1
        
        # Tìm chỉ mục của phần tử lớn hơn gần nhất ở hai bên
        nextDominant = [n] * n
        prevDominant = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and primeScores[stack[-1]] < primeScores[i]:
                topIndex = stack.pop()
                nextDominant[topIndex] = i
            if stack:
                prevDominant[i] = stack[-1]
            stack.append(i)
        
        # Đếm số lượng dãy con mà nums[i] là phần tử lớn nhất
        numOfSubarrays = [0] * n
        # (nextDominant[i] - i): Số lượng phần tử bên phải mà nums[i] là phần tử lớn nhất
        # (i - prevDominant[i]): Số lượng phần tử bên trái mà nums[i] là phần tử lớn nhất
        for i in range(n):
            numOfSubarrays[i] = (nextDominant[i] - i) * (i - prevDominant[i])
        
        # Sắp xếp theo giá trị giảm dần
        sortedArray = sorted([(nums[i], i) for i in range(n)], reverse=True)
        score = 1
        processingIndex = 0
        
        # Tính điểm tối đa
        while k > 0:
            num, index = sortedArray[processingIndex]
            processingIndex += 1
            operations = min(k, numOfSubarrays[index]) # Lấy số lượng phép nhân tối đa có thể thực hiện với phần tử này
            score = (score * pow(num, operations, MOD)) % MOD
            k -= operations
        
        return score
