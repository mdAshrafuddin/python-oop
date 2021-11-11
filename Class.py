class Item:
    def __init__(self, name, price, quantity):
        # Run valitation to the received arguments
        assert price > 0, f"Price {price} is not greater than or equal to zero"
        assert quantity > 0, f"Quantity {quantity} is not greater or equal to zero"
        # Assing slef value
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item('Ashraf', 100, -5)
item2 = Item("Tanjil", 300, -7)

print(item1.name)
print(item1.price)
print(item1.quantity)

print(item2.name)
print(item2.price)
print(item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())



