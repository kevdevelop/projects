inventory = {'Waffle Batter Mix': 10, 'Milk Carton': 0, 'Egg': 8, 'Butter': 0, 'Vanilla Ice Cream': 15, 'Strawberry Ice Cream': 9, 'Chocolate Ice Cream': 6, 'Napkins': 50, 'Plasticware': 40, 'Serving Boats': 30}
suppliers = {'Vandelay': 0, 'Madrigal': 500, 'DunderMifflin': 0}

Vandelay = {'Waffle Batter Mix': 10, 'Milk Carton': 0, 'Egg': 8, 'Butter': 0}
Madrigal = {'Vanilla Ice Cream': 15, 'Chocolate Ice Cream': 6, 'Strawberry Ice Cream': 9}
DunderMifflin = {'Napkins': 50, 'Plasticware': 40, 'Serving Boats': 30}

key_list = list(inventory.keys())
value_list = list(inventory.values())

query = input("""        Welcome to the Egan EZ Inventory System! Type: 
            inventory -- for current inventory list,
            suppliers -- for current suppliers and outstanding balances,
            order ------ for item(s) in need of ordering,
            sales ------ for store-specfic sales information,
            OR
            enter inventory item or supplier to search for: 
            """)

if query == "inventory":
    for akey in inventory.keys():
        print("Got item", akey, "with a stock count of", inventory[akey], ".")

elif query == "suppliers":
    for akey in suppliers.keys():
        print(akey, ", with an outstanding balance of $", suppliers[akey], ".")

elif query == "order":
    order_list = ''
    for akey in inventory.keys():
        if inventory[akey] == 0:
            order_list += akey
            order_list += ", "
    order_list = order_list[:-2]
    print("The following items need to be ordered: ", order_list)

elif query == "sales":
    man = {'January': 4200, 'February': 4400, 'March': 5100, 'April': 5400, 'May': 5500, 'June': 6400, 'July': 7800, 'August': 8100, 'September': 7700, 'October': 6100, 'November': 5300, 'December': 4800}
    valpark = {'January': 2700, 'February': 3200, 'March': 3800, 'April': 4300, 'May': 5000, 'June': 5800, 'July': 6800, 'August': 7200, 'September': 7000, 'October': 6200, 'November': 5200, 'December': 4100}

    store = input("Enter machester OR valleypark : ")
    if store == "manchester":
        print("Here are the monthly sales for the Manchester store in 2017:")
        total = 0
        for akey in man.keys():
            print("For the month of", akey, ", sales at the Manchester store totaled $", man[akey])
        for akey in man.keys():
            total += man[akey]
        print("Manchester sales for 2017 totaled $", total)
        
    if store == "valleypark":
        print("Here are the monthly sales for the Valley Park store in 2017:")
        total = 0
        for akey in valpark.keys():
            print("For the month of", akey, ", sales at the Valley Park store totaled $", valpark[akey])
        for akey in valpark.keys():
            total += valpark[akey]
        print("Valley Park sales for 2017 totaled $", total)

elif query == "Vandelay":
    stock_list = ''
    for akey in Vandelay.keys():
            stock_list += akey
            stock_list += ", "
    stock_list = stock_list[:-2]        
    print(query, "is our supplier for the following: ", stock_list)

elif query == "Madrigal":
    stock_list = ''
    for akey in Madrigal.keys():
            stock_list += akey
            stock_list += ", "
    stock_list = stock_list[:-2]        
    print(query, "is our supplier for the following: ", stock_list)

elif query == "DunderMifflin":
    stock_list = ''
    for akey in DunderMifflin.keys():
            stock_list += akey
            stock_list += ", "
    stock_list = stock_list[:-2]        
    print(query, "is our supplier for the following: ", stock_list)

elif query in inventory:
    if inventory[query] == 0:
        print("Time to order", query, "! Out of stock.")
    else:
        print("We have", query,", with", inventory[query], "still in stock.")

else:
    print("Error! Please try again")