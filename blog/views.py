from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request):
    # posts = Article.objects.all()
    posts = Article.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# def project_index(request):
#     posts = Article.objects.all().order_by('-created_on')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'project_index.html', context)
#
#
# def project_detail(request, pk):
#     posts = Article.objects.get(pk=pk)
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'project_detail.html', context)