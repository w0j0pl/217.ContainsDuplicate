class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = ""
        que = ""

        for i in s :
            if i not in que:
                que += i

            else:
                que = que[que.index(i)+1:]
                que += i

            if len(que) > len(best):
                best = que   
                             
        return len(best)