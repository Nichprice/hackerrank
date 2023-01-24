## recusively

## i think there is amuch quicker way of doing this, but recursion is cool and for smart people

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)