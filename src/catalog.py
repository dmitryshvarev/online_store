class Product:
    """Класс для представления товара"""
    name: str
    description: str
    price: float
    quantity: int


class Category:
    """Класс для представления категории товаров"""
    name: str
    description: str
    products: list[Product]
