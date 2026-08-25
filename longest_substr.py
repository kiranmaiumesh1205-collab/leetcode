class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    res = ""
    max_len = 0

    for ch in s:
        if ch in res:
            res = res[res.index(ch) + 1:]

        res += ch
        max_len = max(max_len, len(res))

    return max_len
