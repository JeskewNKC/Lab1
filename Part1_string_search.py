import collectx2 = x2.lower()ions
def string_find(x):
    x2 = x.replace(' ','')

    c = collections.Counter(x2)
    y = [char for char in x2 if c[char] ==1]
    print (x)
    print (y[0])

string_find('Deep data structure')

