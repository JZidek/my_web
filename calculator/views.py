from django.shortcuts import render
from . import model


def kalkulacka(request):
    error_msg = "None"
    vysledek = "Ahoj"
    if request.method == 'POST':
        try:
            float(request.POST['a'])
            float(request.POST['b'])
        except:
            error_msg = 'A nebo B neni cislo'
            return render(request, 'calculator/kalkulacka.html', dict(error_msg = error_msg, vysledek = vysledek))
        if (float(request.POST['b'] == 0) and (request.POST['operator'] == '/')):
            error_msg = 'nelze delit nulou'
            return render(request, 'calculator/kalkulacka.html', dict(error_msg = error_msg, vysledek = vysledek))
        elif request.POST['operator'] == '+':
            vysledek = model.secti(request.POST['a'], request.POST['b'])
        elif request.POST['operator'] == '-':
            vysledek = model.odecti(request.POST['a'], request.POST['b'])
        elif request.POST['operator'] == '*':
            vysledek = model.vynasob(request.POST['a'], request.POST['b'])
        elif request.POST['operator'] == '/':
            vysledek = model.vydel(request.POST['a'], request.POST['b'])
        else:
            error_msg = 'neco se pokazilo'
            return render(request, 'calculator/kalkulacka.html', dict(error_msg = error_msg, vysledek = vysledek))
    return render(request, 'calculator/kalkulacka.html', dict(error_msg = error_msg, vysledek = vysledek))
        
        


