class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        for x in range(len(strs)):
            if sorted(strs[x])==sorted(strs[x+1]):
                result.append([strs[x],strs[x+1]])
            else:
                result.append([strs[x]])
        return result

        