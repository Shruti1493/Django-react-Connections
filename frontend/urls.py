from django.urls import path
from django.views.generic import TemplateView
from frontend import views

urlpatterns = [
    path('',views.index,name='home'),
]
