from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'owner']


class AuthorSerializer(serializers.ModelSerializer):
    # books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    books = serializers.ReadOnlyField(source='books.title')

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'nation', 'books']
