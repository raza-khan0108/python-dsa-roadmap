class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("IBMCIC")
            elif i % 3 == 0:
                res.append("IBM")
            elif i % 5 == 0:
                res.append("CIC")
            else:
                res.append(str(i))
        return res
            
print(Solution().fizzBuzz(15))
