from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Website Django',
        'heading' : 'Ini Homepage',
        'subheading' : 'punya Nopal',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ]
    }
    return render(request, 'index.html', context)