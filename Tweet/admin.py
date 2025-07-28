from django.contrib import admin

# Register your models here.

from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
        fields=('tweet',)
    



admin.site.register(Tweet,TweetAdmin)
