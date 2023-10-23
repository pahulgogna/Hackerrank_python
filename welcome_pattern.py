# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

n = int(n)
m = int(m)
dot_count = 2
other_half = ''
pattern_list = []
for rows in range(n):
    if rows < (n-1)//2:
        for i in range((m//2) - (rows*3)-1):
            print('-', end='')
            other_half = '-' + other_half
            
        s = 0
        for x in range((rows*3) + 2):
            if s == 0:
                print('.', end='')  # initial . in every line
                other_half ='.' + other_half
                s += 1
                
            # the center |
            elif i + x + 1 == (m-1)//2:
                print('|', end='')
            elif dot_count < 2:
                print('.', end='')
                other_half = '.' + other_half
                dot_count += 1
            else:
                print('|', end='')
                dot_count = 0
                other_half = '|' + other_half
        
        s = 0
        print(other_half)
        rev = ''
        for i in other_half:
            rev = i + rev
        pattern_list = [rev + '|' + other_half] + pattern_list
        other_half = ''
        
        
    elif rows == (n-1)//2:
        for i in range((m+1)//2 - 4):
            print('-', end='')
        print('WELCOME', end='')
        for i in range((m+1)//2 - 4):
            print('-', end='')
        print()
for i in pattern_list:
    print(i)
