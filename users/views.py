from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from  django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache

from django.db.utils import IntegrityError
from users.models import Profile
from  django.db import models
from django.contrib.auth.models import User
from users.forms import ProfileForm, SignupForm

# Create your views here.
@login_required()
def update_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

        # else:
        #     return render(request, 'users/update_profile.html', context={'form': form})
    else:
        form=ProfileForm()

    print(form['website'])
    x=form['website']
    return render(request=request,
                template_name='users/update_profile.html',
                context={
                    'profile':profile,
                    'user': request.user,
                    'form': form
                    })


def login_view(request):
#    import pdb; pdb.set_trace()  DEBUG
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('feed')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', context={'error' : 'invalid username and password'})
    return render(request, 'users/login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

@never_cache
@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')
