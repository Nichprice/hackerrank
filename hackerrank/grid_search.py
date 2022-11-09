G = ["7283455864",
"6731158619",
"8988242643",
"3830589324",
"2229505813",
"5633845374",
"6473530293",
"7053106601",
"0834282956",
"4607924137"]
P = ["9505",
"3845",
"3530"]

R = len(G)
C = len(G[0])
r = len(P)
c = len(P[0])

def gridSearch(G, P):
    # Write your code here
    def check(x, y):
        for i in range(r):
            if P[i] != G[x + i][y:y+c]:
                return False

        return True

    for i in range(R):
        for j in range(C):
            if G[i][j] == P[0][0]:
                if check(i, j):
                    return("YES")

    return("NO")