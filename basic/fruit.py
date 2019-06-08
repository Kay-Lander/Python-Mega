content = open("fruits.txt")
food = content.read()
content.close()
fruits = food.splitlines()
for i in fruits:
    print(len(i))
