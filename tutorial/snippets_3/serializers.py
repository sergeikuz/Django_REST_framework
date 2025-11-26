from rest_framework import serializers
from tutorial.snippets_3.models import Snippet_3, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet_3.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]


class SnippetSerializer_3(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet_3
        fields = ["id", "title", "code", "linenos", "language", "style", 'owner']
