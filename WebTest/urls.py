from django.urls import path, include
from . import views, url_handlers

urlpatterns = [
    path('line', views.plc, name='plc'),
    path('bar', views.hmi, name='hmi'),
    path('start', views.start, name='start'),
    path('tables', views.data, name='data'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('', url_handlers.index_handler),
]
