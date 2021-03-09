from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    # author = serializers.ReadOnlyField(source='author.surname')
    author = serializers.HyperlinkedRelatedField(
        view_name='author-detail',  # სახელის მიხედვით იღებს ურლ-ს
        queryset=Author.objects.all().filter(nation='Georgian')  # წიგნის შექმნისას, რა ჩამონათვალი გამოიტანოს,
        # read_only=True -ზე ველს საერთოდ არ გამოიტანს ქვევით create-ში.
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'owner']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'nation', 'books']
