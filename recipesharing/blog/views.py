from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Ingredients
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, CreateView, ListView
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def rate_view(request,pk):
    if request.method == 'POST': 
        post = get_object_or_404(Post, id=pk)
        form = RateForm(request.POST)
        if form.is_valid(): 
            score = form.cleaned_data['score']
            Rate.objects.create(user=request.user, score=score, post=post)
            return HttpResponseRedirect(reverse('blog:post-detail', args=[str(pk)]))

def like_view(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
   
    return HttpResponseRedirect(reverse('blog:post-detail', args=[str(pk)]))

@method_decorator(login_required, name='dispatch')
class CreateNewPost(CreateView):
    model = Post
    form_class = RecipeForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'new_post.html'

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'list.html'
    paginate_by = 2
    ordering = '-date' 

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        liked_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = liked_post.total_likes()

        liked = False
        if liked_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["rateform"] = RateForm()
        return context

class SearchView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            query = self.model.objects.filter(title__icontains=search)
            return query
         
