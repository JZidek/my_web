from django.urls import path
from . import views
from . import url_handlers

urlpatterns = [
    path("film_index", views.FilmIndex.as_view(), name = "filmovy_index"),
    path("<int:pk>film_detail", views.FilmDetail.as_view(), name = "filmovy_detail"),
    path("create_film", views.CreateFilm.as_view(), name = "novy_film"),
    path("", url_handlers.index_handler)
]