import unittest
from lab_python_oop import Tovar, Igrushka, Produkt, MolochnyProdukt

class TestGoods(unittest.TestCase):

    def test_tovar_creation(self):
        """Проверяем базовый класс Товар"""
        t = Tovar("Пакет", 5.0)
        self.assertEqual(t.name, "Пакет")
        self.assertEqual(t.price, 5.0)
        self.assertEqual(t.get_type_name(), "Товар")

    def test_igrushka_creation(self):
        """Проверяем класс Игрушка и его специфичные поля"""
        i = Igrushka("Кукла", 100.0, "пластик", 3)
        self.assertEqual(i.name, "Кукла")
        self.assertEqual(i.material, "пластик") # Проверка специфичного поля
        self.assertEqual(i.get_type_name(), "Игрушка")

    def test_molochny_produkt_creation(self):
        """Проверяем цепочку наследования (Молочный -> Продукт -> Товар)"""
        m = MolochnyProdukt("Молоко", 80.0, "2026-10-15", 1000, 3.2, 4)
        self.assertEqual(m.name, "Молоко")           # Из Товара
        self.assertEqual(m.expiration_date, "2026-10-15") # Из Продукта
        self.assertEqual(m.fat_content, 3.2)         # Из Молочного
        self.assertEqual(m.get_type_name(), "Молочный продукт")

    def test_get_info_dict(self):
        """Проверяем, что get_info() возвращает словарь с нужными ключами"""
        p = Produkt("Хлеб", 40.0, "2026-10-12", 500)
        info = p.get_info()
        
        # Проверяем, что в словаре есть ключи 'Тип', 'Название' и 'Вес'
        self.assertIn("Тип", info)
        self.assertIn("Название", info)
        self.assertIn("Вес", info)
        self.assertEqual(info["Тип"], "Продукт")

if __name__ == '__main__':
    unittest.main()