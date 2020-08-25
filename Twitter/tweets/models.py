from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import Profile


LIKE_CHOICES = (
    ('Like', "Like"),
    ("Unlike", "Unlike")
)


class Heart(models.Model):
    count = models.CharField(max_length=5)


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image_url = models.CharField(
        max_length=2883, default="https://cdn.pixabay.com/photo/2017/08/24/03/41/milky-way-2675322__340.jpg")

    time = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(
        User, null=True, blank=True, related_name='blog_post')
    disliked = models.ManyToManyField(
        User, null=True, blank=True, related_name='blog_post2')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.liked.count()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')
    followers = models.ManyToManyField(
        User, null=True, blank=True, related_name='followers')
    # following = models.ManyToManyField(
    #     User, null=True, blank=True, related_name='following')

    def __str__(self):
        return self.user.username



class Like(models.Model):
    number = models.CharField(max_length=10, null=True, blank=True)

# class Tweet2(models.Model):
#     title = models.CharField(max_length=50)
#     content = models.TextField(max_length=500)
#     image_url = models.CharField(
#         max_length=2883, default="https://cdn.pixabay.com/photo/2017/08/24/03/41/milky-way-2675322__340.jpg")
#     # imgae_url = models.ImageField(default="tweet_default.jpg", upload_to='tweet_pics')
#     # imgae_url = models.ImageField(default='tweet_default.jpg', upload_to='tweet_pics')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     time = models.DateTimeField(auto_now=True)
#     # liked = models.ManyToManyField(
    #     User, null=True, blank=True, related_name='blog_post')
    # disliked = models.ManyToManyField(
    #     User, null=True, blank=True, related_name='blog_post2')


class Coments(models.Model):
    post = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
