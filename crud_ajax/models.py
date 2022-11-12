from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as __
from django.urls import reverse
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(_('title'),max_length=200)
    slug = AutoSlugField(__('slug'),populate_from=('title','author__user__username'), unique=True)
    body = RichTextField(_('body'),max_length=5000)
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title+self.author.user.username)
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('crud_ajax:post_detail', args=[self.slug])

    @property
    def like_count(self):
        return self.liked.all().count()
    
    def get_photos(self):
        return self.post_photos.all()

    class Meta:
        ordering = ['-created'] 

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_photos')
    image = models.ImageField(upload_to='post/photo')
    caption = models.CharField(_('caption'),max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.post.title}-{self.pk}"

