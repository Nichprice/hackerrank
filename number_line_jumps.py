#add x1 and x2 to arrays [first] and [seceond]
#for n in range 0 to infinity
#  
#for a range of 1 to infinity, multiply n times the v, add to the x, add to the array
#if the array[n] of first > array[n] of second and array[n+1] of first 


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    arrA = []
    arrB = []
    arrA.append(x1)
    arrB.append(x2)
    keepgoing = True
    answer = ""
    n = 0
    if x1 > x2 and v1 > v2:
        answer = "NO"
    elif x2 > x1 and v2 > v1:
        answer = "NO"
    elif v1 == v2:
        answer = "NO"
    else:
        while keepgoing:
            if arrA[n] != arrB[n]:
                n += 1
                arrA.append(x1 + v1 * n)
                arrB.append(x2 + v2 * n)
                if arrA[n-1] > arrB[n-1]:
                    if arrA[n] < arrB[n]:
                        answer = "NO"
                        keepgoing = False
                elif arrA[n-1] < arrB[n-1]:
                    if arrA[n] > arrB[n]:
                        answer = "NO"
                        keepgoing = False
            elif arrA[n] == arrB[n]:
                answer = "YES"
                keepgoing = False
    return answer