def count_substring(string, sub_string):
    length = len(sub_string)
    end = 0
    count = 0
    for i in range(len(string)):
        end = i + length
        if end > len(string):
            break
        check = string[i:end]
        if check == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)