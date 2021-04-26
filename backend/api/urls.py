from django.urls import path
from .views import elastisearch_query

urlpatterns = [path("query/", elastisearch_query)]
