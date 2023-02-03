""" Given an array of integers.
Return an array, where the first element is the count of positives 
numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array. """

def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    p = sum([1 for i in arr if i > 0])
    n = sum([i for i in arr if i < 0])
    return [p,n]