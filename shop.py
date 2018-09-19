####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Get Baked"
signature_flavors = ["tuna","salmon","red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("Cashier: Hello! Can I take your order?")
    print("Here are our menu:")
    for i in menu:
        print("-%s (%.2f KD)" % (i,menu[i]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here! 
    for j in original_flavors:
        print("-",j)

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for k in signature_flavors:
        print("-",k)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order.lower() in menu or order.lower() in original_flavors or order.lower() in signature_flavors:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("What's your order? (type 'Exit' to end your order)")
    while True:
        temp = input()
        if temp.lower() != "exit":
            if is_valid_order(temp.lower()) == True:
                order_list.append(temp.lower())
            else:
                print("~Please enter the exact spelling as shown in the menu~")
        else:
            break
        
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print("~This order is eligible for credit card payment.~")
    else:
        print("~This order is not eligible for credit card payment.~")
        

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for i in order_list:
        if i in menu:
            total += menu[i]
        elif i in original_flavors:
            total += original_price
        else:
            total += signature_price

            
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    total = get_total_price(order_list)
    if len(order_list) > 0:
        for i in order_list:
            print("-",i)
        print("The total price is %s KD" % total)
        accept_credit_card(total)
    else:
        print("~Empty~")

    print("Thank you for shopping at %s" % cupcake_shop_name)
        
