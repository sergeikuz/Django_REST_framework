from rest_framework import serializers
from tutorial.snippets_3.models import Snippet_3, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


'''class UserSerializer(serializers.ModelSerializer):
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
        fields = ["id", "title", "code", "linenos", "language", "style", 'owner']'''


class SnippetSerializer_3(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet_3-highlight", format="html"
    )

    class Meta:
        model = Snippet_3
        fields = [
            "url",
            "id",
            "highlight",
            "owner",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet_3-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
