from tutorial.snippets_3.models import Snippet_3
from tutorial.snippets_3.serializers import SnippetSerializer_3, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from tutorial.snippets_3.permissions import IsOwnerOrReadOnly

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
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet_3.objects.all()
    serializer_class = SnippetSerializer_3
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

