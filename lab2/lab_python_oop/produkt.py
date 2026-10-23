from .tovar import Tovar


class Produkt(Tovar):
    def __init__(self, name, price, expiration_date, weight):
        super().__init__(name, price)
        self.expiration_date = expiration_date
        self.weight = weight

    def get_type_name(self):
        return "Продукт"

    def display_info(self):
        super().display_info()
        print(f"Срок годности: {self.expiration_date}")
        print(f"Вес: {self.weight} г")

    def get_info(self):
        info = super().get_info()
        info.update({
            "Срок годности": self.expiration_date,
            "Вес": f"{self.weight} г"
        })
        return info