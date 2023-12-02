from django.urls import path
from . import views

urlpatterns = [
    #Response path.
    path('', views.projects, name="projects"),
    path('project/<str:pk>', views.project, name="project"),
    # Creating Project path 
    path('create-project/', views.createProject, name="create-project"),
    # Updating Project path
    path('update-project/<str:pk>', views.updateProject, name="update-project"),
    # Deleting Project path
    path('delete-project/<str:pk>', views.deleteProject, name="delete-project"),
]