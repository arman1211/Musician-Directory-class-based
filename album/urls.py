from django.urls import path
from . import views

urlpatterns = [
    path("",views.AddAlbumView.as_view(),name='album'),
    path('editalbum/<int:pk>', views.EditAlbumView.as_view(),name='editalbum')
]
