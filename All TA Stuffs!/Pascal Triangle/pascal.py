num_of_pascal= int(input("Number of pascal: "))
list1 = [1]
print (list1)
for i in range(num_of_pascal):
    newlist=[]
    newlist.append(1)
    for z in range(len(list1)-1):
        newlist.append(list1[z]+list1[z+1])
    newlist.append(1)
    list1=newlist
    print(list1)
