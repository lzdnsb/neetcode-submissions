class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter_s = Counter(s)
        counter_t = Counter(t)
        for k, v in counter_s.items():
            if k in counter_t and v == counter_t[k]:
                continue
            return False
        return True
