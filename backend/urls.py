from django.contrib import admin
from django.urls import path

from backend.views import index, simple_api_view

urlpatterns = [
    path('', index, name='index'),
    path('api/phrases/', simple_api_view, name='phrases'),
    path('admin/', admin.site.urls),
]
