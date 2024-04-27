pizza = {'crust' : 'thick' ,
         'toppings' : ['mushrooms', 'extra cheese', 'strawberry'] }
print(f"You ordered a {pizza['crust']} - crust pizza"
       "\nwith following toppings")
for topping in pizza['toppings']:
    print(topping)