from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()

    context = {
        'form': form,
        'title': 'Create Post'
    }
    return render(request, 'post_form.html', context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        'title': instance.title,
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'title': 'List',
        'object_list': queryset
    }
    return render(request, 'index.html', context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
