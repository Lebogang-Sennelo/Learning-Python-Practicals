#displaying the first item on the list
fruits=["apple","banana","cherry"]

print(fruits[0])

#changing list valuse
fruits[1]="blueberry"
print(fruits)

#append
fruits=["apple","banana","cherry"]
fruits.append("kiwi")
print(fruits)

#insert item to a certain posistion
fruits.insert(1,"orange")
print(fruits)

#remove items
fruits.remove("kiwi")
print(fruits)

#sorting items in ascending order
fruits.sort()
print(fruits)

#sorting in decending order
fruits.sort(reverse=True)
print(fruits)