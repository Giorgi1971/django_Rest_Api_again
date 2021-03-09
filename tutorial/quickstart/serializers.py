from django.contrib.auth.models import User, Group
from rest_framework import serializers
from books.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    my_books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', queryset=Book.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    # id = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'my_books', 'snippets']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name']
