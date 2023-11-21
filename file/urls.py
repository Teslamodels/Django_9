from django.urls import path
from .views import Sigma, Male

urlpatterns = [
    path('', Sigma.as_view(), name='sigma'),
    path('male/', Male.as_view(), name='male'),
]