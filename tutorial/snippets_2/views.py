from tutorial.snippets_2.models import Snippet_2
from tutorial.snippets_2.serializers import SnippetSerializer_2
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippet_2.objects.all()
        serializer = SnippetSerializer_2(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer_2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet_2.objects.get(pk=pk)
    except Snippet_2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer_2(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer_2(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
