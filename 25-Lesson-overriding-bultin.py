class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer  = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        return count * 2

shopping = Shopping(['AShraf', 'Tanjil'], 'as')
print(len(shopping))