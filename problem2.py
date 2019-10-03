score=list(map(int,input().split()))
my_score=list(map(int,input().split()))
s=set(score)
rank=[]
for i in my_score:
    c=1
    for j in s:
        if i<j:
            c=c+1
    rank.append(c)
print(rank)
count1=[]
for k in range(0,len(rank)):
    C=rank.count(rank[k])
    count1.append(C)
if count1.count(count1[0])==len(count1):
    print(min(rank))
else:
    print(rank[count1.index(max(count1))])
