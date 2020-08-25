from django.shortcuts import render, redirect, get_object_or_404
from . models import Tweet, Like, Profile, Coments
from .forms import CreateTweetForm, ProfileUpdateForm, UserUpdateForm, FollowersForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import randint
# from django.shortcuts import render



def LikeView(request, pk):
    post = get_object_or_404(Tweet, id=request.POST.get('post_id'))
    # x = Like.objects.create(number="2")
    post.liked.add(request.user)
    return redirect('/tweet_detail/'+ str(pk))

    def __str__(self):
        return self.x


def DisLikeView(request, pk):
    post = get_object_or_404(Tweet, id=request.POST.get('post_id2'))
    # x = Like.objects.create(number="2")
    post.disliked.add(request.user)
    return redirect('/tweet_detail/'+ str(pk))

    def __str__(self):
        return self.x

@login_required(login_url="/accounts/login")
def image_update(request):
    # redirect('/')

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect("/profile")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = request.user
    user = User.objects.all()
    context = {
        "p_form": p_form}
    return render(request, 'image_update.html', context)


@login_required(login_url="/accounts/login")
def user_update(request):
    # redirect('/')

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect("/profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
    current_user = request.user
    # user = User.objects.all()
    context = {
        "u_form": u_form}
    return render(request, 'user_update.html', context)
# profileuser = Profile.objects.filter(user=request.user)
# print(profileuser)


@login_required(login_url='/accounts/login')
def accountProfile(request):

    followers = request.user.profile.followers.all()
    if request.method == 'POST':
        # f_form = FollowersForm
        u_form = UserUpdateForm(request.POST,  instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = request.user
    user = User.objects.all()[0:4]
    # followers = Followers.objects.all()
    context = {"users": user,
               "current": current_user,
               "u_form": u_form,
               "p_form": p_form,
               'followers': followers}
    return render(request, 'profile.html', context)


@login_required(login_url="/accounts/login")
def create_tweet(request):
    form = CreateTweetForm(request.POST)
    # author = request.user
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image_url = request.POST.get('image_url')
        user = request.user
        tweet = Tweet(title=title, content=content, user=user, image_url=image_url)
        tweet.save()
        return redirect("/")

    # context = {"form": form}
    return render(request, 'create_tweet.html', {"form": form})


@login_required(login_url="/accounts/login")
def home(request):
    # contact_list=Tweet.objects.all()
    # post = get_object_or_404(Profile)
    
    context = {}
    followers = request.user.profile.followers.all()
    followers2 = request.user.profile.followers.all()
    followers = followers[0:4]
    user = request.user
    users = User.objects.all()
    # for people in users:
    #     if people not in request.user.followers:
    x = randint(0, len(users))
    y = randint(0, len(users))
    if x == y:
        y = y+2
    elif y == 0:
        y = y+2
        

    print(x, y)
    users = users[x:y]
    total_likes = Like.objects.all().count()
    def __str__(self):
        return self.total_likes
    user = request.user
    tweet = Tweet.objects.all().order_by("-time")
    paginator = Paginator(tweet, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # if request.user.followers in users:
    #     users = users.pop(request.user.followers)
    # else:
    #     users = User.objects.all()

    # post = get_object_or_404(Tweet, id=request.POST.get('post_id'))
    context = {"tweets": page_obj.object_list, "current": user,
               'users': users, 'followers': followers, 'followers2':followers2 , 'paginator': paginator, 'page_number': int(page_number)}
    return render(request, 'index.html', context)

def FollowViewHome(request, pk):

    post = get_object_or_404(Profile, user=pk)


    post.followers.add(request.user)

# post = Profile.objects.filter(user_id=pk)

# test = get_object_or_404()
# x = Like.objects.create(number="2")

    print(post)
    return redirect("/")

def search_page(request):
    return render(request, 'search-page.html')

# def get_tweet_query_set(query=None):
#     queryset = []
#     queries = query.split(" ")
#     for q in queries:
#         posts = Tweet.objects.filter(
#             Q(title__icontains=q) |
#             Q(content__icontains=q)
#         ).distinct()

#         for post in posts:
#             queryset.append(post)
#     return list(set(queryset))

def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts  =  Tweet.objects.none()
    else:
        allPostsTitle = Tweet.objects.filter(title__icontains=query)
        allPostsContent = Tweet.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    context = {"allPosts":allPosts, 'query':query}
    return render(request, 'search.html', context)

def profile_search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts  =  Tweet.objects.none()
    else:
        allPostsTitle = User.objects.filter(username__icontains=query)
        # allPostsContent = Tweet.objects.filter(content__icontains=query)
        allPosts = allPostsTitle

    context = {"allPosts":allPosts, 'query':query}
    return render(request, 'profile_search.html', context)

def FollowView(request, pk):
    post = get_object_or_404(Profile, user=pk)
    followed = False
    if post.followers.filter(id=request.user.id).exists():
        post.followers.remove(request.user)
        followed = False
    else:
        post.followers.add(request.user)
        followed = True
# post = Profile.objects.filter(user_id=pk)

# test = get_object_or_404()
# x = Like.objects.create(number="2")

    print(post)
    return redirect("/profile/")


def UnFollowView(request, pk):
    post = get_object_or_404(Profile, user=pk)
    # post = Profile.objects.filter(user_id=pk)

    # test = get_object_or_404()
    # x = Like.objects.create(number="2")
    # post.followers.add(request.user)
    post.followers.remove(request.user)
    print(post)
    return redirect("/profile/")

    # def __str__(self):
    #     return self.user
def tweetDetail(request, pk):

    tweet = get_object_or_404(Tweet, id=pk)
    comments = Coments.objects.all().order_by('-time')
    context = {'tweet': tweet, 'comments': comments}
    

    return render(request, 'tweetDetailView.html', context)

def CreateComment(request,pk):
    post = get_object_or_404(Tweet, id=pk)
    user = request.user
    content = request.POST.get('comment_content')
    comment = Coments(post=post, user=user, content=content)
    comment.save()
    return redirect('/tweet_detail/'+ str(post.id))


def FollowersList(request):
    followers = request.user.profile.followers.all()
    context = {'followers': followers}
    return render(request, 'followers_list.html', context)


def About(request):
    return render(request, 'about.html')

def updateTweet(request, pk):
    
    post = Tweet.objects.get(id=pk)
    form = CreateTweetForm(instance=post)
    if request.method == 'POST':
        form = CreateTweetForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update_tweet.html', {"form": form})

def deleteTweet(request, pk):
    post = Tweet.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/')

    return render(request, 'delete_tweet.html')