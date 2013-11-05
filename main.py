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
    p = 0
    rank=1
    cloud[0].append(rank)
    i=1
    c=1
    count=1
    while i<l:
        c=i
        #position 1 is frequency
        if cloud[p][1] <> cloud[c][1]:
            p = c
            rank+=count
            count=1
        else:
            count+=1
        cloud[i].append(rank)
        i+=1
    return cloud

cloud1=makeranks(cloud1)
cloud2=makeranks(cloud2)

l1=len(words[0])
l2=len(words[1])
def makeweights(cloud):
    i=0
    l=len(cloud)
    while i<l:
        cloud[i].append(round(100.0*cloud[i][1]/l,2))
        i+=1
    return cloud

clod1=makeweights(cloud1)
clod2=makeweights(cloud2)

#print cloud1
#print cloud2

def printtoexcel(cloud):
    for item in cloud:
        print item[0]+"\t"+str(item[1])+"\t"+str(item[2])+"\t"+str(item[3])
    print ""

printtoexcel(cloud1)
printtoexcel(cloud2)



