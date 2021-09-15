
from django.urls import path

from .views import event


urlpatterns = [
    path('api/event/', event, name='event'),
]