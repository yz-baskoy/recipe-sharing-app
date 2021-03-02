from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 
from django.db.models import Avg

DIF_LEVEL = (
    ('easy','EASY'),
    ('middle','MIDDLE'),
    ('hard','HARD'),
)

class Ingredients(models.Model):
    ingredients = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.ingredients

    def total_ingredients(self):
        return self.ingredients.count()

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_posts' )
    date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    difficulty = models.CharField(max_length=8, choices=DIF_LEVEL, default='easy')
    select_ingredients = models.ManyToManyField(Ingredients)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rating')
    score = models.IntegerField()
