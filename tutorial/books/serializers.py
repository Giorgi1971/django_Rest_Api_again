from rest_framework import serializers
from .models import *


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    rating = serializers.IntegerField()
    author = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.added_date = validated_data.get('added_date', instance.added_date)
        instance.author = validated_data.get('author', instance.author)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)
    surname = serializers.CharField(max_length=120)
    nation = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.nation = validated_data.get('nation', instance.nation)
        instance.save()
        return instance


