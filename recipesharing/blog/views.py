from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Ingredients
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, CreateView
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
   
    return HttpResponseRedirect(reverse('blog:post-detail', args=[str(pk)]))

# view function to create new post from homepage
class CreateNewPost(CreateView):
    model = Post
    form_class = RecipeForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'new_post.html'

# view function to display a list of posts on the homepage
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query) or Q(author__icontains=query) or Q(description__icontains=query)).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'list.html', {'page': page, 'posts': posts})

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
        return context

def success(request):
    return HttpResponse('done!')        

