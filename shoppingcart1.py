# shopping cart and bill

n=int(input("Enter the no of items in cart: ")) 
cart=[["Item", "costPerItem"]]
for i in range(n):
    c=[]
    Item=input("Enter the item name:")
    cost_per_item=float(input("Enter the cost of this item:"))
    c.append(Item)
    c.append(cost_per_item)
    cart.append(c)
print("Cart: \n", cart)

# daughter's cart

dc=[["item", "quantity"]] 
m=int (input("Enter the no of items purchased:"))
for i in range (m):
    d=[]
    item=input("Enter the item purchased: ")
    no_of_item=int (input("Enter count of the item: ")) 
    d.append(item) 
    d.append(no_of_item) 
print("Daughter's cart: \n", dc)