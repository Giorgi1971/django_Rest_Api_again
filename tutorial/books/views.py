from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, renderers
from rest_framework import viewsets

from books.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsSuperUserOrReadOnly]
