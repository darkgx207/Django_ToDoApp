from django.urls import path
from .views import index, api


urlpatterns = [
    path('', index , name='homepage'),
    path('api', api , name='apipage')

]
