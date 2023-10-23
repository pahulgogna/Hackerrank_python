

def print_formatted(number):
    # your code goes here
    string = ''
    longest = len(str(bin(number))) # spacing between numbers in str
    num_length = len(str(number))
    spacing = ''
    
    for i in range(1,number+1):
        
        for j in range(4):
            if j == 0:
                to_print = str(i)
            elif j == 1:
                to_print = str(oct(i,))[2:]
            elif j == 2:
                to_print = str(hex(i,))[2:]
                if to_print in 'abcdef':
                    to_print = to_print.upper()
            elif j == 3:
                to_print = str(bin(i,))[2:]
            
            req = longest - len(to_print) - 2
            for _ in range(req):
                spacing += ' '
            string = string + spacing + ' ' + to_print
            spacing = ''
        print(string[1:])
        string = ''
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)