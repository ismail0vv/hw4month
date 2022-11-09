from django.db import models


# Create your models here.
class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
    name = models.CharField(max_length=100, verbose_name='Имя')

    def __str__(self):
        return self.name


class Film(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    director = models.ForeignKey(Director, on_delete=models.SET_NULL,
                                 related_name='film_list_on_director', null=True, verbose_name='Режиссер')
    title = models.CharField(max_length=255, verbose_name='Название')
    producer = models.CharField(max_length=255, verbose_name='Продюсер')
    rating = models.FloatField(blank=True, null=True, verbose_name='Рейтинг')
    duration = models.FloatField(default=0, verbose_name='Длительность')

    def __str__(self):
        return self.title
