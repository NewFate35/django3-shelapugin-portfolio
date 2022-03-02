from django.db import models


class Achievements(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="achievements/images/", verbose_name='Изображение')
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title

