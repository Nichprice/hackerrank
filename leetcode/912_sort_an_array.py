## insertion sort
## solves it, but very slowly
## worst case O(n^2) best case O(n)

def sortArray(self, nums: List[int]) -> List[int]:

    for i in range(1, len(nums)):
        j = i - 1
        while j >=0 and nums[j + 1] < nums[j]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
            j -= 1

    return nums

## merge sort
## O(nlogn)
## really tricky to write

#pseudocode
def mergeSort(arr, s, e):
    ## If the current subarray is of size 1 or 0 - base case
    if e - s + 1 <= 1:
        return arr
    # Split the array into two equal halves
    m = (s + e)/2
    ## Keep splitting until base case is hit
    mergeSort(arr, s, m)
    mergeSort(arr, m + 1, e)
    ## Merge arrays once sorted

    def merge(arr, l, m, r):
        leftSubarray = m - l + 1
        rightSubarray = r - m
    
        i = 0 ## starting index for leftSubarray
        j = 0 ## starting index for rightSubarray
        k = l ## starting index of arr, the merged array
        
        ## Comparing both arrays to find the smaller value
        while i < leftSubarray.len and j < rightSubarray.len:
            if leftSubarray[i] <= rightSubarray[j]:
                arr[k] = leftSubarray[i]
                i += 1
            else:
                arr[k] = rightSubarray[j]
                j += 1
            k += 1

        ## Subarrays may not be split in equal length
        ## This will exhaust any items that are left in either
        while i < leftSubarray.len:
            arr[k] = leftSubarray[i]
            i += 1
            k += 1
        while j < rightSubarray.len:
            arr[k] = rightSubarray[j]
            j += 1
            k += 1

    merge(arr, s, m, e)

    ## Return the resulting array
    return arr

## actual code for quicksort
## O(nlogn)

def sortArray(self, nums: List[int]) -> List[int]:

        def helper(head, tail):
            if head >= tail: return 
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = nums[m]
            while r >= l:
                while r >= l and nums[l] < pivot: l += 1
                while r >= l and nums[r] > pivot: r -= 1
                if r >= l:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            helper(head, r)
            helper(l, tail)

        helper(0, len(nums)-1)
        return nums