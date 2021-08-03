from django.shortcuts import render, redirect
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.decorators.cache import cache_control, never_cache

from post.models import Post
from post.forms import PostForm
# Create your views here.


@never_cache
@login_required()
def list_post(request):

    posts= Post.objects.all().order_by('-created')
    return render(request, 'post/feed.html', {'posts':posts})

@login_required()
def create_post(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form= PostForm()
    return render(request,
        template_name='post/new.html',
        context={'form':form,
                'user': request.user,
                'profile': request.user.profile}
                )
