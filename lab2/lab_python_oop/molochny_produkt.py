from .produkt import Produkt


class MolochnyProdukt(Produkt):
    def __init__(self, name, price, expiration_date, weight, fat_content, storage_temp):
        super().__init__(name, price, expiration_date, weight)
        self.fat_content = fat_content
        self.storage_temp = storage_temp

    def get_type_name(self):
        return "Молочный продукт"

    def display_info(self):
        super().display_info()
        print(f"Жирность: {self.fat_content}%")
        print(f"Температура хранения: {self.storage_temp} °C")

    def get_info(self):
        info = super().get_info()
        info.update({
            "Жирность": f"{self.fat_content}%",
            "Темп. хранения": f"{self.storage_temp} °C"
        })
        return info