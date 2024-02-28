My_laptop={"make":"Apple","Colour":"Silver","weight":"7500 grams","speed":"2.5 gigeherts"}

print(My_laptop["make"])
print(My_laptop["Colour"])
print(My_laptop["weight"])
print(My_laptop["speed"])

My_laptop["Colour"]="red"
for key,value in My_laptop.items():
    print(key)
    print("\n")
    print(value)
