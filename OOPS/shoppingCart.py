class Shopping_Cart:

    def __init__(self):
        self.cart = []
    
    def adding(self,name,price):
        self.cart.append({'item_name': name , 'price' : price})
        print(f"Added {name} to the cart for ${price}")

    def remove(self,product_name):
        for item in self.cart:
            if item['item_name'] == product_name:
                self.cart.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"Item {product_name} not found in the cart.")
    
    def display_items(self):
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Items in your shopping cart:")
            for item in self.cart:
                print(f"- {item['item_name']}: ${item['price']:.2f}")
    
    def calculate_total(self):
        total = sum(item['price'] for item in self.cart)
        print(f"Total price: ${total:.2f}")
        return total
    
shopcart = Shopping_Cart()

while True:
    print("\n Choose an option")
    print("1. Add item in cart.")
    print("2. Remove item from cart.")
    print("3. Display Total item in cart.")
    print("4. Calculate total item value.")
    print("5. Exit")

    choice = int(input("Enter choice:->"))

    if choice == 1:
        product_name = input("Enter item name:->")
        product_price = int(input("Enter Product price:->"))
        shopcart.adding(product_name,product_price)
    if choice == 2:
        product_name = input("Enter product name that you want to remove:->")
        shopcart.remove(product_name)
    if choice == 3:
        shopcart.display_items()
    if choice == 4:
        shopcart.calculate_total()
    if choice == 5:
        print("Cart close")
        break
    else:   
        print("Opps! Enter valid choice..")