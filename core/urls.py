from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "core"
urlpatterns = [
    path("", views.PlaceIndexView.as_view(), name="index"),
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),
    path("place/<int:pk>/", views.PlaceDetailView.as_view(), name="place_detail"),
    path(
        "password/<int:pk>/", views.PasswordDetailView.as_view(), name="password_detail"
    ),
    path(
        "password/add/<int:pk>/",
        views.PasswordAddView.as_view(),
        name="add_password",
    ),
    path("place/add", views.PlaceCreateView.as_view(), name="place_add"),
    path(
        "place/update/<int:pk>/", views.PlaceUpdateView.as_view(), name="place_update"
    ),
    path(
        "place/delete/<int:pk>/", views.PlaceDeleteView.as_view(), name="place_delete"
    ),
]
