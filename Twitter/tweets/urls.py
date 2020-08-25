from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    # path("accounts/profile", views.accountProfile)
    path("createtweets", views.create_tweet),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('dislike/<int:pk>', views.DisLikeView, name='dislike_post'),
    path('follow/<int:pk>', views.FollowView, name='follow_post'),
    path('followhome/<int:pk>', views.FollowViewHome, name='follow_post'),
    path('unfollow/<int:pk>', views.UnFollowView, name='unfollow_post'),
    path('profile/', views.accountProfile, name="profile"),
    path('image_update/', views.image_update),
    path('user_update/', views.user_update),
    path('search/', views.search, name='search'),
    path('search_page/', views.search_page, name='search-page'),
    path('tweet_detail/<int:pk>', views.tweetDetail, name="tweet_detail"),
    path('create_comment/<int:pk>', views.CreateComment, name='create_comment'),
    path('profile_search/', views.profile_search, name='profile_search'),
    path('follower_list/', views.FollowersList, name="followerslist"),
    path('about/', views.About, name="About"),
    path('delete_tweet/<int:pk>', views.deleteTweet, name='DeleteTweet'),
    path('update_tweet/<int:pk>', views.updateTweet, name='UpdateTweet'),
    # path('bla/', views.home2, name='home2'),
    # path("createtweets2", views.tweetCreatePage),
    # path("creating/", views.createtweet2),
]
