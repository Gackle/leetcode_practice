# coding: utf-8
""" KMP 算法实现
- 首先列出模式串 P 的所有子串，求得每一个子串的所有前缀和后缀，然后计算 **各个子串** 的前缀后缀的最长共有元素的长度，得到一个 **部分匹配表** 。
- 根据 `部分匹配表` 去求 `next` 数组：<u> `next` 数组相当于“最长共有元素长度值”整体向右移动 1 位，然后初始值赋为 -1 </u>。
- 假设现在文本串 S 匹配到 `i` 位置，模式串 P 匹配到 `j` 位置
如果 `j = -1`，或者当前字符匹配成功（即 `S[i] == P[j]` ），都令 `i++`，`j++`，继续匹配下一个字符；
- 如果 `j != -1`，且当前字符匹配失败（即 `S[i] != P[j]` ），则令 `i` 不变，`j = next[j]`。此举意味着失配时，模式串 P 相对于文本串 S 向右移动了 `j - next [j]`  位
- 换言之，将模式串 P 失配位置的 `next` 数组的值对应的模式串 P 的索引位置移动到失配处
"""


def kmp(s, p):
    sl = len(s)
    pl = len(p)
    i = 0
    j = 0
    next = get_next(p)
    while i < sl and j < pl:
        if s[i] == p[j] or j == 0:
            i += 1
            j += 1
        else:
            j = next[j]
    return True if j == pl else False


def get_next(p):
    next = [0] * len(p)
    next[0] = -1    # 对于首字母其 next 的值为 -1
    k = -1  # 初始值，k 为前缀和后缀匹配的长度
    i = 0
    while i < (len(p) - 1):
        if k == -1 or p[k] == p[i]:
            k += 1
            i += 1
            next[i] = k
        else:
            k = next[k]  # 回溯
    return next


if __name__ == "__main__":
    s = "wefsdfadbdsab2df"
    p = "abaac"
    print(kmp(s, p))
