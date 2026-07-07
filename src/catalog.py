class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict, existing_products=None):
        """Класс-метод для создания или обновления товара на основе словаря."""
        name = product_dict.get("name")
        description = product_dict.get("description")
        price = product_dict.get("price", 0)
        quantity = product_dict.get("quantity", 0)

        if existing_products:
            for product in existing_products:
                if name.lower() == product.name.lower():
                    best_price = max(price, product.price)
                    total_quantity = quantity + product.quantity

                    product.price = best_price
                    product.quantity = total_quantity

                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                price_drop = input("\nСогласны ли Вы на снижение цены? (y/n)  ")
                if price_drop.lower() != "y":
                    return
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс для представления категории товаров."""

    categories_count = 0
    products_count = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.__products = products

        Category.categories_count += 1
        Category.products_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в атрибут products."""
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.\n"
        return products_str
