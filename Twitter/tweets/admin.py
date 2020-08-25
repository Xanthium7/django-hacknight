from django.contrib import admin

from .models import Tweet, Like, Heart, Profile, Coments

# Register your models here.


class TweetAdmin(admin.ModelAdmin):
    admin.site.register(Tweet)


# class FollowerAdmin(admin.ModelAdmin):
#     admin.site.register(Followers)


class LikeAdmin(admin.ModelAdmin):
    admin.site.register(Like)

# class Tweet2Admin(admin.ModelAdmin):
#     admin.site.register(Tweet2)


class HeartAdmin(admin.ModelAdmin):
    admin.site.register(Heart)


class ProfileAdmin(admin.ModelAdmin):
    admin.site.register(Profile)

class CommentAdmin(admin.ModelAdmin):
    admin.site.register(Coments)