import sys
input = sys.stdin.readline
class Solution:
    def main(self):
        n = int(input())
        d = []
        for _ in range(n):
            cmd = input().split()

            if cmd[0] == 'push_front':
                d.insert(0, cmd[1])
            elif cmd[0] == 'push_back':
                d.append(cmd[1])
            elif cmd[0] == 'pop_front':
                if not len(d):
                    print(-1)
                    continue
                print(d.pop(0))
            elif cmd[0] == 'pop_back':
                if not len(d):
                    print(-1)
                    continue
                print(d.pop())
            elif cmd[0] == 'size':
                print(len(d))
            elif cmd[0] == 'empty':
                if not len(d):
                    print(1)
                else:
                    print(0)
            elif cmd[0] == 'front':
                if not len(d):
                    print(-1)
                    continue
                print(d[0])
            elif cmd[0] == 'back':
                if not len(d):
                    print(-1)
                    continue
                print(d[-1])            

sol = Solution()
sol.main()