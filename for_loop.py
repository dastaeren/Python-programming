fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "banana":
     print(x)    

for x in fruits:     
    if x == "banana":
     break #stops at banana

for x in fruits:
   if x =="banana":
    continue #banana is excluded
   print(x)

for x in range(6): #it will stop at 5 and if your rang is 8 it will stop at 7
   print(x)   

for x in range(2,6):
   print(x)

for x in range(2,30,3):
   print(x)   

for x in range(6):
   print(x)
else:
   print("Finally Finished")
        