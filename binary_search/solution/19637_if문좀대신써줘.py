import sys
input = sys.stdin.readline

class Solution:
    def main(self):
        n, m = map(int, input().split())
        title = ['x']
        rang = [0]

        prev = ""
        for _ in range(n):
            title_, range_ = input().split()
            if range_ == prev:
                continue
            title.append(title_)
            rang.append(int(range_))

            prev = range_

        for _ in range(m):
            str_ = int(input())

            if str_ == 0:
                print(title[1])
                continue
            l, h = 0, len(title)-1

            while l <= h:
                mid = (l+h) // 2
                
                if str_ <= rang[mid]:
                    if str_ <= rang[mid-1]:
                        h = mid - 1
                    else:
                        print(title[mid])
                        break
                elif str_ > rang[mid]:
                    if str_ > rang[mid+1]:
                        l = mid + 1
                    else:
                        print(title[mid+1])
                        break



sol = Solution()
sol.main()