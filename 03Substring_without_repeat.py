'''
input:'abcabcbb';'bbbbbb';'pwwkew'
output:'3';'1';'3'
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        tmplen = 0
        result = ''
        reslen = 0
        for i in range(len(s)):
            lin = s[i:]
            for j in lin:
                if j not in tmp:
                    tmp += j
                else:
                    break
            tmplen = len(tmp)
            if tmplen > reslen:
                reslen = tmplen
                result = tmp
            tmp = ''
            tmplen = 0
        return reslen
    
print(Solution().lengthOfLongestSubstring('aab'))



