from django.shortcuts import render
from django.views import generic
from .models import Place, Password
from django.urls import reverse, reverse_lazy
# Create your views here.
def home(request):
    return render(request,"core/home.html",{})

class PlaceIndexView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place


class PasswordDetailView(generic.DetailView):
    model = Password

class PlaceCreateView(generic.edit.CreateView):
    model = Place
    fields = '__all__'
    success_url = reverse_lazy("core:index")

class PlaceUpdateView(generic.edit.UpdateView):
    model = Place
    fields = '__all__'
    success_url = reverse_lazy("core:index")

class PlaceDeleteView(generic.edit.DeleteView):
    model = Place
    success_url = reverse_lazy("core:index")
