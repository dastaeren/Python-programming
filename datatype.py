x = "Hello World" #string
x = 50 #integer
x = 60.5 #float
x = 3j #complex
x = ["geeks","for","geeks"] #list
x = ("geeks","for","geeks") 
x = range(10)
x = {"name": "Suraj","age": 24}
x = {"geeks","for","geeks"}
x = frozenset({"geeks","for","geeks"})
x = True
x = b"Greeks"
x = bytearray(4)
x = memoryview(bytes(6))
x = None

my_list = [1,2,3,4,'string']
my_list.insert(2,5)# insert 5 at place 2
my_list.append(7)
my_list.remove(2)# doesn't follow array index and actually removes the contain as it remove 2
my_list.remove(my_list [0])


my_list.pop() #removing the last element
print('list after pop', my_list)
varpop = my_list.pop()
print('list remains unchanged', my_list)

print(my_list)
print(len(my_list))
print(varpop)