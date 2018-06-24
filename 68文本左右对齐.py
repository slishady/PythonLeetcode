class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #储存答案
        ans_list = []
        #用来切割words的指针
        i = 0
        
        while i < len(words):
            beigin = i
            wordsum = 0
            leastspace = 0
            end = i
            oneresult = ""
            while end < len(words) and len(words[end]) + wordsum + leastspace <= maxWidth:
                leastspace += 1
                wordsum += len(words[end])
                end += 1
            leastspace -= 1
            oneresult = ""
            if end == len(words):
                for i in words[beigin:end]:
                    oneresult += i
                    if leastspace != 0:
                        oneresult += " "
                        leastspace -= 1
                ans_list.append(oneresult)
                break
                        
            realsum = 0 
            for j in words[beigin:end]:
                realsum += len(j)
            left_space = maxWidth - realsum
            if leastspace != 0:
                eachspace = left_space // (leastspace)
                left_space2 = left_space - eachspace*leastspace
            else:
                oneresult += words[beigin] + left_space*" "
                ans_list.append(oneresult)
                i = end
                continue
            oneresult = ""
            for j in words[beigin:end]:
                oneresult += j 
                if leastspace > 0:
                    oneresult += eachspace*" "
                    leastspace -= 1
                    if left_space2 > 0:
                        oneresult += " "
                        left_space2 -= 1

            ans_list.append(oneresult)
            i = end
        if len(ans_list[-1]) < maxWidth:
            ans_list[-1] += " "*(maxWidth-len(ans_list[-1]))
        return ans_list


a = Solution()
print(a.fullJustify(["What","must","be","acknowledgment","shall","be"],
maxWidth = 16))
                    
                    
                

                

