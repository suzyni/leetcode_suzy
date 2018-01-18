import collections
import operator
line = "aa AA bb cc CC cc dd ee ee ee ee ee ee ff ff ff ff gg"
line = line.lower().split()
fre = collections.Counter(line)
dict1 = {1:2, 3:4, 7:1, 5:2}
#print sorted(dict1.items(), key = operator.itemgetter(1))[::-1]
for item in fre:
    print item
