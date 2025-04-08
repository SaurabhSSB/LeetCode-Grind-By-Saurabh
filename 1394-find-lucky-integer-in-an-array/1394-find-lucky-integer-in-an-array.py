class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky: int = -1
        dict_1: dict = {}
        for i in arr:
            if i in dict_1:
                dict_1[i]+= 1
            else:
                dict_1.update({i: 1})
        for j in dict_1:
            if j == dict_1[j]:
                if j > lucky:
                    lucky= j
        return lucky
