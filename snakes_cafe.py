# When run, the program should print an intro message and the menu for the restaurant
# The program’s content should match included sample exactly
print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

# The restaurant’s menu should include appetizers, entrées, desserts, and beverages.
# The program should prompt the user for an order

# Dictionary to track orders
ordered_items = {}

# While loop to continue taking order until user enters 'quit'
while True:
    # The > character represents user input line and should be printed out with a trailing space.
    order = input("> ")

    if order in ordered_items:
        ordered_items[order] += 1
        # When a user enters an item, the program should print an acknowledgment of their input
        print(f"** {ordered_items[order]} orders of {order} have been added to your meal **")
    else:
        ordered_items[order] = 1
        # When a user enters an item, the program should print an acknowledgment of their input
        print(f"** 1 order of {order} has been added to your meal **")
    if order == "quit":
        ordered_items.pop("quit")
        for i in ordered_items:
            print("You ordered " + str(ordered_items[i]), i + "('s)")
        break
