class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        N = len(s) # 4 // 0, 1, 2, 3
        n = N//2 # 0, 1
        
        for idx in range(0, n):
            s[idx], s[(N-1) - idx] = s[(N-1) - idx], s[idx]

            

        