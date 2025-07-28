from django import forms
from .models import Tweet


class AddTweet(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=('tweet','image')