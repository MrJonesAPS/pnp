from django.shortcuts import render
from django.views import generic
from .models import Place, Password

# Create your views here.
def home(request):
    return render(request,"core/home.html",{})

class PlaceIndexView(generic.ListView):
    model = Place

class PlaceDetailView(generic.DetailView):
    model = Place


class PasswordDetailView(generic.DetailView):
    model = Password
