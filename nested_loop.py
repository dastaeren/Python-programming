#loop inside loop

adj = ["red","big","tasty"]# 3 elements in list
fruits = ["apple","banana","cherry"]

for x in adj:
    print('Fruits')#print for 3times
    for y in fruits:
        print(x,y) #Print statement is executed 3x3= 9 times as it is inside loop(nested loop)

for x in [0,1,2]:
    pass        