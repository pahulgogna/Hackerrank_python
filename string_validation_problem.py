if __name__ == '__main__':
    a = input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    for s in a:
        if s.isalnum():
            alnum = True
            
        if s.isalpha():
            alpha = True
      
        if s.isdigit():
            digit = True
            
        if s.islower():
            lower = True

        if s.isupper():
            upper = True
    
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
