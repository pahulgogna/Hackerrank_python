if __name__ == '__main__':
    N = int(input())
    list1 = []
    
    for _ in range(N):
        line = input().split()
        
        if line[0] == 'insert':
            position = int(line[1])
            num = int(line[2])
            list1 = list1[:position] + [num] + list1[position:]
            
        elif line[0] == 'print':
            print(list1)
            
        elif line[0] == 'remove':
            list1.remove(int(line[1]))
            
        elif line[0] == 'append':
            list1.append(int(line[1]))

        elif line[0] == 'sort':
            list1.sort()

        elif line[0] == 'pop':
            list1.pop()

        elif line[0] == 'reverse':
            list1.reverse()
