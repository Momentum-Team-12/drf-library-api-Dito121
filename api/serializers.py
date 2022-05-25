from rest_framework import serializers
from .models import Book, LANGUAGE_CHOICES, STYLE_CHOICES


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'linenos',
            'language',
            'style',
        )
