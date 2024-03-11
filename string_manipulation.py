my_city = "New York"
print(type(my_city))

my_city = 'New York'
print(type(my_city))

my_city = str("New York")
print(type(my_city))

my_city = "'New York'" #it will print with single quote
print(my_city)

x = 1
print(type(x))

y ='2'
print(type(y))

word1 = 'New '
word2 = 'York'
print(word1 + word2)

word = "Rio de Janeiro"
char = word[4]
print(char)

x = word.replace("Rio","Mar")
print(x)

word = 'Rio de Janerio'
print(word.count('o'))

#repeat string 
work = "Tokyo "*3
print(work)

#split string
work = "Rio de Janerio"
split_words = work.split(' ')
print(split_words)

#reuse the list
print(split_words[0])
print(split_words[1])
print(split_words[2])
