#求前缀
from typing import List

def compare(a,b):
    n=[]
    for i in range(len(a)) if len(a)<=len(b) else range(len(b)):
        if a[i]==b[i]:
            n.append(a[i])
        else:
            return n
    return n

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs!=[]:
            same=strs[0]
        else:
            return ''
        for i in range(1,len(strs)) :
            same=compare(same,strs[i])
        return  ''.join(same)
a=Solution()
print(a.longestCommonPrefix(['flower','flow','flight']))