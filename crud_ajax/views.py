from django.shortcuts import render
from django.views import View, generic
from .models import Post
from django.http import JsonResponse
# Create your views here.


class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts':posts,
        }
        return render(request, self.template_name, context)


def load_post_data_view(request, **kwargs):
    num_posts = kwargs.get('num_posts')
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    j_posts = Post.objects.all()
    data = []
    for obj in j_posts:
        item = {
            'id': obj.id,
            'title':obj.title,
            'slug':obj.slug,
            'body':obj.body,
            'author':obj.author.user.username,
            'liked': True if request.user in obj.liked.all() else False,
            'created':obj.created,
            'updated':obj.updated
        }
        data.append(item)
    return JsonResponse({'data':data[lower:upper], 'size':size})
    
