class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for s_i in s:
            count_s[s_i] = count_s.get(s_i, 0) + 1
        for t_i in t:
            count_t[t_i] = count_t.get(t_i, 0) + 1

        return count_s == count_t
        