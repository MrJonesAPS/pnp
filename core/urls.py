from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "core"
urlpatterns = [
    path("", views.PlaceIndexView.as_view(), name="index"),
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),

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
        "password/<int:pk>/", views.PasswordDetailView.as_view(), name="password_detail"
    ),
    path(
        "password/add/<int:pk>/",
        views.PasswordAddView.as_view(),
        name="password_add",
    ),
    path(
        "password/update/<int:pk>/", views.PasswordUpdateView.as_view(), name="password_update"
    ),
    path(
        "password/delete/<int:pk>/", views.PasswordDeleteView.as_view(), name="password_delete"
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
