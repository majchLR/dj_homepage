from django.shortcuts import render

posts = [
    {
        'author': 'Michał Wróbel',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '28-03-2020'
    },
    {
        'author': 'Magdalena Izworska',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '25-03-2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
