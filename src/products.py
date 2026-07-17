from src.catalog import Product


class Smartphone(Product):
    """Класс для представления смартфонов."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод для инициализации экземпляра класса."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
