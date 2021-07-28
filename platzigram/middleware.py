# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:


    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            ## saber si es staff if not request.user.is_staff:
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')
        # else:
        #     if request.path not in [reverse('login'), reverse('signup')]:
        #         return redirect('login')


        response = self.get_response(request)
        return response
