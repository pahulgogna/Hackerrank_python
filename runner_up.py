if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    g1 = arr[0]
    
    for i in range(len(arr)):
        if arr[i] >= g1:
            g1 = arr[i]

    n = [i for i in arr if i != g1]

    g2 = n[0]

    for i in range(len(n)):
        if n[i] >= g2:
            g2 = n[i]

    print(g2)
        