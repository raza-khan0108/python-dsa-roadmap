class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        for i in word:
            if i in 'aeiou':
                count += 1
        return count    
    
print(Solution().countVowels("abcde"))
        
    