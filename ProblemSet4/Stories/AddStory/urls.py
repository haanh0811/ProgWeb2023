from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/', views.add, name='add'),
    path('addentry/', views.addentry, name='addentry'),
    path('entry/<int:id>/', views.entry, name='entry')
]