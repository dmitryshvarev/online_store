class ZeroQuantityError(Exception):
    """Исключение, отвечающее за обработку событий, когда добавляется товар с нулевым количеством."""
    def __init__(self, massage=None):
        super().__init__(massage)
