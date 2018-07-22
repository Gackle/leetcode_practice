# coding: utf-8
''' 22. 括号生成
'''


class Solution:
    '''
    '''

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(n, left, right, gen_str, gen_list):
            '''
            :type left: int
            :type right: int
            :type gen_str: str
            :type gen_list: List[str]
            '''
            if (left + right) == n * 2:
                gen_list.append(gen_str)
                return
            if left < n:
                gen(n, left + 1, right, gen_str + "(", gen_list)
                if right < left:
                    gen(n, left, right + 1, gen_str + ")", gen_list)
            else:
                gen(n, left, right + 1, gen_str + ")", gen_list)

        gen_list = []
        gen(n, 0, 0, "", gen_list)
        return gen_list


class Solution2:
    ''' 剪枝法
    '''

    def generateParenthesis(self, n):
        max_num = 2**(2 * n - 1)
        for num in range(max_num):
            current = bin(num)[2:].rjust(2 * n, '0')
        pass
        # 时间复杂度难以接受，最起码大于 O(2**n)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
