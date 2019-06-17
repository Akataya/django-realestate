from django.db import models

property_type = (
    ('Sale', 'sale'),
    ('Rent', 'rent')
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    property_type = models.CharField(choices=property_type, max_length=10)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property/', null=True, blank=True)

    # location

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Reserve(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.name
