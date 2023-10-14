if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    perm = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)] 

    a = [perm[i] for i in range(len(perm)) if (perm[i][0] + perm[i][1] + perm[i][2] != n)]
    print(a)