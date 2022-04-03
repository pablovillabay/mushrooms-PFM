from django.urls import path
from mushinfo import views

app_name = 'mushinfo'

urlpatterns = [
    path('', views.Mushinfo.as_view(), name='mushinfo'),
]