class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr=0
        temp=[]
        ans=[]
        res=[]
        for i in range(len(words)):
            word_len=len(words[i])
            if curr+word_len+len(temp)<=maxWidth:
                temp.append(words[i])
                curr+=word_len
            else:
                ans.append(temp)
                temp=[words[i]]
                curr=word_len
        if temp:
            ans.append(temp)
        for idx,line_words in enumerate(ans):
            if idx==len(ans)-1:
                line=" ".join(line_words)
                line+=" " *(maxWidth - len(line))
            elif len(line_words)==1:
                line=line_words[0]+" "*(maxWidth-len(line_words[0]))
            else:
                total_spaces=maxWidth-sum(len(word) for word in line_words)
                gaps=len(line_words)-1
                even_space=total_spaces//gaps
                extra=total_spaces%gaps
                line=""
                for i in range(gaps):
                    line+=line_words[i]
                    line+=" "*(even_space+(1 if i<extra else 0))
                line+=line_words[-1]
            res.append(line)
        return res