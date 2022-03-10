from django.db import models


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата заявки')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    OPTIONS = [
        ("1", "Пакет 1"),
        ("2", "Пакет 2"),
        ("3", "Пакет 3"),
    ]
    order_choice = models.CharField(max_length=20, choices=OPTIONS, default="1", verbose_name="Пакет")

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
