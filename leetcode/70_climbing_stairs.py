## recursive soln is v simple but v slow
## recursive:

def climbingStairs(self, n):
    if n <= 3:
        return n

    return self.climbingStairs(n-1) + self.climbingStairs(n-2)


## complicated interative soln
## very fast!

def climbingStairs(self, n):
    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one = one + two
        two = one

    return one
