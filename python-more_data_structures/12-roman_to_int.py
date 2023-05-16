#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    length = len(roman_string)
    for i in range(length):
        if i > 0 and rom_num[length[i]] > rom_num[length[i - 1]]:
            int_val += rom_num[length[i]] - 2 * rom_num[lengthg[i - 1]]
        else:
            int_val += rom_num[length[i]]
    return int_val
