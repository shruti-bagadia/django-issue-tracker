from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("projects/new/", views.project_create, name="project_create"),
    path("issues/new/", views.issue_create, name="issue_create"),


]
