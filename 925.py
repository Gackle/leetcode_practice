# coding: utf-8
""" 925. 长按键入

你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。


示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

思路：双指针，遍历 name 和 typed，理论上来说，如果符合条件的话，应该是两者都能遍历完（不管两者长度是否一样），否则就一定不符合条件。
其次，如果 name 中的某个字符，在 typed 对应位置及其以后位置都无法找到相同字符，也可以提前报告不符合
"""


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # name 的指针
        ni = 0
        # typed 的指针
        ti = 0
        while ni < len(name) and ti < len(typed):
            if name[ni] != typed[ti]:
                while 0 < ti < len(typed) and typed[ti-1] == typed[ti]:
                    ti += 1
                if ti == len(typed) or name[ni] != typed[ti]:
                    return False
            ni += 1
            ti += 1
        return True if ni == len(name) else False


if __name__ == "__main__":
    s = Solution()
    # name = "pyplrz"
    # typed = "ppyypllr"
    name = "kikcxmvzi"
    typed = "kiikcxxmmvvzz"
    print(s.isLongPressedName(name, typed))
