from src.catalog import Product
from src.base_category_order import BaseCategoryOrder


class Order(BaseCategoryOrder):
    """Класс для представления заказа."""

    orders_count = 0

    product: Product
    quantity: int
    total_cost: float

    def __init__(self, product, quantity):
        """Метод для инициализации экземпляра класса."""
        self.product = product
        self.quantity = quantity
        self.total_cost = self.product.price * self.quantity

        Order.orders_count += 1

    def __str__(self):
        """Метод для строкового представления экземпляра класса."""
        return f"Товар: {self.product.name}, количество: {self.quantity} шт., итоговая стоимость: {self.total_cost}"
