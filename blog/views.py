from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'JK Rowling',
        'book': 'Harry Potter and the Philospher\'s Stone',
        'rating': '9.8'
    },
    {
        'author': 'Stan Lee',
        'book': 'The Amazing Spiderman',
        'rating': '9.6'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Blogs'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
