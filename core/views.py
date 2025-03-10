from django.shortcuts import render
from django.views import generic
from .models import Place, Password
from django.urls import reverse, reverse_lazy


# Create your views here.
def home(request):
    return render(request, "core/home.html", {})


class PlaceIndexView(generic.ListView):
    model = Place


class PlaceDetailView(generic.DetailView):
    model = Place


class PasswordDetailView(generic.DetailView):
    model = Password


class PasswordAddView(generic.CreateView):
    model = Password
    fields = "__all__"
    # TODO: I would rather this go back to the place detail page,
    #   but I couldn't figure out how to get that id and pass it to reverse_lazy
    success_url = reverse_lazy("core:index")

    # StackOverflow suggested that I might want to do this
    # but by default the place is included as an option in the form
    # def form_valid(self, form):
    #    form.instance.place = self.request.GET["id"]
    #    return super(PasswordAddView, self).form_valid(form)


class PlaceCreateView(generic.edit.CreateView):
    model = Place
    fields = "__all__"
    success_url = reverse_lazy("core:index")


class PlaceUpdateView(generic.edit.UpdateView):
    model = Place
    fields = "__all__"
    success_url = reverse_lazy("core:index")


class PlaceDeleteView(generic.edit.DeleteView):
    model = Place
    success_url = reverse_lazy("core:index")
