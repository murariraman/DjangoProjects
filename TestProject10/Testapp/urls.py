from django import views
from django.urls import path
from Testapp import views


urlpatterns = [
    path('testapp1/', views.testappview ),
]
