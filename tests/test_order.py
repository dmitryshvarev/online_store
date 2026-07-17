def test_order_init(order_iphone, product_iphone):
    """Проверяет правильность инициализации классa Order."""
    assert order_iphone.product == product_iphone
    assert order_iphone.quantity == 2
    assert order_iphone.total_cost == 420000.0


def test_order_str(order_iphone):
    """Проверяет работу магического метода __str__ классa Order."""
    assert str(order_iphone) == "Товар: Iphone 15, количество: 2 шт., итоговая стоимость: 420000.0"
