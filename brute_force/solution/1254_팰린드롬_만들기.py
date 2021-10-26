class Solution:
  def main(self):
    str_ = input()
    len_ = len(str_)

    for i in range(len_):
      if str_[i:] == str_[i:][::-1]:
        return len_ + i

sol = Solution()
print(sol.main())