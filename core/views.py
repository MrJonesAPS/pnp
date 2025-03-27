from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Place, Code, Comment, Vote
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from core.owner import OwnerCreateView, OwnerDeleteView, OwnerDetailView, OwnerListView, OwnerDeleteView, OwnerUpdateView


# Create your views here.
def home(request):
    return render(request, "core/home.html", {})


#######
# User Detail
#######
class UserDetailView(generic.DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Change the name of the user context variable here
        context['profile_user'] = context.pop('user')
        return context


#######
# Places
#######
class PlaceIndexView(generic.ListView):
    model = Place


class PlaceDetailView(generic.DetailView):
    model = Place

class PlaceCreateView(OwnerCreateView):
    model = Place
    fields = ['name','long','lat']
    success_url = reverse_lazy("core:index")


class PlaceUpdateView(OwnerUpdateView):
    model = Place
    fields = ['name','long','lat']
    success_url = reverse_lazy("core:index")

class PlaceDeleteView(OwnerDeleteView):
    model = Place
    success_url = reverse_lazy("core:index")

########
# Codes
########
class CodeDetailView(generic.DetailView):
    model = Code

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_code = context["code"]
        context["num_yes_votes"] = Vote.objects.filter(code=this_code).filter(worked=True).count()
        context["num_no_votes"] = Vote.objects.filter(code=this_code).filter(worked=False).count()
        return context

class CodeAddView(OwnerCreateView):
    model = Code
    fields = ['value','code_type']

    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})

    def form_valid(self, form):
        form.instance.place_id = self.kwargs.get('pk')
        return super(CodeAddView, self).form_valid(form)

class CodeUpdateView(OwnerUpdateView):
    model = Code
    fields = ['value','code_type']
    
    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})
    
    #we don't need to do the form_valid thing here. It'll just keep the existing foreign key id

class CodeDeleteView(OwnerDeleteView):
    model = Code
    
    def get_success_url(self):
        return reverse_lazy("core:place_detail", kwargs={"pk": self.object.place.id})


########
# Votes
########
class WorkedView(OwnerCreateView):
    model = Vote
    fields = []
    template_name = 'core/code_worked.html'

    def get_success_url(self):
        return reverse_lazy("core:code_detail", kwargs={"pk": self.object.code.id})

    def form_valid(self, form):
        form.instance.code_id = self.kwargs.get('pk')
        form.instance.worked=True
        return super(WorkedView, self).form_valid(form)

class NotWorkedView(OwnerCreateView):
    model = Vote
    fields = []
    template_name = 'core/code_not.html'

    def get_success_url(self):
        return reverse_lazy("core:code_detail", kwargs={"pk": self.object.code.id})

    def form_valid(self, form):
        form.instance.code_id = self.kwargs.get('pk')
        form.instance.worked=False
        return super(NotWorkedView, self).form_valid(form)

########
# Comments
########


class CommentAddView(OwnerCreateView):
    model = Comment
    fields = ['text']

    def get_success_url(self):
        return reverse_lazy("core:code_detail", kwargs={"pk": self.object.code.id})

    def form_valid(self, form):
        form.instance.code_id = self.kwargs.get('pk')
        return super(CommentAddView, self).form_valid(form)


class CommentUpdateView(OwnerUpdateView):
    model = Comment
    fields = ['text']
    
    def get_success_url(self):
        return reverse_lazy("core:code_detail", kwargs={"pk": self.object.code.id})


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    
    def get_success_url(self):
        return reverse_lazy("core:code_detail", kwargs={"pk": self.object.code.id})
