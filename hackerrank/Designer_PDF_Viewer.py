def designerPdfViewer(h, word):
    # Write your code here
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    h_max = 0
    for letter in word:
        index = al.index(letter)
        if h[index] > h_max:
            h_max = h[index]
    return h_max * len(word)
