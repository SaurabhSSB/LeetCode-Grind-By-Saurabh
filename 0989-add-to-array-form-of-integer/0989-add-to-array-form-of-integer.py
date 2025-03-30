class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        i = len(num) - 1
        
        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                num[i] = carry % 10
            else:
                num.insert(0, carry % 10)
            carry //= 10
            i -= 1
        
        return num