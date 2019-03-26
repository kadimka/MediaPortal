from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance.slug, filename)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = GenericRelation('comments')
    user_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return "Article '{0}' from category '{1}'".format(self.title, self.category.name)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'category': self.category.slug, 'slug': self.slug})


class MyArticles(Article):
    class Meta:
        proxy = True


class Comments(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class UserAccount(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    favorite_articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account_user', kwargs={'user': self.user.username})
