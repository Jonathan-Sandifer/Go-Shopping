from django.urls import path

from projects.views import (
    ProjectListView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="home"),
    path("<int:pk>/", Task.as_view(), name="show_project"),
]
