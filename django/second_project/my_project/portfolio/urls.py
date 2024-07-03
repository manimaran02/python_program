from django.urls import path
from . import views





urlpatterns = [
    path('',views.home,name  = "Home"),
    path('project/<int:id>/',views.project,name = "Project")
]