from django.urls import path
from . import views

urlpatterns = [
 #   path('', views.pokus, name = 'pokus'),
    path("zbozi_index/", views.IndexView.as_view(), name = "pokus"),
    path("<int:pk>detail_index/", views.DetailView.as_view(), name="detail"),
 #   path("koment/", views.CreateComment.as_view(), name="komentar"),
]