from django.shortcuts import render
from django.http import HttpResponse
from  datetime import datetime
from django.contrib.auth.decorators import login_required #pide iniciar seccion
from django.views.decorators.cache import cache_control, never_cache


# Create your views here.

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@never_cache
@login_required()
def list_post(request):

    # content=[]
    # for post in posts:
    #     content.append("""
    #     <p><strong> {name} </strong></p>
    #     <p><small> {user} - <i> {timestamp}</i> </small> </p>
    #     <figure><img src="{picture}"/> </figure>
    #     """.format(**post))
    #
    # return HttpResponse('<br>'.join(content))

    return render(request, 'post/feed.html', {'posts':posts})
