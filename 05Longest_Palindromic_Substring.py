'''
input:"abacd";"cdddd"
output:"aba";"dddd"
'''

class Solution1:
    # brute_force
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        maxcount = 0
        r_b,r_e = 0,0
        for i in range(lens):
            for j in range(i,lens):
                b,e = i,j
                while e >= b:
                    print(s[b],s[e])
                    if s[b] == s[e]:
                        b,e = b+1,e-1
                        tmpcount = j-i
                    else:
                        break
                if e < b:
                    tmpcount = j-i+1
                print(tmpcount)
                if tmpcount > maxcount:
                    maxcount = tmpcount
                    r_b,r_e = i,j
        return s[r_b:r_e+1]

class Solution2:
    #  enumerate center of substring
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        reslen = 0
        r_b = 0
        r_e = 0
        if slen ==1 : return s
        for i in range(1,slen):
            tmplen = 0
            b,e = i-1,i
            while b >= 0 and e < slen:
                if s[b] == s[e]:
                    tmplen += 1
                    b = b-1
                    e = e+1
                else:
                    break
            if tmplen > reslen:
                reslen = tmplen
                r_b = b+1
                r_e = e
        return  s[r_b:r_e]

if __name__ == '__main__':
    sol = Solution2()
    print(sol.lengthOfLongestSubstring('abccba'))



