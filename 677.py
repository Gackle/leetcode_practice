# coding: utf-8
''' 677. 键值映射

实现一个 MapSum 类里的两个方法，insert 和 sum。

对于方法 insert，你将得到一对（字符串，整数）的键值对。字符串表示键，整数表示值。如果键已经存在，那么原来的键值对将被替代成新的键值对。

对于方法 sum，你将得到一个表示前缀的字符串，你需要返回所有以该前缀开头的键的值的总和。
'''


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_list = dict()
        self.trie = Trie(None)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key not in self.index_list:
            self.index_list[key] = val
        else:
            temp = val
            val = val - self.index_list[key]
            self.index_list[key] = temp

        current = self.trie
        for c in key:
            if c not in current.tree:
                current.tree[c] = Trie(val)
            else:
                current.tree[c].val += val
            current = current.tree[c]

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current = self.trie
        for c in prefix:
            if c not in current.tree.keys():
                return 0
            else:
                current = current.tree[c]

        return current.val


class Trie:
    def __init__(self, val):
        self.val = val if val is not None else 0
        self.tree = dict()


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


if __name__ == '__main__':
    pass
