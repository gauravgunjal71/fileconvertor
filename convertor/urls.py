from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('jpgtopdf', views.jpgToPdf),
    path('pdftojpg', views.pdftojpg),
    path('pdftableextraction', views.pdftableextract),
    path('pdf_view', views.pdf_view)
]