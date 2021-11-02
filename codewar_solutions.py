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

# len(a) will give you the number of top-level elements in the list/array named a.

# Your task is to create a function deepCount that returns the number of ALL elements within an array, including any within inner-level arrays.

# For example:

# deepCount([1, 2, 3]);  
# //>>>>> 3
# deepCount(["x", "y", ["z"]]);  
# //>>>>> 4
# deepCount([1, 2, [3, 4, [5]]]);  
# //>>>>> 7

def deep_count(listOfElem):
    count = 0
    for elem in listOfElem:
        count += 1
        if type(elem) == list:
            count += deep_count(elem) 
    return count

# We'll create a function that takes in two parameters:

# a sequence (length and types of items are irrelevant)
# a function (value, index) that will be called on members of the sequence and their index. The function will return either true or false.
# Your function will iterate through the members of the sequence in order until the provided function returns true; at which point your function will return that item's index.

# If the function given returns false for all members of the sequence, your function should return -1.

# true_if_even = lambda value, index: value % 2 == 0
# find_in_array([1,3,5,6,7], true_if_even) # --> 3

def find_in_array(seq, predicate): 
    for index, number in enumerate(seq):
        if predicate(number, index):
            return index
    return -1

# Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).

# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/

# twoSum [1, 2, 3] 4 === (0, 2)

def two_sum(numbers, target):
    output = []
    for index, number in enumerate(numbers):
        try:
            if numbers.index(target - number, index+1, len(numbers)):
                output.append(index)
                output.append(numbers.index(target - number, index+1, len(numbers)))
                break
        except ValueError:
            continue
    return output