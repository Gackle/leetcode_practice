# encoding: utf-8
"""1177. 构建回文串检测

给你一个字符串 s，请你对 s 的子串进行检测。
每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。我们可以 `重新排列` 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 
如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）
 

示例：
输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。
 

提示：
1 <= s.length, queries.length <= 10^5
0 <= queries[i][0] <= queries[i][1] < s.length
0 <= queries[i][2] <= s.length
s 中只有小写英文字母
"""
from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        """将 26 个英文字母，对应 26 个位来表示。比如字母 a 对应 1<<0, 字母 b 对应 1<<1 ，字母 c 对应 1<<2，以此类推。 这样可以将字符串 s 看成一个数组，然后统计数组的异或前缀和 count ，这样就可以统计每一个字母的奇偶性。
        遍历所有 queries，待检子串都可以表示为 [left,right,k]。利用异或前缀和数组，可以得到待检子串每一个字母的奇偶性。出现偶数次的字母，可以对称放在字符串两侧，构成回文串，剩下的出现奇数次字母配对后，还会剩余，需要从中选择最多 k 项替换成任何小写英文字母。替换 k 次，可以保证使得长度最长为 2k+1 的字符串变成回文串。所以我们只需要判断，待检子串的为 1 数位，是否小于 2k+1 即可。
        """
        n = len(s)
        count = [0] * (n + 1)
        for i in range(n):
            count[i + 1] = count[i] ^ (1 << (ord(s[i]) - ord('a')))
        res = []
        for l, r, k in queries:
            bits = (count[r + 1] ^ count[l]).bit_count()
            res.append(bits <= k * 2 + 1)
        return res
    

if __name__ == '__main__':
    s = Solution()
    examples = [
        ({"s": "abcda", "queries": [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]}, [True,False,False,True,True])
    ]
    for row in examples:
        kwargs, ans = row
        res = s.canMakePaliQueries(**kwargs)
        assert res == ans, f"canMakePaliqueries({kwargs}) except {ans} but got {res}"
    print("You Pass!")