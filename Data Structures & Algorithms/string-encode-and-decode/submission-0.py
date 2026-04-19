class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            sz = len(s)
            code += str(sz) + "#" + s
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i < len(s):
            # read digits until '#'
            j = i
            while s[j].isdigit():
                j += 1
            sz = int(s[i:j])
            # read string with len=sz
            j = j + 1
            i = j + sz
            decode.append(s[j: i])

        return decode


