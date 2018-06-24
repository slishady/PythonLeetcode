class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False
        if " " in s:
            return False
        a = ['0', '1', '2' ,'3', '4', '5', '6', '7', '8', '9','.']
        cnt = 0
        for i in range(len(s)):
            if s[i] not in a:
                return False

            if s[i] == '.':
                cnt += 1
                if cnt == 2:
                    return False
                if len(s) == 1:
                    return False
                
        # if s.startswith("00"):
        #     return False


        return True

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            {},
            {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
            {'digit': 3, '.': 4},
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}
        ]
        
        cur_state = 1
        
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            if c not in state[cur_state].keys():
                return False
            cur_state = state[cur_state][c]
        
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True
        