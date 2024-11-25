from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'subheading': 'Blog Belajar Django',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ]
    }
    return render(request, 'blog/index.html', context)