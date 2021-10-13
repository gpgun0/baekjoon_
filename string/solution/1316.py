class Solution:
    def main(self, word: str) -> int:
        char_check_list = [0] * 26

        char_check_list[ord(word[0]) - 97] = 1
        for i in range(1, len(word)):
            if char_check_list[ord(word[i]) - 97] and word[i-1] != word[i]:
                return 0
            char_check_list[ord(word[i]) - 97] = 1
        
        return 1
        
sol = Solution()
cnt = 0
n = int(input())
for _ in range(n):
    word = input()
    cnt += sol.main(word)
print(cnt)