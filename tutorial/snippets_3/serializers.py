from rest_framework import serializers
from tutorial.snippets_3.models import Snippet_3, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer_3(serializers.ModelSerializer):
    class Meta:
        model = Snippet_3
        fields = ["id", "title", "code", "linenos", "language", "style"]

