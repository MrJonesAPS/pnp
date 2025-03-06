from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "core"
urlpatterns = [
    path("", views.PlaceIndexView.as_view(),name="index"),
    path("place/<int:pk>/", views.PlaceDetailView.as_view(),name="place_detail"),
    path("password/<int:pk>/", views.PasswordDetailView.as_view(),name="password_detail"),
]

