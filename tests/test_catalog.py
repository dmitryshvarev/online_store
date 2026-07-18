import pytest

from src.catalog import Category, Product


def test_products_and_categories_count(category_smartphone, category_tv):
    """Проверяет подсчет количества продуктов и категорий."""
    assert Category.products_count == 4
    assert category_smartphone.products_count == 4
    assert category_tv.products_count == 4

    assert Category.categories_count == 2
    assert category_smartphone.categories_count == 2
    assert category_tv.categories_count == 2


def test_product_init(product_samsung, product_iphone, product_xiaomi, product_qled):
    """Проверяет правильность инициализации классa Product."""
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5

    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8

    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14

    assert product_qled.name == '55" QLED 4K'
    assert product_qled.description == "Фоновая подсветка"
    assert product_qled.price == 123000.0
    assert product_qled.quantity == 7


def test_product_str(product_samsung, product_iphone, product_xiaomi, product_qled):
    """Проверяет работу магического метода __str__ классa Product."""
    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."
    assert str(product_iphone) == "Iphone 15, 210000 руб. Остаток: 8 шт."
    assert str(product_xiaomi) == "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт."
    assert str(product_qled) == '55" QLED 4K, 123000 руб. Остаток: 7 шт.'


def test_product_add(product_samsung, product_iphone):
    assert product_samsung + product_iphone == 2580000.0


def test_category_init(
    category_smartphone, category_tv, product_samsung, product_iphone, product_xiaomi, product_qled
):
    """Проверяет правильность инициализации классa Category."""
    assert category_smartphone.name == "Смартфоны"
    assert (
        category_smartphone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smartphone.products == """Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.\n"""
    # assert category_smartphone.products == [product_samsung, product_iphone, product_xiaomi]

    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_tv.products == '55" QLED 4K, 123000 руб. Остаток: 7 шт.\n'
    # assert category_tv.products == [product_qled]


def test_category_str(category_smartphone, category_tv):
    """Проверяет работу магического метода __str__ классa Category."""
    assert str(category_smartphone) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category_tv) == "Телевизоры, количество продуктов: 7 шт."


def test_new_product(product_dict):
    """Проверяет класс-метод для создания или обновления экземпляра класса Product"""
    product_cls = Product.new_product(product_dict)
    assert product_cls.name == "Samsung Galaxy S23 Ultra"
    assert product_cls.description == "256GB, Серый цвет, 200MP камера"
    assert product_cls.price == 180000.0
    assert product_cls.quantity == 5


def test_new_product_existing_products(product_dict, product_samsung, product_iphone):
    product_cls_1 = Product.new_product(product_dict, [product_samsung, product_iphone])
    product_cls_2 = Product.new_product(product_dict, [product_iphone])
    assert product_cls_1.quantity == 10
    assert product_cls_2.quantity == 5


def test_price_getter(product_samsung):
    assert product_samsung.price == 180000.0


def test_price_setter(product_samsung):
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0


def test_price_less_or_equal_zero(product_samsung, capsys):
    product_samsung.price = -100
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product_samsung.price == 180000.0

    product_samsung.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert product_samsung.price == 180000.0


def test_price_setter_ignore_drop(product_samsung, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product_samsung.price = 100
    assert product_samsung.price == 180000.0


def test_price_setter_accept_drop(product_samsung, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product_samsung.price = 100
    assert product_samsung.price == 100


def test_add_product(category_tv, product_samsung):
    category_tv.add_product(product_samsung)
    assert (
        category_tv.products
        == '55" QLED 4K, 123000 руб. Остаток: 7 шт.\nSamsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n'
    )


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_add_product_error(category_tv):
    with pytest.raises(TypeError) as exc_info:
        category_tv.add_product(1)
    assert str(exc_info.value) == "Можно добавлять только экземпляры класса Product и производных от него"


def test_middle_price(category_smartphone, category_without_products):
    assert category_smartphone.middle_price() == 140333
    assert category_without_products.middle_price() == 0


def test_add_product_without_quantity(capsys, category_smartphone, product_without_quantity):
    assert len(category_smartphone) == 3

    category_smartphone.add_product(product_without_quantity)
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-2] == "Товар с нулевым количеством не может быть добавлен"
    assert massage.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    assert len(category_smartphone) == 3


def test_add_product_with_quantity(capsys, category_smartphone, product_iphone):
    assert len(category_smartphone) == 3

    category_smartphone.add_product(product_iphone)
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert massage.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    assert len(category_smartphone) == 4


def test_product_init_error():
    with pytest.raises(ValueError) as exc_info:
        Product("Iphone 15", "512GB, Gray space", 210000.0, -1)
    assert str(exc_info.value) == "Товар с отрицательным количеством не может быть добавлен"
