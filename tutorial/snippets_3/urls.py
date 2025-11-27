from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial.snippets_3 import views


urlpatterns = [
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

urlpatterns = format_suffix_patterns(urlpatterns)
