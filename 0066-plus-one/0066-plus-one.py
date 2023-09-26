class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        i = 0
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    i += 1
                else:
                    carry = 0
                    digits[i] += 1
            else:
                carry = 0
                digits.append(1)
        
        return digits[::-1]