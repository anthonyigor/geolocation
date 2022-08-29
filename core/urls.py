from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.asview(), name='index')
]
