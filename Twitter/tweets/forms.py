from django.forms import ModelForm
from django import forms
from . models import Tweet, Profile
from django.contrib.auth.models import User


class CreateTweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['title', 'content', 'image_url']

        widgets = {
            'title': forms.TextInput(attrs={'class': ' input-field white-text'}),
            'content': forms.Textarea(attrs={'class': ' materialize-textarea white-text', 'data-length': "500", "id": "textarea2"}),
            # 'imgae_url': forms.ImageField(attrs={'class': ''}),
            'user': forms.Select(attrs={'class': 'input-field col s12'})


        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserForm(forms.ModelForm):
    model = User
    fields = ['username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        # widgets = {
        #     'image': forms.FileInput(attrs={'class': 'btn-floating waves-effect waves-light', 'style': 'width: 100px;'}),


class FollowersForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['followers']
