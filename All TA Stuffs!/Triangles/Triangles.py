
sym = "*"
mult = 1
count = 6

while mult<= count:
    print (sym*mult)
    mult = mult + 1

mult1 = 1
while mult1<= count:
    print(" " * (count - mult1) + "*" * mult1)
    mult1 = mult1 + 1

mult2 = 1
while mult2 <= count:
    print(" " * (count - mult2) + "*" * (mult2*2-1))
    mult2 =mult2 +1

mult3 = 1
while mult3 <= count:
    print (" "* (count - mult3) + "*" * (mult3*2-1))
    mult3= mult3 +1

mult4=1
count1=10
while mult4<= count1:
    print (" " * mult4 + "*" * (count1-(mult4*2-1)) + " " * mult4)
    mult4 = mult4+1