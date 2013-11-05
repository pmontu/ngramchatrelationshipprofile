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
#print words[0]
#print words[1]

def makecloud(words):
    previous = words[0]
    c=1
    i=1
    l=len(words)
    cloud = []
    while i<l:
        current = words[i]
        if previous == current:
            c+=1
        else:
            cloud.append([previous,c])
            c=1
            previous = current
        i+=1
    return sorted(cloud, key=lambda student: student[1], reverse=True)

cloud1=makecloud(words[0])
cloud2=makecloud(words[1])

def makeranks(cloud):
    l = len(cloud)
    i=0
    while i<l:
        cloud[i].append(i+1)
        i+=1
    return cloud

cloud1=makeranks(cloud1)
cloud2=makeranks(cloud2)

print cloud1
print cloud2


