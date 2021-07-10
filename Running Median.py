#Problem statement

"""Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

#Solution

def median(seq):
    seq.sort()
    if len(seq) % 2 != 0:
        med = seq[len(seq)//2]
    else:
        med1 = seq[int(len(seq)/2) - 1]
        med2 = seq[int(len(seq)/2)]
        med = (med1 + med2)/2
    return  med

def run_med(seq):
    for i in range(1, len(seq)+1):
        print(median(seq[:i]))


a = [2, 1, 5, 7, 2, 0, 5]
run_med(a)

