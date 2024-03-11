string = 'Geeks'
def test(string):
    string = "GreeksforGeeks"
    print("Inside Function:", string)

test(id(string)) # giving memory address by using 'id'
print("Outside function:", string)   