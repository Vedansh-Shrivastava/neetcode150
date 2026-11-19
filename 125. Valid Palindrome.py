class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s))
        st = st.lower()
        # for i in range(len(st) // 2):
        #     if st[i] != st[len(st) - 1 - i]:
        #         return False
            
        return st == st[::-1]
