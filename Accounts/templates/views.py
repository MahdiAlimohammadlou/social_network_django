from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.

def posts(request):
    if request.method == "GET":
        all_posts = Post.objects.all()
        # first_post=all_posts[0]
        return render(
            request,
            'blog/posts.html',
            context={"all_posts":all_posts})
    elif request.method == "POST":
        body = request.POST["post_body"]
        Post.objects.create(body=body)
        return HttpResponse(f"new post was created successfully!")