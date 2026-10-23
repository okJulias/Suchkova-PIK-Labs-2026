class Tovar:
    """Базовый класс: товар."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_type_name(self):
        """Возвращает название типа. Переопределяется в наследниках."""
        return "Товар"

    def display_info(self):
        print(f"=== {self.get_type_name()} ===")
        print(f"Название: {self.name}")
        print(f"Цена: {self.price:.2f} руб.")

    def get_info(self):
        return {
            "Тип": self.get_type_name(),
            "Название": self.name,
            "Цена": f"{self.price:.2f}"
        }