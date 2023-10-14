def minion_game(string):
    # your code goes here
    length = len(string)
    vowels = 'AEIOU'
    count = {'STUART': 0, 'KEVIN': 0}
    vowel_list = [i for i in range(length) if string[i] in vowels]
    non_vowel_list = [x for x in range(length) if string[x] not in vowels]
    for i in vowel_list:
        sub_len = length - i
        count['KEVIN'] += sub_len
    for j in non_vowel_list:
        sub_len = length - j
        count['STUART'] += sub_len
    if count['STUART'] > count['KEVIN']:
        print(f'Stuart {count["STUART"]}')
    elif count['STUART'] == count['KEVIN']:
        print('Draw')
    else:
        print(f'Kevin {count["KEVIN"]}')
        
        
                                       

if __name__ == '__main__':
    s = input()
    minion_game(s)