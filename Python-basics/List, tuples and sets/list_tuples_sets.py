#create a list
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']

print(Fruit)

#locate by index(-1 for last item of index)
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']

print(Fruit[3])
print(Fruit[-1])

#Append in list
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.append('Tomato')
print(Fruit)

#insert according to index
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.insert(0,'Strawberry')
print(Fruit)

#Add List within List
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
veg= ['onion','potato']
Fruit .insert(0,veg)
print(Fruit)

#remove value in list
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.remove('Apple')
print(Fruit)

#pop method to remove
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.pop()
popped=Fruit.pop()
print(popped)
print(Fruit)

#Reverse our list
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.reverse()
print(Fruit)

#sorting our list
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']
Fruit.sort()
print(Fruit)

#min/max/sum
num= [1,2,3,4,5]
print(min(num))
print(max(num))
print(sum(num))

#find through index
Fruit= ['Apple', 'Mango', 'kiwi', 'banana', 'melon']

print(Fruit.index('melon'))

#Creating a tuple(separated from list with just changing bracket)
Fruit= ('Apple', 'Mango', 'kiwi', 'banana', 'melon')

print(Fruit)

##list are mutable(can be changed) & tuples are immutable(cannot be changed)

#Intersection methods of sets
Fruit= {'Apple', 'Mango', 'kiwi', 'tomato', 'pumpkins'}
veg={"potato",'tomato', 'pumpkins'}

print(Fruit.intersection(veg))

#Differences methods of sets
Fruit= {'Apple', 'Mango', 'kiwi', 'tomato', 'pumpkins'}
veg={"potato",'tomato', 'pumpkins'}

print(Fruit.difference(veg))

#union methods of sets
Fruit= {'Apple', 'Mango', 'kiwi', 'tomato', 'pumpkins'}
veg={"potato",'tomato', 'pumpkins'}

print(Fruit.union(veg))
