class Store:
    def __init__(self, name, list_of_products):
        self.name = name
        self.list_of_products = list_of_products

    def add_product(self, new_product):
        pass

    def sell_product(self, id):
        pass

    def inflation(self, percent_increase):
        pass

    def set_clearance(self, category, percent_discount):
        pass


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= (1 + percent_change)
        elif is_increased == False:
            self.price *= (1 - percent_change)
        else:
            print("Error")
        return self

    def print_info(self):
        print()
        print("Product Info")
        info = self.__dict__
        for key in info:
            print(f"{key}: {info[key]}")
        print()
        return self

product1 = Product("Bananas", 6.00, "food")
product1.print_info().update_price(0.05, True).print_info()