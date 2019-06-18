from django.db import models


class About(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self):
        return str(self.id)


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    icon = models.CharField(max_length=150)

    def __str__(self):
        return str(self.title)
