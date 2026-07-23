# Prices of food
menu = {
    "Pizza" : 90,
    "Tea" : 10 , 
    "Burger" : 40,
    "Coffee" : 25,
    "French Fries" : 70,
    "Dosa" : 70
}
#Greetings
print("Good morning customer")

# Showing the menu
print(f'''
Your Menu sir/mam:
       Pizza = Rs. {menu["Pizza"]}
       Burger = Rs. {menu["Burger"]}
       Tea = Rs. {menu["Tea"]}
       Coffee = Rs. {menu["Coffee"]}
       French Fries = Rs. {menu["French Fries"]}
       Dosa = Rs. {menu["Dosa"]}
      ''')

# Ordering
order = input("Please give us your order: ")
total = 0

if order in menu:
    print("Your order has been placed !\nDo you want something more")
    total += menu[order]
    order = input("Please give us your order")
    if order in menu:
        print("Your order has been placed")
        total += menu[order]
        print("I hope you enjoyed the meal")
        print(f"Your total is {total}")

    else:
        print(f"Your total is {total}")
        print("I hope you enjoyed the meal")

else:
    print("Sorry order not in the menu")