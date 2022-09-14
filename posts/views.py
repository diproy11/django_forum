from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .form import PostForm


def index(request):
    # Get all posts
    #if the method is POST
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            form.save() 
    
        # If the form is valid
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    
    posts = Post.objects.all()[:20]
     #Show
     
    return render(request, 'posts.html',{'posts':posts}) 

def delete(request, post_id):
    #Find User
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
   