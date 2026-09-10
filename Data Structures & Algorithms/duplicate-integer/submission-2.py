class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyThere = []
        for i in nums:
            if i in alreadyThere:
                return True
            alreadyThere.append(i)
        return False
            
        