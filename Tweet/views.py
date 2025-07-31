from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from  .forms import AddTweet,RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

# Create your views here.


def helo(request):
    return render(request,'layout.html')



def homepage(request):
    tweets=Tweet.objects.all()
    return render(request,'homepage.html',{'tweets':tweets})

@login_required
def  addTweet_views(request):
    if request.method=='POST':
        form=AddTweet(request.POST,request.FILES)

        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save
            form.save()
            return redirect('homepage')
        
        else:
            print(form.errors)
            return render(request,'add_tweet.html',{'form':form})
        
    else:
        form=AddTweet()
        return render(request,'add_tweet.html',{'form':form})
    


@login_required
def   edit_tweet(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)
    
    if request.method=='POST':
        form=AddTweet(request.POST,instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        
        return render(request,'edit_tweet.html',{'form':form})
    
    else:
        form=AddTweet()
        return render (request,'edit_tweet.html',{'form':form})








@login_required
def tweet_delete(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)

    

    if request.method=='POST':
        tweet.delete()
        return redirect('homepage')
    
    return render(request,'tweet_delete.html',{'tweet':tweet})
 

    
def Register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        
        else:
            return render(request,'register.html',{'form':form})
    
    else:
       form=RegisterForm()
       return render(request,'register.html',{'form':form})
    



def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

           
            user=authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('homepage')
            return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        
        
        return render(request,'login.html',{'form':form})
    
    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form})
    

def logout_view(request):
    logout(request)
    return redirect('homepage')



def tweet_list(request):
    query=request.GET.get('q')
    if query:
        tweets=Tweet.objects.filter(Q(tweet__icontains=query)|
                Q(user__username__icontains=query)).distinct()
    else:
        tweets=Tweet.objects.all().order_by('-created_at')
    
    return render(request,'search_result.html',{'tweets':tweets})










@login_required
def my_tweet(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_tweet.html', {'tweets': tweets})