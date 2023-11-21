class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        i = 0
        
        while carry:
            # Case 1 : if index in-bounds
            if i < len(digits):
                # Case 1a: if digits[i] is 9, then we keep the carry as is
                if digits[i] == 9:
                    digits[i] = 0
                # Case 1b: if digits[i] != 9, then carry = 0
                else :
                    digits[i] += 1
                    carry = 0
            
            # Case 2 : if index out of bounds
            else:
                digits.append(1)
                carry = 0
            
            i += 1
        
        return digits[::-1]