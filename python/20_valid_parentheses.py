class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in dic.values():
                stack.append(c)
            else:
                if (not stack) or (dic[c] != stack.pop()):
                    return False
        if not stack:
            return True
        else:
            return False
        