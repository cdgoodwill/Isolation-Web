from django.urls import path

from .views import index, data, place

urlpatterns = [
    path('', index.index, name='index'),
    path('data', data.render_data, name='data'),
    path('place/<uuid:pk>', place.EditPlaceView.as_view()),
    path('edit_place', place.edit_place, name="edit_place"),
]
