from django.db import models
from django.utils.text import slugify

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name="Название игры")
    image = models.ImageField(upload_to='game_images',
                              default='default.jpg',
                              verbose_name="Изображение игры")
    slug = models.SlugField(max_length=200,
                            unique=True,
                            blank=True,
                            verbose_name="URL-метка")
