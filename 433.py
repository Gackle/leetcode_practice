# encoding: utf-8
"""433. 最小基因变化
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）
给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
 

示例 1：
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1

示例 2：
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2

示例 3：
输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
输出：3
 

提示：
start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
"""
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """ 广度优先遍历 BFS 哈希表 字符串
        看错标签用了 DFS ……
        """
        if endGene not in bank:
            return -1
        
        def dfs(curGene: str, waitBank: List[str]) -> int:
            if curGene == endGene:
                return 0
            if len(waitBank) == 0:
                return -1
            steps = []
            for index, gene in enumerate(waitBank):
                if sum([1 if i != j else 0 for i, j in zip(curGene, gene)]) != 1:  # 不符合突变 P.S. 比较这部分可以优化加速
                    continue
                step = dfs(gene, waitBank[:index] + waitBank[index+1:])
                if step >= 0:
                    steps.append(step)
                
            return 1+ min(steps) if len(steps) > 0 else -1
        
        return dfs(startGene, bank)


    def minMutationOffice(self, startGene: str, endGene: str, bank: List[str]) -> int:
        from collections import deque
        if startGene == endGene:
            return 0
        bank = set(bank)
        if endGene not in bank:
            return -1
        q = deque([(startGene, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == endGene:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
    
if __name__ == '__main__':
    s = Solution()
    examples = [
        ({"startGene": "AACCGGTT", "endGene": "AACCGGTA", "bank": ["AACCGGTA"]}, 1),
        ({"startGene": "AACCGGTT", "endGene": "AAACGGTA", "bank": ["AACCGGTA","AACCGCTA","AAACGGTA"]}, 2),
        ({"startGene": "AAAAACCC", "endGene": "AACCCCCC", "bank": ["AAAACCCC","AAACCCCC","AACCCCCC"]}, 3),
        ({"startGene": "AAAACCCC", "endGene": "CCCCCCCC", "bank": ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]}, 4)
    ]

    for row in examples:
        kwargs, ans = row
        res = s.minMutationOffice(**kwargs)
        assert res == ans, f"minMutation({kwargs}) except {ans} but got {res}"

    print("You Pass!")