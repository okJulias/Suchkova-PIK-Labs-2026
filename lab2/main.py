from lab_python_oop import Tovar, Igrushka, Produkt, MolochnyProdukt
from tabulate import tabulate


def main():
    goods = [
        Igrushka("Кукла Маша", 599.99, "пластик", 3),
        Produkt("Хлеб", 45.50, "2026-10-12", 500),
        MolochnyProdukt("Молоко", 89.90, "2026-10-15", 1000, 3.2, 4),
        Tovar("Пакет", 5.00),
    ]   

    print("Характеристики экземпляров:\n")
    for item in goods:
        item.display_info()
        print()

    print("Сводная таблица:")
    headers = [
        "Тип", "Название", "Цена",
        "Материал", "Мин. возраст",
        "Срок годности", "Вес",
        "Жирность", "Темп. хранения"
    ]
    rows = []
    for item in goods:
        info = item.get_info()
        rows.append([info.get(h, "") for h in headers])

    print(tabulate(rows, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()