from tutorial.snippets_3.models import Snippet_3
from tutorial.snippets_3.serializers import SnippetSerializer_3, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from tutorial.snippets_3.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet_3-list", request=request, format=format),
        }
    )


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet_3.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet_3.objects.all()
    serializer_class = SnippetSerializer_3
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        context = self.get_serializer_context()

        serializer = self.get_serializer(
            data=self.request.data,
            context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet_3.objects.all()
    serializer_class = SnippetSerializer_3
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        context = self.get_serializer_context()

        serializer = self.get_serializer(
            data=self.request.data,
            context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)


