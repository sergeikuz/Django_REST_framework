from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tutorial.snippets_2 import views


urlpatterns = [
    path("snippets_2/", views.snippet_list),
    path("snippets_2/<int:pk>/", views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
