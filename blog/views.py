from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'JK Rowling',
        'book': 'Harry Potter and the Philospher\'s Stone',
        'description': 'Blog Post 1',
        'date': '10th March 2021'
    },
    {
        'author': 'Stan Lee',
        'book': 'The Amazing Spiderman',
        'description': 'Blog Post 2',
        'date': '10th March 2021'
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
