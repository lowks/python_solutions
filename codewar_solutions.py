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