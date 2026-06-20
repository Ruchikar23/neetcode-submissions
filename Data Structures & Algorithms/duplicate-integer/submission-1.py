class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_obj = set()
        for i in nums :
            if i in set_obj:
                return True
            set_obj.add(i)
        return False 