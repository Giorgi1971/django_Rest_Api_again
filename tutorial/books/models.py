from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Book(models.Model):
    title = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='Author', on_delete=models.PROTECT, related_name='author')
    rating = models.IntegerField()

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
