from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Название продукта', max_length=50)
    price = models.FloatField('Цена')
    description = models.TextField('Описание')
    count = models.IntegerField('Количество')
    is_active = models.BooleanField('Активность')

    def __str__(self):
        return self.name, self.price, self.description, self.count, self.is_active
        

class Category(models.Model):
    name = models.CharField('Название категории' , max_length =  50)

    def __str__(self):
        return self.name