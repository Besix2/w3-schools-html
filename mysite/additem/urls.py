from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('additem/', views.additem, name='additem'),
    path('update-db/', views.update_db, name='update_db')
]
