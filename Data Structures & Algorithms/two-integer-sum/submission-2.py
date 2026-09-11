class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for x,j in enumerate(nums):
            sub=target-j
            if sub in map:
                return [map[sub],x]
            map[j]=x
        return None