from django.urls import path
from . import views

urlpatterns = [
    path('', views.website),
    path('home', views.website),
    path("contact",views.contact),
    path('about',views.about)
]