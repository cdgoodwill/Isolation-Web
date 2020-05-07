from django.urls import path

from .views import index, data

urlpatterns = [
    path('', index.index, name='index'),
    path('data', data.render_data, name='data'),
]
