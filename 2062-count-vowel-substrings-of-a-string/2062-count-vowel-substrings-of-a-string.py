class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count: int = 0 
        vowel: set[str] = {"a","e","i","o","u"}
        for i in range(len(word)):
            substring: set = set()
            if word[i] not in vowel:
                continue
            substring.add(word[i])
            for j in word[i:]:
                if j not in vowel:
                    break
                else:
                    substring.add(j)
                    if len(substring) == 5:
                        count+= 1
        return count