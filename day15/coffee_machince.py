""""
Virtual coffee machine

"""


resource={
    "water":300,
    "milk":200,
    "coffee":100,
    "Money":0
}

coffee_type={

    "espresso":
            {
                "ingredients":{
                                "water":50,
                                "coffe":18,
                                },
                "Cost":1.5,
            },
    "latte":{
                "ingredients":{
                                "water":200,
                                "coffe":24,
                                'milk':150
                                },
                "Cost":2.5,
             },
    "cappuccino":{
                "ingredients":{
                                "water":250,
                                "coffe":24,
                                'milk':100
                                },
                "Cost":3.0,
                }
}
# This method is working
def report():
    """Display the current available resource in the coffee machine"""
    print(resource)
# money calculate and return other method
def money_check():
    """The method calculate the user coin and return output other method"""
    quarters=0.25
    dimes=0.10
    nickles=0.05
    pennies=0.01
    print("Please enter coin")
    d_coins = float(input("Enter How many dimes "))
    n_coins = float(input("Enter How many nickles "))
    p_coins = float(input("Enter How many pennies "))
    q_coins = float(input("Enter How many quarters "))
    q = quarters*q_coins
    d=dimes*d_coins
    n=nickles*n_coins
    p=pennies*p_coins
    total_cost = q+d+n+p
    return total_cost


def user_get_money(second,money):
    """Display refund money back to the user"""
    return f" Remaining amount after coffee  {second-money}"

def cost_check(money,second):
    """This function used to credit and debit to money to user and vendor"""
    if money==second:
        print("Please Having Coffee")
        resource['Money'] +=money
    elif money< second:
        print(f"Money is not sufficient {money}")
    elif money>second:
        print("Please Having Coffee")
        out=user_get_money(second,money)
        resource['Money'] +=second
        print(out)
# This method working
def calculation_Insufficient(use_coffee_type):
    """his method used to check the resource available inside the machine and make the coffee available to you"""
    data_coffee_type =coffee_type[use_coffee_type]['ingredients']
    if resource['water'] > data_coffee_type['water'] and resource['coffee'] > data_coffee_type['coffe']:
        resource['water'] -=data_coffee_type['water']
        resource['coffee'] -= data_coffee_type['coffe']
        cost=money_check()
        print("Total coins you enter into machine is :",cost)
        second_parameter=coffee_type[use_coffee_type]['Cost']
        cost_check(cost,second_parameter)
    else:
        print("Insufficient resource. ")

# This method is working
def add_resource():
    """This is admin method allow to add the resource to the machine"""
    resource_add = input("What do you want to add :")
    quality= int(input("Enter amount of quality"))
    if resource_add in resource:
        resource[resource_add]+=quality
    else:
        print("Check the input")

while True:
    user_prompt = input("What would you like? (espresso/latte/cappuccino):")
    if  user_prompt=='espresso':
            calculation_Insufficient('espresso')
    elif user_prompt=='latte':
            calculation_Insufficient('latte')
    elif user_prompt=='cappuccino':
            calculation_Insufficient('cappuccino')
    elif user_prompt=='report':
        report()
    elif user_prompt=='add':
        add_resource()
    if user_prompt=='off':
        break


