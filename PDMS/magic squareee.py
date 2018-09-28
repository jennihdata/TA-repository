n = 3
x = 0
y = int((n-1)/2)

array = [ ]

for i in range (0,n):
    array.append ([ ])
    for j in range (0,n):
        array[i].append (0)

array [x][y] = 1

num = 2
while num <= n*n:
    a = x-1
    b = y+1

    if (a<0):
        a=x-1+n

    if (b>=3):
        b=y+1-n

    if (array[a][b] != 0):
        a = x-1
        b = y

    x=a
    y=b

    array [a][b]= num


    num += 1

for a in array:
    print(a)