class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        existing_dict = {}

        for product in existing_products:
            if product:
                name, weight, category = product.split(', ')
                existing_dict[(name, category)] = float(weight)

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for product in products:
                key = (product.name, product.category)
                if key in existing_dict:
                    existing_dict[key] += product.weight
                    print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_dict[key]}")
                else:
                    existing_dict[key] = product.weight

            for (name, category), weight in existing_dict.items():
                file.write(f"{name}, {weight}, {category}\n")
