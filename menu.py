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

count= int(input("Enter number of order: "))

lis = []
for x in range(count):
    
    foodType = input('Enter the type of menu you are ordering: ')
    
    if foodType=='Breakfast':
        lis.append(('Breakfast',breakfastList[float(input("Choose Breakfast: "))]))
    elif foodType=='Snack':
        lis.append(('Snack',snackList[float(input("Choose Snack: "))]))
    elif foodType=='Dessert':
        lis.append(('Dessert',snackList[float(input("Choose Dessert: "))]))
    else:
        print('Wrong input. Closing!!!')
        break;


print("Your Order: ",lis)



