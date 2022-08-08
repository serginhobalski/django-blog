from django.urls import path
from blog.views import home, sobre, contato


urlpatterns = [
    path('', home),
    path('home/', home),
    path('sobre/', sobre),
    path('contato/', contato),
]