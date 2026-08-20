class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen={}
       for x,j in enumerate(nums):
        sub= target-j
        if sub in seen:
            return [seen[sub],x]
        seen[j]=x