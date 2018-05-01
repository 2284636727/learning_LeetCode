class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([i.lower() for i in s if i.isalpha()])
        index1 = int(len(s)/2) + len(s) % 2 -1
        index2 = int(len(s)/2)


s = 'aba'
index1 = int(len(s)/2) + len(s) % 2
index2 = int(len(s)/2) - 1

print(index1,index2)
print(s[:index1],s[:index2:-1])
print(s[:index1] == s[:index2:-1])