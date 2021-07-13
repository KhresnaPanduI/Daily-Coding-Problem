#Difficulty: Medium
#Problem statement
"""This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary
so that each line has exactly length k. Spaces should be distributed as equally as possible,
with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

#Solution

def justify(words, k):
    res = list() #result list

    #count each word length and assign to dictionary
    word_length = dict()
    total = 0
    for item in words:
        word_length[item] = len(item)
        total += len(item)

    #Split each word to k-char
    import  math

    for i in range(math.ceil(total/k)):
        for word in words:
            res.append("")
            if len(res[i]) <= 16:
                res[i] += word
                res[i] += ' '
                words.remove(word)

    print(word_length)
    print(res)
    print(total)
    print(math.ceil(total/k))


justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)

cek = list()
print(cek)
cek.append("")
cek[0] += 'tes'
cek.append("")
cek[1] += 'tes2'
print(cek)