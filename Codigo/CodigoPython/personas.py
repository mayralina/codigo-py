#un for loop es utilizado para iterar sobre una secuemcia (puede ser una lista, un diccionario, un conjunto o una string)

#Simple loop
people = ["Andres" ,"Alejandra", "Benito","Jose"]

print("**** Simple loon****")
for person in people:
  print("Current person : {0}" .format(person))

#Break
print("****Break loop****")
for person in people:
   if person=="Benito":
     break
   print("Current person: {0}" .format(person))
   print("Estas orden tiene que estar intentadas")

print("****Range loop****")
#range
for i in range(len(people)):
   print (people[i])

for i in range(0,len(people)):
   print("Number: {0}". format(i))
   print("Orden extra par ver la imporatancia de indentacion")

#While loops : hasta que se cumpla una condicion 

count= 0
while count <=10:
   print ("Count: {0}" .format(count))
count+=1
