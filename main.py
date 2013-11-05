f = open('input00.txt','r')
name1 = "Mohan Kumar D"
name2 = "Manoj Kumar P"
words=[[],[]]
for line in f:
    line = line.rstrip('\n')
    if name1 == line:
        pool = 0
    elif name2 == line:
        pool = 1
    else:
        words[pool] += line.split(' ')
words[0].sort()
words[1].sort()
print words[0]
print words[1]

