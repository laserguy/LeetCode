class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0
        div, rem = n//7, n%7

        for i in range(div):
          val = 28 + i*7
          count += val

        for i in range(1,rem+1):
          count += i + div

        return count