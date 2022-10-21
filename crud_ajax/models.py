from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext as _
from django.urls import reverse
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(_('slug'),populate_from=('title','author__user__username'), unique=True)
    body = RichTextField(max_length=5000)
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
    
    