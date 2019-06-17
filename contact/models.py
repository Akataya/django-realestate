from django.db import models


class ContactDetails(models.Model):
    # location =
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'contact details'
        verbose_name_plural = 'contact details'

    def __str__(self):
        return str(self.id)
