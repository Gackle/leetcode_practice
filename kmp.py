# coding: utf-8
""" KMP 算法实现
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
    s = "asddsfesdbaddews"
    p = "ddew"
    print(kmp(s, p))
