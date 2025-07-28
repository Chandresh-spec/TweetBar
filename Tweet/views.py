from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from  .forms import AddTweet

# Create your views here.


def helo(request):
    return render(request,'layout.html')



def homepage(request):
    tweets=Tweet.objects.all()
    return render(request,'homepage.html',{'tweets':tweets})


def  addTweet_views(request):
    if request.method=='POST':
        form=AddTweet(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('homepage')
        
        else:
            print(form.errors)
            return render(request,'add_tweet.html',{'form':form})
        
    else:
        form=AddTweet()
        return render(request,'add_tweet.html',{'form':form})
    

def edit_tweet(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)
    if request.method=='POST':
     form=AddTweet(request.POST,request.FILES,instance=tweet)
     if form.is_valid():
         form.save()
         return redirect('homepage')
     
     else:
         print(form.errors)
         return render(request,'edit_tweet.html',{'form':form})
     
    else:
      form=AddTweet()
      return render(request,'edit_tweet.html',{'form':form})



def tweet_delete(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)

    

    if request.method=='POST':
        tweet.delete()
        return redirect('homepage')
    
    return render(request,'tweet_delete.html',{'tweet':tweet})
 

    
