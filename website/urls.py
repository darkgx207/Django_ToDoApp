from django.urls import path
from .views import index, edit, create


urlpatterns = [
    path('', index , name='homepage'),
    path('edit/<int:int>', edit , name='editpage_id'),
    path('create/', create , name= 'createpage'),

]
