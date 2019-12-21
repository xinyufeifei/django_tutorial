from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "Qiong",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Dec 21, 2019",
    },
    {
        "author": "Jane Don",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "Dec 22, 2019",
    },
]

# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
