from django.urls import path
from imgclass import views

app_name = 'imgclass'

urlpatterns = [
    path('', views.IMGclass.as_view(), name='imgclass'),
]