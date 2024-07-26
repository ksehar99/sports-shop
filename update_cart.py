from tkinter import messagebox


class UpdateCart:
    def __init__(self):
        self.cart = {}

    def product_list(self):
        products = [
            ['Helmet', 2000], ['Shoes', 4000], ['Jersey', 1800], ['Ball', 600], ['Bat', 1200],
            ['Football', 1500], ['Football Jersey', 1800], ['Football shoes', 3500], ['Football nets', 2500],
            ['Football T-Shirt', 1500],
            ['Basketball', 2000], ['Crew socks', 500], ['Shooter sleeves', 800], ['Backpack', 2500],
            ['Skinny hairband', 300],
            ['Baseball Cleats', 3500], ['Baseball leg guards', 1500], ['Baseball chest protector', 2000],
            ['Baseball T-shirt', 1200], ['Baseball bat', 2500],
            ['Soccer Cleats', 3000], ['Soccer Shoes', 2800], ['Soccer pants', 1500], ['Soccer T-Shirt', 1000],
            ['Soccer ball', 700],
            ['Tennis ball', 600], ['Tennis T-shirt', 1200], ['Tennis shoes', 3500], ['Tennis rackets', 4500],
            ['Tennis P-cap', 500],
            ['Hockey Jersey', 1800], ['Hockey Hat', 400], ['Hockey Stick', 3000], ['Hockey ball', 600],
            ['Hockey shoes', 3500],
            ['T-shirts', 1200], ['Shorts', 800], ['Jackets', 2500], ['Hoodie', 2000], ['Cleats', 3000]
        ]
        return products

    def increase(self, var, product):
        if product not in self.cart:
            self.cart[product] = 1
        else:
            if self.cart[product] < 50:
                self.cart[product] += 1
            else:
                messagebox.showerror("Error", f"sorry! currently we don't have {self.cart[product]} {product}")
        var.set(self.cart[product])

    def decrease(self, var, product):
        if product in self.cart and self.cart[product] > 0:
            self.cart[product] -= 1

            if self.cart[product] == 0:
                del self.cart[product]

        if product in self.cart:
            var.set(self.cart[product])
        else:
            var.set(0)

    def save_cart(self):
        with open('temporary_cart.txt', 'w') as file:
            for product, quantity in self.cart.items():
                file.write(f"{product},{quantity}\n")
