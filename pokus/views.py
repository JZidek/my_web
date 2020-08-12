from django.shortcuts import render
from .models import Zbozi
import datetime
from django.views import generic
from .forms import ZboziKoment

class IndexView(generic.ListView):
    template_name = "pokus/pokus.html"
    context_object_name = "zbozi1"

    def get_queryset(self):
        return Zbozi.objects.all().order_by("-id")

class CreateComment(generic.edit.CreateView):
    form_class = ZboziKoment
    template_name = "pokus/koment.html" 

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form":form})

class DetailView(generic.DetailView):
    model = Zbozi
    template_name = "pokus/detail.html"




    





