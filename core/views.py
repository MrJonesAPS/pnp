from django.shortcuts import render
from django.views import generic
from .models import Place, Password, Comment
from django.urls import reverse, reverse_lazy


# Create your views here.
def home(request):
    return render(request, "core/home.html", {})

#######
# Places
#######
class PlaceIndexView(generic.ListView):
    model = Place


class PlaceDetailView(generic.DetailView):
    model = Place

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

########
# Passwords
########
class PasswordDetailView(generic.DetailView):
    model = Password


class PasswordAddView(generic.CreateView):
    model = Password
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})

class PasswordUpdateView(generic.edit.UpdateView):
    model = Password
    fields = "__all__"
    
    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})

class PasswordDeleteView(generic.edit.DeleteView):
    model = Password
    
    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})


########
# Comments
########


class CommentAddView(generic.CreateView):
    model = Comment
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("core:password_detail", kwargs={"pk": self.object.password.id})

class CommentUpdateView(generic.edit.UpdateView):
    model = Comment
    fields = "__all__"
    
    def get_success_url(self):
        return reverse_lazy("core:password_detail", kwargs={"pk": self.object.password.id})

class CommentDeleteView(generic.edit.DeleteView):
    model = Comment
    
    def get_success_url(self):
        return reverse_lazy("core:password_detail", kwargs={"pk": self.object.password.id})
