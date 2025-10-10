#Testing if statement
language = 'python'
if language == 'python':
     print('condition is true')

#Testing else statement
language = 'javascript'
if language == 'python':
    print('language is python')
else:
    print("its another language" )

#Testing elif
language = 'javascript'
if language == 'python':
    print('language is python')
elif language == 'javascript':
 print('lanugage is javascript')
else:
    print("its another language" )

#Boolean functions(AND)
user='Matee'
age = '18'
if user=='Matee' and age=='18':
    print('You can vote')
else:
    print('You cannot vote')   
#OR
user='wsif'
age = '18'
if user=='Matee' or age=='18':
    print('You can vote')
else:
    print('You cannot vote')      

 # Program using the NOT function

is_raining = False

if not is_raining:
    print("You can go outside without an umbrella!")
else:
    print("Take an umbrella with you!")
