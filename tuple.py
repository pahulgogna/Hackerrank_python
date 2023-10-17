# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

nums = [int(i) for i in input().split()]

tu = tuple(nums)

print(hash(tu))