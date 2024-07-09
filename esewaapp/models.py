from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',default='Images')
    price = models.IntegerField()

    def __str__(self):
        return self.title

