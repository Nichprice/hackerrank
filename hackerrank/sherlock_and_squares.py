def squares(a, b):
    # Write your code here
    sq1 = a ** .5
    if round(sq1, 1) != sq1:
        sq1 = int(sq1 + 1)
    sq2 = int(b ** .5)
    return int((sq2 - sq1) + 1)