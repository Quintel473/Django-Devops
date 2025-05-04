from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('style.css', views.serve_css),  # accessible as /style.css
]
