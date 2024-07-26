print("Welcome in zaika")
menu= {
    "pasta": 70,
    "cold dink": 40,
    "sandwich": 30,
    "cold coffee": 60,
    "burger": 50
}
print("our menu:")
print("---------")
total_order = 0
for item,price in menu.items():
    print(f"{item} :Rs. {price}")

next_order= True
while next_order:
    order = input("Enter the name of  item you want to add in order").lower()
    if item in menu:
        total_order += menu[item]
        print(f"{order} added in your order")
        another_order = input("Do you want to ad another item? press(yes/no").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False
    else:
        print(f"{item} is not available")
        another_order = input ("Do you want to ad another item? press(yes/no").lower()
        if another_order == 'yes':
            next_order =True
        else:
            next_order = False
print(f"your total bill is : Rs. {total_order}")