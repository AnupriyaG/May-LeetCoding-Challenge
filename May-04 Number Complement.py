class Solution:
    def findComplement(self, num):
        temp, bit = num, 1
        while temp:
            # flip current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            temp = temp >> 1
        return num
        