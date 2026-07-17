from abc import ABC, abstractmethod


class BaseCategoryOrder(ABC):
    """<Базовый абстрактный класс, являющийся родительским для классов категорий и заказов."""

    @abstractmethod
    def __str__(self):
        pass
