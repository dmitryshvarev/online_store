class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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


