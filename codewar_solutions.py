def get_count(sentence):
    return  len([x for x in sentence if x in "aeiou"])

def is_sorted_and_how(arr):
    return "yes, ascending" if (sorted(arr) == arr) else "yes, descending" if (arr == sorted(arr)[::-1]) else "no" 

from operator import add, sub, mul, truediv

def arithmetic(a, b, operator):
    ops = {
    'add' : add,
    'subtract' : sub,
    'multiply' : mul,
    'divide' : truediv,
    }
    return ops[operator](int(a), int(b))

def binary_to_string(binary):
    return ''.join([chr(int(x, 2)) for x in [binary[i:i+8] for i in range(0, len(binary), 8)]])

def balance(left, right):
    left = left.count("!") * 2 + left.count("?") * 3
    right = right.count("!") * 2 + right.count("?") * 3
    if left < right:
        return "Right"
    elif right < left:
        return "Left"
    else:
        return "Balance"

class Converter():
    @staticmethod
    def to_ascii(h):
        output = [h[i:i+2] for i in range(0, len(h), 2)]
        return ''.join([bytes.fromhex(x).decode("ascii") for x in output])
    
    @staticmethod
    def to_hex(s):
        return ''.join([x.lstrip("0x") for x in list(map(hex, list(map(ord, s))))])

        
        
# class Converter_Better():
#     @staticmethod
#     def to_ascii(h):
#         return h.decode("hex")
#     @staticmethod
#     def to_hex(s):
#         return s.encode("hex")

def highest_rank(arr):
    output = [(x, arr.count(x)) for x in arr]
    return max([x[0] for x in set(output) if x[1] == max(output, key=lambda x:x[1])[1]])

import re

def solve(s):
    return max(map(sum_string, re.split('[aeiou]', s)))

def sum_string(string):
    return sum([ord(x) - 96 for x in string])

from collections import Counter

def group(arr):
    return [[i] * j for i, j in Counter(arr).items()]