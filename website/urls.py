from django.urls import path
from .views import index, create


urlpatterns = [
    path('', index , name='homepage'),
    path('create/<int:int>', create , name='createpage'),

]
