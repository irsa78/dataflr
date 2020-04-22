from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
# Create your views here.
#DataFlair #AJAX_tutorial
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })
def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")

# def search(request):
#     if request.method=='POST':
#         search_text=request.POST['search_text']
#     else:
#         search_text=''
#     post=Post.objects.filter(post_heading__contains=search_text)
#     return render()
