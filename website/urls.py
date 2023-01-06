from django.urls import path
from .views import index, edit


urlpatterns = [
    path('', index , name='homepage'),
    path('edit/<int:int>', edit , name='editpage_id'),


]
