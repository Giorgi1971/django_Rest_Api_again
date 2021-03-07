from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to='Author', on_delete=models.PROTECT, related_name='books')
    owner = models.ForeignKey('auth.User', related_name='my_books', on_delete=models.CASCADE)
    highlighted = models.TextField()
    price = models.SmallIntegerField(default=5)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    nation = models.CharField(max_length=24)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.surname}'
