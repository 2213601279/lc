class Solution:
    def combine(self, n: int, k: int):
        """

        Args:
            n:
            k:

        Returns:

        """
        # 结果集合
        result = []
        self.back_trace(n, k, result, [], 1)
        return result

    def back_trace(self, n: int, k: int, result: [], path: [], start_index: int):
        if len(path) == k:
            # 浅拷贝赋值，相当于new 一个list
            result.append(path[:])
            return result
        for i in range(start_index, n + 1):
            path.append(i)
            self.back_trace(n=n, k=k, result=result, path=path, start_index=i)
            path.pop()
