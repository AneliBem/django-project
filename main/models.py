from django.db import models

# клас з розмірною сіткою, 10 символів та розміри унікальні. __str__ для правильного відображення
class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

# клас категорії, 255 символів та моделі унікальні, Створює таблицю в базі даних з полями: id name slug; 
# Meta сортування по імені, призначається індекс для поля name, verbose_name та verbose_name_plural визначають, як модель називатиметься в адмін-панелі 
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ClothingItem(models.Model):
    
