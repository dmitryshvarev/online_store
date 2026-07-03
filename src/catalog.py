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

    @classmethod
    def new_product(cls, product: dict):
        """Возвращает экземпляр класса Product на основе данных словаря."""
        return cls(product.get("name"), product.get("description"), product.get("price"), product.get("quantity"))


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
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.products)
