from django.db import models

# Create your models here.


class Club(models.Model):
    class Meta:

        verbose_name_plural = 'Clubs'

    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, unique=True)
    sport = models.CharField(max_length=60, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):

        return f'{self.name}'

    def get_friendly_name(self):

        return self.friendly_name
