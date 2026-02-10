from product import Grocery_items, Electronic_items, Laptop
from order import Order

milk = Grocery_items("Milk", 80, 70, 5.0, "jan-13")
tv = Electronic_items("Tv", 40000, 24000, 5.0, 12)

my_order = Order("Normal", "Vizag")
my_order.add_items(tv, 1)
my_order.add_items(milk, 3)

my_order.display_delivery_details()

Order.update_delivery_charges("Normal", 100)
my_order.display_delivery_details()

asus_laptop = Laptop("Asus A15s", 100000, 85000, 5.0, 24, "16 GB", "550 SSD")
asus_laptop.display_product_details()
