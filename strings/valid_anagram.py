class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        count={}
        dic={}
        for char in s:
            count[char]=count.get(char,0)+1
        for char in t:
            dic[char]=dic.get(char,0)+1
        return count == dic