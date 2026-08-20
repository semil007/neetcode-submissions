class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub={}
        for x,j in enumerate(nums):
            comp=target-j
            if comp in sub:
                return [sub[comp],x]
            else:
                sub[j]=x