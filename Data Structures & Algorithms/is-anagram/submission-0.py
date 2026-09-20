class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(t)):
            if t[i] in map:
                map[t[i]] += 1
            else:
                map[t[i]] =1

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] -= 1
            else:
                return False

        return all(value == 0 for value in map.values())

            
        