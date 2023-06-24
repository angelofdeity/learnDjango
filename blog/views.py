from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'name': 'Nico',
        'title': 'I must win',
        'content': 'Winning is something that must be constant',
        'date': 'June 24th 2023'
    },
    {
        'name': 'Angel',
        'title': 'I will guide',
        'content': 'Guidance is something everyone needs',
        'date': 'June 23rd 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return HttpResponse('Blog about')
