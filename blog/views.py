# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.views.generic.edit import FormView, CreateView
from django.views import generic


# Create your views here.
def post_list(request):
     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
     return render(request, 'blog/post_list.html', {"posts": posts})
    

def post_new1(request):
    
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    content = {
        "form" : form
    }
    
    return render(request, "blog/post_edit.html", content)


class PostNewView(CreateView):
    model = Post
    fields = ['title','author','text']
    template_name = "blog/post_edit_class.html"
    success_url = "/"

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list_class.html"
    success_url = "/"
    queryset = Post.objects.all()

    def get_queryset(self):
        result = super(generic.ListView, self).get_queryset()
        query = self.request.GET.get("q")
        
        if query:
           result = Post.objects.filter(title__icontains = query)
        
        return result
        
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ['text']
    template_name = "blog/post_edit_class.html"
    success_url = "/"