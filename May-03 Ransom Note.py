#Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set = set(ransomNote)
        for i in ransom_set:
            if(not (ransomNote.count(i) <= magazine.count(i))):
                return False
        return True