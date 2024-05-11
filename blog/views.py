from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
import traceback
from django.http import HttpResponseServerError
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from .models import Article
from django.shortcuts import render, get_object_or_404

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})

# def home(request):
#     return render(request, 'home.html')

def home(request):
    # Fetch the latest articles
    print("1")
    latest_articles = Article.objects.order_by('-created_at')[:5]  # Get the latest 5 articles
    return render(request, 'home.html', {'latest_articles': latest_articles})

from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        print("1")
        form = UserCreationForm(request.POST)
        print("2")
        try:
            if form.is_valid():
                print("Form is valid")
                user = form.save()
                print("User registered")
                return redirect('home')
            else:
                print("Form is invalid")
                print(form.errors)
        except Exception as e:
            print("Exception occurred during form validation:", e)
        print("3")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page upon successful login
            else:
                # Authentication failed
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('home')


# @login_required
# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         print("Received POST request.")
#         if form.is_valid():
#             print("Form is valid.")
#             article = form.save(commit=False)
#             article.author = request.user
#             try:
#                 article.save()
#                 print("Article saved successfully.")
#                 # Explicitly return HttpResponseRedirect
#                 print("Redirecting to home page...")
#                 return HttpResponseRedirect('/home/')  # Adjust the URL as needed
#             except IntegrityError as e:
#                 print(f"IntegrityError occurred: {e}")
#                 # Return a more user-friendly error message
#                 return HttpResponseServerError("An error occurred while saving the article. Please try again later.")
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#                 return HttpResponseServerError("An error occurred while saving the article. Please try again later.")
#         else:
#             print("Form is not valid:", form.errors)
#     else:
#         form = ArticleForm()
#     return render(request, 'add_article.html', {'form': form})

from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from .forms import ArticleForm

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            try:
                article.save()
                print("Article saved successfully.")
                # Redirect to the home page using its URL name
                return redirect('home')
            except Exception as e:
                # Handle other exceptions
                return HttpResponseServerError("An error occurred while saving the article. Please try again later.")
        else:
            # Handle invalid form submission
            return HttpResponseServerError("Form is not valid.")
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})




