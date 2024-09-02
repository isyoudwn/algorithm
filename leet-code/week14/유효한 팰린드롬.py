class Solution:
    # convert all letters Upper to Lower
    # remove all non-alphanumeric characters -> remove all character which isn't number or alpha 
    # confirm the result phrase, having a same forward and backward(symmetry)
    # 200000 O(nlogn)

    def isPalindrome(self, s: str) -> bool:

        s.lower()
        s = s.lower().replace(' ', '')

        for st in s:
            if not st.isalnum():
                s = s.replace(st, '')
        
        N = len(s)

        if N <= 1:
            return True
        

        forward = ''
        backward = ''

        if N % 2 == 0:
            forward = s[:N//2]
            backward = s[N//2:]
        else :
            forward = s[:N//2]
            backward = s[N//2 + 1:]

        backward = backward[::-1]

        if forward == backward:
            return True
        return False