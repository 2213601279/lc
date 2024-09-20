"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false

说明: 你可以假设字符串只包含小写字母
"""

"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
import collections
from typing import List


class Soulution:
    def diff_strings(self, s: str, t: str):
        hash_s = collections.Counter(s)
        hash_t = collections.Counter(t)
        return hash_s == hash_t


class Soulution_with_list:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print(set(nums1))
        print(set(nums2))
        a = set(nums1) & set(nums2)
        print(a)
        return list(a)


# class HappyNums:
#     def judge_happy(self, nums: int):
#
#     def calculate_nums(self, a: int) -> int:
#         #         按位求平方和
#         sum_a = 0
#         set_a = set()
#         str_a = str(a)
#         for i in str_a:
#             sum_a += int(i) ** 2
#         if sum_a == 1:
#             return True
#         else:
#             str_a = sum_a


if __name__ == '__main__':
    s = "anagram"
    t = "nagarama"
    print(Soulution().diff_strings(s, t))
    print(Soulution_with_list().intersection(nums1=[1, 2, 3, 4, 2, 1, 2, 3]
                                             , nums2=[3, 99, 70]))
