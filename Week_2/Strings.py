#Strings in python
#Date:22/02/2024
#Name:Hildad

city="Nairobi"

#Convert to uppercase
print(city)
print("\n") #New line
print(city.upper())

#Converts to lowercase
print("\n")
print(city.lower())

town="       Juja      "
print("\t") #New tab
print(town.strip())

#Add two strings
f_name="Hildad"
s_name="Muchiri"
Full_name=f_name + s_name

print(Full_name)


print(city[0])#from 0-6 prints the number forwards
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[5])
print(city[6])
print(city[-1])#negative 1-6 prints the word backwards
print(city[-2])
print(city[-3])
print(city[-4])
print(city[-5])
print(city[-6])
print(city[-0])

#Replacing a character
fruit="orange"
print(fruit.replace("o","y"))

#splitting characters
subject="Chemistry,Physics"
print(subject.split(","))
print(subject.split(":"))

age=19
height=2.0

print("i am  {0} years old and {1} meters tall" .format (age,height)) 

#len()-Counts the number of characters in a word
height = 1.22345

name = "Hildad"
print(len(name))


