class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numlen = len(str(num))
        number = list(str(num))
        for i in range(4-numlen):
            number = [0] + number
        number = list(map(int, number))
        result = ""
        if number[0] != 0:
            result += 'M'*number[0]
        if number[1] != 0:
            if number[1] == 4:
                result += 'CD'
            elif number[1] == 9:
                result += 'CM'
            elif number[1] < 5:
                result += 'C' * number[1]
            else:
                result += ('D' + "C"*(number[1] - 5))
        if number[2] != 0:
            if number[2] == 4:
                result += 'XL'
            elif number[2] == 9:
                result += 'XC'
            elif number[2] < 5:
                result += 'X'*number[2]
            else:
                result += ('L' + 'X'*(number[2]-5))
        if number[3] != 0:
            if number[3] == 4:
                result += 'IV'
            elif number[3] == 9:
                result += 'IX'
            elif number[3] < 5:
                result += 'I'*number[3]
            else:
                result += ('V'+'I'*(number[3]- 5)) 

        return result

a = Solution()
print(a.intToRoman(3))
print(a.intToRoman(4))
print(a.intToRoman(9))
print(a.intToRoman(58))
print(a.intToRoman(1994))
