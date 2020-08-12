from django.shortcuts import render
from django.views import generic
from .forms import FilmForm
from .models import Film

class FilmIndex(generic.ListView):
    template_name = "moviebook/film_index.html"
    context_object_name = "filmy"

    def get_queryset(self):
        return Film.objects.all().order_by("-id")

class FilmDetail(generic.DetailView):
    model = Film
    template_name = "moviebook/film_detail.html"

class CreateFilm(generic.edit.CreateView):

    form_class = FilmForm
    template_name = "moviebook/create_film.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit = True)
        return render(request, self.template_name, {"form":form})