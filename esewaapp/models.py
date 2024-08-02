from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, verbose_name='Product Name')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  

    def __str__(self):
        return self.name
