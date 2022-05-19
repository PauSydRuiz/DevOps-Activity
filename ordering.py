breakfastList = {1: "Pancake", 2: "Hotdog", 3: "Egg"}
snackList={1: "Burger", 2: "Fries", 3:"Spaghetti"}
dessertList={1: "Cake", 2: "Juice", 3:"Ice Cream"}

menuList = {
    'Breakfast':{1: "Pancake", 2: "Hotdog", 3: "Egg"},
    'Lunch':{1: "Burger", 2: "Fries", 3:"Spaghetti"},
    'Dinner':{1:"Cake", 2: "Juice", 3:"Ice Cream"}
}

print("Breakfast",breakfastList)
print("Snack",snackList)
print("Dessert",dessertList)

count= input(int("Enter number of order"))

lis = []
for x in range(count):
    lis.append(menuList[int(input("Choose from the list: "))])

print("Your Order: ",lis)



