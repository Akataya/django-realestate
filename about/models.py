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