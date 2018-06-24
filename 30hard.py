class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        if len(s) == 0:
            return []
        self.length = len(words[0])
        ans_list = []
        pos_list = []
        startpos = -1
        words.sort()
        while startpos < len(s):
            startpos += 1
            jet = 1
            pos_list = []
            for i in range(len(words)):
                if i > 0 and words[i] == words[i-1]:
                    newpos = pos_list[-1] + self.length
                    pos_list.append(s.find(words[i], newpos))
                else:
                    pos_list.append(s.find(words[i], startpos))
            pos_list.sort()
            if -1 in pos_list:
                break
            else:
                pos = 0
                while pos < len(pos_list)-1:
                    if pos_list[pos] + self.length != pos_list[pos+1]:
                        jet = 0
                        # if pos_list[pos] != 0:
                        #     if pos == 0:
                        #         startpos = pos_list[pos]+1
                        #     else:
                        #         startpos = pos_list[pos]
                        #         g = s[pos_list[pos]: pos_list[pos]+self.length]
                        # else:
                        #     startpos = 1
                        break
                    pos += 1
            if jet == 0:
                pass
            else:
                ans_list.append(pos_list[0])
                

        return list(set(ans_list))

class Solution:
    def split(self,string,width):#将一个字符串string按着width的宽度切开放在一个列表中，返回这个列表。
        result = []
        i = 0
        length = len(string)
        while i<=length-width:
            result.append(string[i:i+width])
            i = i+width
        return result
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        words_count = len(words)
        if words_count>0:#判断输入的s和words是否为空，如果不为空，将words中的单词的宽度放在length_word中
            length_word = len(words[0])
        else:
            length_word = 0
        i= 0
        length_s = len(s)
        if length_s == 0 or words_count == 0:#如果s为空或者words为空，返回空的列表
            return []
        while i <= length_s-length_word*words_count:#利用while循环，实现对s遍历
            string_list = self.split(s[i:i+length_word*words_count],length_word)#将s从i开始切分出一个长度和words中所有单词加在一起长度相同的一个子串，并将这个子串切开，放在string_list中
            string_list.sort()#由于words中的单词并不是排好序的，所以这里需要调用两个sort函数，将这两个列表排序，这样才能够判断他们是否相等。
            words.sort()
            if  string_list == words:#如果不是排好序的列表，即使里面的元素都相等，但是顺序不等的话，也是不会相等的。
                result.append(i)
            i = i + 1
        return result


s = "barfoofoobarthefoobarman"
a = Solution()
words = ["foo", "bar", "the"]
b = "wordgoodgoodgoodbestword"
c = ["word","good","best","good"]
d = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
e = ["fooo","barr","wing","ding","wing"]
f = "barfoothefoobarman"
g = ["foo","bar"]
h = "wordgoodstudentgoodword"
i = ["word","student"]
j = "ababaab"
k = ["ab","ba","ba"]
print(a.findSubstring(j, k))