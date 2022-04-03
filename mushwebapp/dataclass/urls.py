from django.urls import path
from dataclass import views

app_name = 'dataclass'

urlpatterns = [
    path('', views.Dataclass.as_view(), name='dataclass'),
]