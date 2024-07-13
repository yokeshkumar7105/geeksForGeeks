class Solution:
    def reverseWords(self, s):
        # code here
        li = s.split(".")
        
        s1 = ""
        
        for i in range(len(li)):
            li[i] = li[i][::-1]
        s1 = ".".join(li)
        return s1
