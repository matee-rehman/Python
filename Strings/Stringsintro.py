#Printing a simple string
print('Hello WORLD')

#Printing a string with a Data-type
message='Hello world'
print(message)

#How to find the length of string
message= 'Matee is a good boy'
print(len(message))

#How to access a specific character in string
message='Matee eats good food'
print(message[11 ])

#How to Access specific WORDS in string(First index is inclusive:The end index is exclusive)
message='Matee lives in lahore'
print(message[0:8])

#METHODS OF DIFFERENT FUNCTIONS

#How to uppercase/lowercase our word 
message='Matee'
print(message.upper())
print(message.lower())

#How to count number of word or letter in string
message='Hello World'
print(message.count('O'))

#How to find word in string(if the word is not present it shows -1)
message='Matee is using VS CODE'
print(message.find('CODE'))
print(message.find('Colab'))

#How to replace word in string with another word(we will use two argument)
message="Hello World"
new_message = message.replace('World' , 'Universe')                      
print(new_message)

#Concatenate
greeting='Hello'
name='Matee'
message= greeting + ', ' + name + '. Welcome!'#Since it got complicated if we want to add more using '+' sign we will use 'Placeholders'
print(message)

#Concatenation with Placeholders
greeting='Hello'
name='Matee'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

#To search for the description of all the functions related to strings
print(help(str))

