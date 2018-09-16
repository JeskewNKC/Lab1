
def firstnonrepeatletter(word):
#  Function that accepts a string and returns the first non-repeating letter
    print(word)
# initialize variable count as list
    count = {}
# remove spaces and make string lowercase
    word.replace(' ','')
    word = word.lower()
    for letter in word:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    for letter in word:
        if count[letter] == 1:
            return letter
print (firstnonrepeatletter('Deep data structure'))
