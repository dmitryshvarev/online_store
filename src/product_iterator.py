from src.catalog import Category


class ProductIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории."""
    category: Category
    index: int

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category):
            product_ = self.category.products_in_list[self.index]
            self.index += 1
            return product_
        else:
            raise StopIteration
