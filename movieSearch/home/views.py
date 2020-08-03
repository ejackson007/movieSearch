from django.shortcuts import render

posts = [
    {
        'author' : 'Evan',
        'title' : "Test Card",
        'content' : 'First Test',
        'date' : 'August 2, 2020'
    },
    {
        'author' : 'Not Evan',
        'title' : "Test 2 Card",
        'content' : 'Second Test',
        'date' : 'August 2, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html', {'title' : 'about'})