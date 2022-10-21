from django.shortcuts import render
from django.views import View, generic
from .models import Post
from django.http import JsonResponse
from .forms import PostForm
from accounts.models import Profile
from datetime import datetime
# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    
class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        posts = Post.objects.all().order_by('-created')
        form = PostForm()
        context = {
            'posts':posts,
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        posts = Post.objects.all()
        form = PostForm(request.POST)
        if is_ajax(request):
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author =  Profile.objects.get(user=request.user)
                instance.save()
                return JsonResponse({
                    'title': instance.title,
                    'body':instance.body,
                    'author':instance.author.user.username,
                    'id':instance.id,
                })
        context = {
            'posts':posts,
            'form':form
        }
        return render(request, self.template_name, context)


def load_post_data_view(request, **kwargs):
    if is_ajax(request):
        num_posts = kwargs.get('num_posts')
        visible = 3
        upper = num_posts
        lower = upper - visible
        size = Post.objects.all().count()

        j_posts = Post.objects.all().order_by('-created')
        data = []
        for obj in j_posts:
            item = {
                'id': obj.id,
                'title':obj.title,
                'slug':obj.slug,
                'body':obj.body,
                'author':obj.author.user.username,
                'liked': True if request.user in obj.liked.all() else False,
                'like_count':obj.like_count,
                'created':obj.created.ctime(),
                'updated':obj.updated
            }
            data.append(item)
            
        return JsonResponse({'data':data[lower:upper], 'size':size})


def load_post_detail_data_view(request, **kwargs):
    slug = kwargs.get('slug')
    post = Post.objects.get(slug=slug)
    data = {
        'id':post.id,
        'title':post.title,
        'slug':post.slug,
        'body':post.body,
        'created':post.created.ctime(),
        'updated':post.updated.ctime(),
        'author':post.author.user.username,
        'logged_in':request.user.username
    } 
    return JsonResponse({'data':data})
    
def likeUnlikePostView(request):
    if is_ajax(request):
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked':liked, 'like_count':obj.like_count})


class PostDetailView(View):
    template_name = 'post/post-detail.html'
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = PostForm()
        context = {
            'post':post,
            'form':form,
        }
        return render(request, self.template_name, context)

def post_detail_udpate(request, **kwargs):
    slug = kwargs.get('slug')
    post = Post.objects.get(slug=slug)
    if is_ajax(request):
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        post.title = new_title
        post.body = new_body
        post.save()
        return JsonResponse({
            'title':new_title,
            'body':new_body
        })

def post_detail_delete(request, **kwargs):
    slug = kwargs.get('slug')
    post = Post.objects.get(slug=slug)
    if is_ajax(request):
        post.delete()
        return JsonResponse({})