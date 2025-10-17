#creating a dictionary
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students)

#Accesing a specific attribute
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students['name'])

#access the key that doen't exist
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students.get('phone',['not found']))

#Add a key in a dictionay
Students ={'name':'Matee','age':'22','courses':['compsci']}
Students['phone']='0309-98-344'
print(Students)

#Update the value
Students ={'name':'Matee','age':'22','courses':['compsci']}
Students.update({'name':'Arslan'})
print(Students)

#Print keys in dictionary
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students.keys())

#Print values in dictionary
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students.values())

#Update Items in dictionary
Students ={'name':'Matee','age':'22','courses':['compsci']}
print(Students.items())

