def get_count(sentence):
    return  len([x for x in sentence if x in "aeiou"])

def is_sorted_and_how(arr):
    return "yes, ascending" if (sorted(arr) == arr) else "yes, descending" if (arr == sorted(arr)[::-1]) else "no" 