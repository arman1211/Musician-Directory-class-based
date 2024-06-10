
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import MusicianModel
from .forms import MusicianForm

class MusicianCreateView(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

class MusicianListView(ListView):
    model = MusicianModel
    template_name = 'home.html'
    context_object_name = 'musicians'

class MusicianUpdateView(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')

class MusicianDeleteView(DeleteView):
    model = MusicianModel
    template_name = 'confirm_delete.html'  
    success_url = reverse_lazy('home')

    def get_object(self):
        id = self.kwargs.get("id")
        return MusicianModel.objects.get(pk=id)
