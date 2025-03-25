from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "core"
urlpatterns = [
    path("", views.PlaceIndexView.as_view(), name="index"),
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),

    #User Detail
    path("user/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),

    #Place CRUD
    path("place/<int:pk>/", views.PlaceDetailView.as_view(), name="place_detail"),
    path("place/add", views.PlaceCreateView.as_view(), name="place_add"),
    path(
        "place/update/<int:pk>/", views.PlaceUpdateView.as_view(), name="place_update"
    ),
    path(
        "place/delete/<int:pk>/", views.PlaceDeleteView.as_view(), name="place_delete"
    ),

    #Password CRUD
    path(
        "code/<int:pk>/", views.CodeDetailView.as_view(), name="code_detail"
    ),
    path(
        "code/add/<int:pk>/",
        views.CodeAddView.as_view(),
        name="code_add",
    ),
    path(
        "code/update/<int:pk>/", views.CodeUpdateView.as_view(), name="code_update"
    ),
    path(
        "code/delete/<int:pk>/", views.CodeDeleteView.as_view(), name="code_delete"
    ),

    #Comment CRUD
    #I don't think we need a comment_detail view
    path(
        "comment/add/<int:pk>/",
        views.CommentAddView.as_view(),
        name="comment_add",
    ),
    path(
        "comment/update/<int:pk>/", views.CommentUpdateView.as_view(), name="comment_update"
    ),
    path(
        "comment/delete/<int:pk>/", views.CommentDeleteView.as_view(), name="comment_delete"
    ),
    
]
