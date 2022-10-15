def circularArrayRotation(a, k, queries):
    # Write your code here
    answers = []
    n = len(a)
    for q in queries:
        answers.append(a[((n - k + q) % n)])    
    return answers