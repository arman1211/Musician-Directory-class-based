from django.urls import path
from . import views

urlpatterns = [
    path("addmusician/",views.MusicianCreateView.as_view(), name='musician'),
    path("",views.MusicianListView.as_view(), name='home'),
    path("edit/<int:pk>",views.MusicianUpdateView.as_view(), name='edit'),
    path("delete/<int:id>",views.MusicianDeleteView.as_view(), name='delete'),
]
