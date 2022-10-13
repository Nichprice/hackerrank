def organizingContainers(container, n):
    # Write your code here   
    types = [0] * n 
    containers = [0] * n 

    for i in range(n):
        for j in range(n):
            types[i] += container[i][j]
            containers[i] += container[j][i]

    if sorted(types) == sorted(containers):
        return 'Possible'
    else:
        return 'Impossible'