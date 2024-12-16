# title, author, and price. Include a method to apply a discount to the price.

class Books:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self,discount_percent):
        discount_amount = (self.price * discount_percent) / 100

        self.price -= discount_amount
        print(f"Discount applied: {discount_percent}%. New price is: {self.price}")
    
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")


book = Books("The Great Gatsby", "F. Scott Fitzgerald", 15.99)


book.display_info()        
book.apply_discount(20)
