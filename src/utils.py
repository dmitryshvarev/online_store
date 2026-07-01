import json
import logging

from src.catalog import Category, Product

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def creates_objects_from_json(path: str = "../data/products.json") -> list[Category]:
    """Читает файл JSON и создает объекты классов."""
    products_data = []
    try:
        with open(path, "r", encoding="utf-8") as products_file:
            logger.info(f'Файл "{path}" успешно загружен')
            try:
                products_data = json.load(products_file)
                logger.info(f'Данные из файла "{path}" преобразованы в объект Python')
            except json.JSONDecodeError:
                logger.error(f'Ошибка декодирования файла "{path}"')
    except FileNotFoundError:
        logger.error(f'Файл "{path}" не найден')

    categories_list = []
    for category in products_data:
        products_list = []
        for product in category.get("products"):
            products_list.append(
                Product(product.get("name"), product.get("description"), product.get("price"), product.get("quantity"))
            )
        categories_list.append(Category(category.get("name"), category.get("description"), products_list))

    return categories_list


if __name__ == "__main__":
    print(creates_objects_from_json()[0].name == "Смартфоны")
