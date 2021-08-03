from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from post import views as post_views
from  django.contrib import  admin
from  django.conf import  settings
from  django.conf.urls.static import  static
from users import views as users_views
urlpatterns = [

    path('', users_views.login_view, name='home'),
    path('hello-world/',local_views.hello_wolrd, name='hello_wolrd'),
    path('sorted/',local_views.sort_numbers, name='sorted'),
    path('hi/<str:name>/<int:age>',local_views.hi, name='hi'),
    path('post/', post_views.list_post, name='feed' ),
    path('post/new', post_views.create_post, name='create_post'),
    path('admin', admin.site.urls),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile')

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
