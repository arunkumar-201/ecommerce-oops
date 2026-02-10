class Order:
    delivery_charges = {
        "Normal": 0,
        "Prime_Delivery": 100
    }

    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address

    def add_items(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)

    def display_delivery_details(self):
        print("Delivery method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Products")
        print("---------------------")

        for products, quantity in self.items_in_cart:
            products.display_product_details()
            print("Quantity: {}".format(quantity))
            print("")

        print("---------------------")
        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))

    def get_total_bill(self):
        total_bill = 0
        for products, quantity in self.items_in_cart:
            total_bill += products.get_deal_price() * quantity

        order_delivery_charges = Order.delivery_charges[self.delivery_method]  # fixed spelling
        total_bill = total_bill + order_delivery_charges
        return total_bill

    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):  # fixed spelling
        cls.delivery_charges[delivery_method] = charges
