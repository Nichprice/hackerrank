def taumBday(b, w, bc, wc, z):
    # Write your code here
    cost = 0
    if bc + z < wc:
        cost = (b + w) * bc + (w * z)
    elif wc + z < bc:
        cost = (b + w) * wc + (b * z)
    else:
        cost = (b * bc) + (w * wc)
    return cost    
    