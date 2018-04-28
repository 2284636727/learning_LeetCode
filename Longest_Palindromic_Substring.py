'''
input:"babad";"cbbd"
output:"aba"or"bab";"bb"
'''

class Solution:
    # brute_force
    def longestPalindrome1(self, s):
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

    # brute_force_opti
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        pass
    # manacher
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pass
        
sol = Solution()
print(sol.longestPalindrome1("cbbd"))