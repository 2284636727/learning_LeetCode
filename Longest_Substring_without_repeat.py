'''
input:"aaasceqsa","au","abcaaa"
ouput:"asceq,5","au,2","abc,3"
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
        return (result,reslen)

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("aaasceqsa"))
    print(sol.lengthOfLongestSubstring("au"))
    print(sol.lengthOfLongestSubstring("abcaaa"))
    

# GOD SOLUTION
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        ret = 0
        pointer = 0
        start = 0
        latest_char = {}
        while pointer < length:
            cur_char = s[pointer]
            if cur_char in latest_char and latest_char[cur_char] >= start:
                start = latest_char[cur_char] + 1
            elif pointer - start + 1 > ret:
                ret = pointer - start + 1
            
            latest_char[cur_char] = pointer
            pointer = pointer + 1
        return ret




