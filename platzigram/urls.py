from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from post import views as post_views
from  django.contrib import  admin
urlpatterns = [
    path('hello-world/',local_views.hello_wolrd),
    path('sorted/',local_views.sort_numbers),
    path('hi/<str:name>/<int:age>',local_views.hi),
    path('post/', post_views.list_post ),
    path('admin', admin.site.urls)
]
