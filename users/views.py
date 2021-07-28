from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from  django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache

from django.db.utils import IntegrityError
from users.models import Profile
from  django.db import models
from django.contrib.auth.models import User
from users.forms import ProfileForm

# Create your views here.

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

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('feed')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        password_confirmation=request.POST['password_confirmation']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()
        profile=Profile(user=user)
        profile.save()

        login(request, user)
        return redirect('feed')

    return render(request, 'users/signup.html')

@never_cache
@login_required()
def logout_view(request):
    logout(request)
    return redirect('login')
