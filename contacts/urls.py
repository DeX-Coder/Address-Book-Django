from django.urls import path
from .views import home, details
urlpatterns = [
    # all routes here.
    path('', home, name='home'),
    path('<int:id>/', details, name='details')
]
