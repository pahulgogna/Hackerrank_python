def solve(s):
    post_space = False
    out = ''
    first_letter = True
    for i in s:
        if post_space:
            if i == ' ':
                out += i
            else:
                out += i.upper()
                post_space = False
        else:
            if first_letter:
                out += i.upper()
                first_letter = False
            else:
                out += i
                if i == ' ':
                    post_space = True
    return out

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
