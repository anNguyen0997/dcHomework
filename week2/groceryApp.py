
# A user should be able to create a shopping list.

# A shopping list consists of a title and address.

# A user should be able to add multiple shoppings lists

# A user should be able to add a grocery items to a particular shopping list.

def menu():                                             # function to display options
    while True:                                         # loop to prompt menu
        print('\n------ SHOPPING LIST ------')
        print('''1. Add an item
2. Display shopping list
3. Exit''')

        userIn = input("\n Choose an Option : ")        # taking in an input using options menu

        if userIn == '1':                               # if input is 1, it will run add items function
            addItem()
        elif userIn == '2':                             # will run display list function
            displayList()
        elif userIn == '3':                             # will exit game
           break
        else:                                           # any input that is not include in menu
            print("INVALID OPTION")


shoppingList = {'name': [], 'quantity': [], 'price': []}

name = shoppingList['name']                             # saving key, value pairs to a variable
quantity = shoppingList['quantity']
price = shoppingList['price']

# Functions

def displayList():                                      # displaying function and printing things the items consists of
        print(shoppingList['name'])
        print(shoppingList['quantity'])
        print(shoppingList['price'])
        
def addItem():                                          # will add/append the input into the 'name' key
    item = input('Enter item to add : ')
    name.append(item)

    amount = input('Enter amount : ')                   # will add/append the input into the 'quantity' key
    item = input('Enter item to add : ')
    quantity.append(amount)

    priceOf = input('Enter price : ')                   # will add/append the input into the 'price' key
    item = input('Enter item to add : ')
    price.append(priceOf)
    
menu()
