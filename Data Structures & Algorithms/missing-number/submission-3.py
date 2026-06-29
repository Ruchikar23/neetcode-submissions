class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res= int(n*(n+1)/2)
        sum_ = 0
        for i in nums :
            sum_ += i 
        miss_num = res - sum_
        return miss_num