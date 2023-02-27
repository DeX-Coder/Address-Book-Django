from django.urls import path
from .views import home
urlpatterns = [
    # all routes here.
    path('', home, name='home'),
]
