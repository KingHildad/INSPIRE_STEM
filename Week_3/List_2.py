friends=["Jack","Jane","Austin","Michelle","Bii"]
for friend in friends:
    print(friend)

enemies=friends[:]#Copies one list into another

for enemy in enemies:
    print(enemy)


fruits=["Apple","Mango","Banana","Passion","Orange","Eggplant"]
print((fruits[0:3]))
del fruits[0]
print(fruits)
#Slice the list

cities=("Nairobi","Juja","Kampala","Ngoingwa","Eldoret","Nakuru","Nyeri")
print(cities)

squares=[]#initialises my empty list
for x in range(0,12):
    squares.append(x**2)
    print(squares)