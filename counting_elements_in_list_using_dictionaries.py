# Enter your code here. Read input from STDIN. Print output to STDOUT

num = input()
list_ = [int(i) for i in input().split()]
count = {}

for i in list_:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

customers = int(input())

sales = 0

for i in range(customers):
    req = [int(x) for x in input().split()]
    if req[0] in count:
        if count[req[0]]>0:
            sales += req[1]
            count[req[0]] -= 1
        else:
            pass
    
print(sales)