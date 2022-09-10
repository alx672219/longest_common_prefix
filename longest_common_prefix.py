from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        strs.sort()   # because of this, I only need to check the first and last one.
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix +=x
            else: 
                break
        return prefix