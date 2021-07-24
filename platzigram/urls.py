from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello-world/',views.hello_wolrd),
    path('sorted/',views.sort_numbers),
    path('hi/<str:name>/<int:age>',views.hi)
]
