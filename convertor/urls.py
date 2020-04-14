from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('jpgtopdf', views.jpgToPdf),
    path('fileuploads', views.fileuploads)
]