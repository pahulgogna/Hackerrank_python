if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    
    greatest = arr[0]
    second_greatest = 0
    for i in arr:
        if i > greatest:
            second_greatest = greatest
            greatest = i
        elif int(second_greatest) < int(i) and i != greatest:
            second_greatest = i 
    print(second_greatest)
    # print(greatest)