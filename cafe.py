menu = ['cake', 'coffee', 'sandwich', 'tea']


# This will create a dictionary for stock values
stock = {           
  'cake': 300,
  'coffee': 550,
  'sandwich': 145,
  'tea': 205
}


 # This will create a dictionary for prices
price = {          
  'cake': 2.5,
  'coffee': 3.0,
  'sandwich': 4.0,
  'tea': 2.5
}

# This will calculate total stock worth
total_stock = 0
for item in menu:
  item_value = stock[item] * price[item]
  total_stock += item_value

print("The total stock worth is: ", total_stock)   # Calculate and print the total stock worth