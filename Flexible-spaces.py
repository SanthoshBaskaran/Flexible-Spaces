partitions=[0]
solution_list=[]
str1=""
width=list(map(int,input().split()))
inter_partitions=list(map(int,input().split()))
for i in inter_partitions:
    partitions.append(i)
partitions.append(width[0])
j=0
for i in partitions:
    j=j+1
    while(j<len(partitions)):
        result=partitions[j]-i
        solution_list.append(result)
        j=j+1
    j=partitions.index(i)
conclusion=list(dict.fromkeys(solution_list))
conclusion.remove(0)
conclusion.sort()
for l in conclusion:
    if(l<0):
        remove(l)
for j in conclusion:
  if(type(j)==int):
    str1=str1+str(j)+' '
print(str1)
