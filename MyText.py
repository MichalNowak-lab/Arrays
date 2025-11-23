def numOfWords(n):
    words = n.split()
    return len(words)

def orderedWordsLen(n):
    words = n.split()
    x = sorted(words, key=len, reverse=True)
    return x


def orderedWords(n):
    words = n.split()
    x = sorted(words)
    return x

print(orderedWordsLen('aaa bb cc asdsasd'))
print(orderedWords('bbbb ccccc aaaaa'))