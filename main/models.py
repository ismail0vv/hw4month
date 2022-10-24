from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Film(models.Model):
    director = models.ForeignKey(Director, on_delete=models.SET_NULL,
                                 related_name='film_list_on_director', null=True)
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    rating = models.FloatField(blank=True, null=True)
    duration = models.FloatField(default=0)

    def __str__(self):
        return self.title
