# exercise_1
# The function is not pure because it contains `cart.append(item)`,
#  which modifies the global `cart` variable.


# exercise_2
total = 0
 
def add_price(total, price):
    total += price
    return total
total = 0
total = add_price(total, 10)
total = add_price(total, 10)
print(total)
 
print(add_price(0, 10))
print(add_price(0, 10))


# exercise_3
TAX = 1.17
def apply_tax(prices):
    result=[]   
    for i in range(len(prices)):
        result.append ( prices[i] * TAX)
    return result 


prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)
