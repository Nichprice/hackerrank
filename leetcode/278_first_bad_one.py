    def firstBadVersion(self, n: int) -> int:

        lo = 0
        hi = n + 1

        while lo <= hi:
            mid = (hi + lo)//2

            if isBadVersion(mid) == True:
                if isBadVersion(mid - 1) == False:
                    return mid
                else:
                    hi = mid - 1
            elif isBadVersion(mid) == False:
                if isBadVersion(mid + 1) == True:
                    return mid + 1
                else:
                    lo = mid + 1