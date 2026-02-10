class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("ratings: {}".format(self.ratings))
        print("you_saved: {}".format(self.you_saved))

    def get_deal_price(self):
        return self.deal_price


class Electronic_items(Product):   # fixed spelling
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    def display_product_details(self):
        super().display_product_details()
        print("Warranty : {} months".format(self.warranty_in_months))


class Grocery_items(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("expiry Date : {}".format(self.expiry_date))


class Laptop(Electronic_items):
    def __init__(self, name, price, deal_price, ratings,
                 warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.ram = ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()
        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))
