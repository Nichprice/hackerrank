def organizingContainers(container):
    # Write your code here   
    conts = [sum(c) for c in container]
    types = [0] * n 

    for c in container:
        for i in range(n):
            types[i] += c[i]

    if sorted(types) == sorted(conts):
        return 'Possible'
    else:
        return 'Impossible'