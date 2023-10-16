if __name__ == '__main__':
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data = [name, score]
        names.append(data)
        
    least = names[0][1]
    l2 = names[0][1]
    for i in range(len(names)):
        if least > names[i][1]:
            least = names[i][1]

    new = [i for i in names if i[1] != least]

    least = new[0][1]
    for i in range(len(new)):
        if least > new[i][1]:
            least = new[i][1]
    final = [i for i in new if i[1] == least]
    
    final.sort()
    
    for i in final:
        print(i[0])