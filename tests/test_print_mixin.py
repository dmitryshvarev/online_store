from src.catalog import Product
from src.products import LawnGrass, Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
