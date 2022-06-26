from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'main/home.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.text = request.POST['text']
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.text = request.POST['text']
    if request.FILES.get('image'):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('home')

def create_comment(request, id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('detail', id)

def update_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, id = post_id)
    update_comment = Comment.objects.get(id = comment_id)
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('detail', post.pk)

def edit_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, id = post_id)
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request, 'main/edit_comment.html', {'post':post, 'comment' : edit_comment})

def delete_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('detail', post.pk)


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    
    context = {
        "like_count":post.like_count,
        "result":result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")