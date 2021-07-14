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
    lines = math.ceil(total/k)
    word_each_line = math.ceil(len(words)/lines)

    for i in range(lines):
        res.append("")
        word_counter = word_each_line

        j = 0
        for word in words:
            print('ini words', words)
            if len(res[i]) <= k and word_counter > 0:
                #print('ini word_counter' + str(word_counter) + 'ini len(res[i]' + str(len(res[i])) +''+ str(k))

                print('ini words[' + str(j) + ']' + str(words[j]))
                res[i] += words[j]
                res[i] += ' '
                word_counter -= 1
                words.pop(j)


        '''

        len_word = len(words)
        j = 0
        while(j < len_word):
            if len(res[i]) <= k and word_counter > 0:
                res[i] += words[j]
                print("ini word [" + str(j) + str(words[j]))
                res[i] += ' '
                word_counter -= 1
                words.pop(j)
                len_word -= 1
            j += 1
        '''


    print(word_each_line)
    print(word_length)
    print(res)
    print(total)
    print(math.ceil(total/k))
    print(words)

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
justify(words, 16)
words_test = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

newlist = list()
for word in words_test:

    print('ini word', word)
    print('ini word[0]', words_test[0])
    print('word test sebelum delete:', words_test)
    words_test.pop(0)
    print('word test setelah delete: ', words_test)
    print()


