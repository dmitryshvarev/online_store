import pytest


def test_smartphone_init(smartphone_1):
    """Проверяет правильность инициализации классa Smartphone."""
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_lawn_grass_init(lawn_grass_1):
    """Проверяет правильность инициализации классa LawnGrass."""
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_add_success(smartphone_1, smartphone_2):
    """Проверяет работу магического метода __add__."""
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_add_error(smartphone_1, lawn_grass_1):
    with pytest.raises(TypeError) as exc_info:
        smartphone_1 + lawn_grass_1
    assert str(exc_info.value) == "Складываться могут только товары одного класса"
