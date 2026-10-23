from .tovar import Tovar


class Igrushka(Tovar):
    def __init__(self, name, price, material, min_age):
        super().__init__(name, price)
        self.material = material
        self.min_age = min_age

    def get_type_name(self):
        return "Игрушка"

    def display_info(self):
        super().display_info()
        print(f"Материал: {self.material}")
        print(f"Минимальный возраст: {self.min_age}+")

    def get_info(self):
        info = super().get_info()
        info.update({
            "Материал": self.material,
            "Мин. возраст": f"{self.min_age}+"
        })
        return info