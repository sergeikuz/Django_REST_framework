from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial.snippets_3 import views
from rest_framework import renderers

from tutorial.snippets_3.views import api_root, SnippetViewSet, UserViewSet

'''urlpatterns = [
    path("", views.api_root),
    path("snippets_3/<int:pk>/highlight/", views.SnippetHighlight.as_view()),
    path("snippets_3/", views.SnippetList.as_view(), name="snippet_3-list"),
    path("snippets_3/<int:pk>/", views.SnippetDetail.as_view(), name="snippet_3-detail"
    ),
    path(
        "snippets_3/<int:pk>/highlight/",
        views.SnippetHighlight.as_view(),
        name="snippet_3-highlight",
    ),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)'''

'''
snippet_3_list = SnippetViewSet.as_view({"get": "list", "post": "create"})
snippet_3_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)
snippet_3_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)
user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})


urlpatterns = format_suffix_patterns(
    [
        path("", api_root),
        path("snippets_3/", snippet_3_list, name="snippet_3-list"),
        path("snippets_3/<int:pk>/", snippet_3_detail, name="snippet_3-detail"),
        path(
            "snippets_3/<int:pk>/highlight/", snippet_3_highlight, name="snippet_3-highlight"
        ),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>/", user_detail, name="user-detail"),
    ]
)'''

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tutorial.snippets_3 import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"snippets_3", views.SnippetViewSet, basename="snippet_3")
router.register(r"users", views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]