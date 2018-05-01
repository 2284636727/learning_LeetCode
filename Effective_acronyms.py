class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        from collections import Counter
        if Counter(s) != Counter(t):
            return False
        index1 = 0
        index2 = 0
        times = 0
        repeat = False
        l_s = len(s)
        l_t = len(t)
        while index1 < l_s and index2 < l_t:
            print(s[index1],t[index2])
            if s[index1] == t[index2]:
                index1 += 1
                index2 += 1
            elif repeat:
                times += 1
                if index1 > index2:
                    index2 += 1
                elif index1 < index2:
                    index1 += 1
                else:
                    return False
            elif s[index1+1] == t[index2]:
                index1 += 1
                repeat = True
            elif s[index1] == t[index2+1]:
                index2 += 1
                repeat = True
            else:
                return False
            print('repeat:',repeat)
            print('times:',times)
        if times > 1:
            return False
        return True

s = "abdc"
t = "dbac"

print(Solution().isAnagram(s,t))