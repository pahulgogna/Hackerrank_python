count = {}

words = []
individual = []
num = int(input())
for i in range(num):
    n = input()
    words.append([i+1, n])

for i in words:
    if i[1] in count:
        count[i[1]] += 1
    else:
        individual.append(i)
        count[i[1]] = 1
out = ''
print(len(individual))
for j in individual:
    print(count[j[1]],end=' ')