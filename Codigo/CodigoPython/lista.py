#Hola otra vez
#A list is a collection which isordered and changable. Allows duplicate

#create a list , ist wat to do it
numbers = [1,2,3,4,5]
fruits= [" manzanas", "naranjas" , "platano" ,"pepino"]

print(numbers, fruits)

#Get a value of a list
print(fruits[0])

#Get length
print(len (fruits))

#Append to the list 
fruits.append("platano")
print(fruits)

#Remove from the lista
fruits.remove("naranjas")
print(fruits)

#insert to position
fruits.insert(2,"manzanas")
print(fruits)

#Reverse the lista
fruits.reverse()
print(fruits)

#sort alphbetically
fruits. sort()
print(fruits)
