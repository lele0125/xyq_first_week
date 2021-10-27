class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits=digits[::-1]
        # num=0
        # for i in range(len(digits)):
        #     num += 10**i*digits[i]
        # num +=1
        # 整数和字符串之间的转化
        # return [int(s) for s in str(num)]
        # 直接考虑最后一位的运算

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0: return digits
        # 考虑[9],[9,9]这种情况
        res = [0] * (len(digits) + 1)
        res[0] = 1
        return res
