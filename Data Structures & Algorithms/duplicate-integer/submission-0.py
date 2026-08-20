class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listt=[]
        state= False
        for x in nums:
            if x not in listt:
                listt.append(x)
                state=False
            else:
                listt.append(x)
                state=True
        return state