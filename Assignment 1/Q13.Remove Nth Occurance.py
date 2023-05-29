# Python program to remove Nth occurrence of the given word

def remove_nth_occurrence(word, string, n):
    words = string.split()
    count = 0
    for i, w in enumerate(words):
        if w == word:
            count += 1
            if count == n:
                del words[i]
                break
    return ' '.join(words)

string = "the quick brown fox jumps over the lazy dog"
word = "the"
n = 2
new_string = remove_nth_occurrence(word, string, n)
print(new_string)


def Nth_occurrence(data,word,count):
    return

data = "i am rohan i am from palghar i i am"
word = 'i'
count = 2

result = Nth_occurrence(data,word,count)