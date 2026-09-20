class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for string in strs:
            new = ""
            for i in range(min(len(string), len(longest))):
                if string[i] == longest[i]:
                    new += string[i]
                else:
                    break
            if len(new) < len(longest):
                longest = new
        return new            



        