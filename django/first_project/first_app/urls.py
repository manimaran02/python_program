from . import views
from django.urls import path


urlpatterns = [
     path('',views.index),
    path('works/',views.index1),
    path('<name>',views.name),
]