
import collections

def string_find(x):

    x2 = x.replace(' ','')
    x2 = x2.lower()
    c = collections.Counter(x2)
    y = [char for char in x2 if c[char] ==1]
    print (x)
    print (y[0])

string_find('Deep data structure')

