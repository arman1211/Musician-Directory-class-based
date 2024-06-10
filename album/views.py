from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from . import forms,models

# Create your views here.

class AddAlbumView(CreateView):
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('musician')
    def form_valid(self, form):
        return super().form_valid(form)
    

class EditAlbumView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')
