def bonAppetit(bill, k, b):
    # Write your code here
    b_actual =  int((sum(bill) - bill[k]) / 2)
    if b - b_actual != 0:
        print(b - b_actual)
    else:
        print("Bon Appetit")