from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm 
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
     if request.method == "POST":
            fm = SignUpForm(request.POST)
            if fm.is_valid():
             messages.success(request, 'Account Created Successfully !!') 
            #  messages.add_message(request,messages.SUCCESS, "Your Account has been created! ")
             fm.save()
            #  return HttpResponseRedirect('/')
     else: 
      fm = SignUpForm()
     return render(request,'registration.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have Logged in successfully !!')
                    return HttpResponseRedirect('/')
        else: 
         fm = AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    else:
      return HttpResponseRedirect('/')
    

@login_required
def logoutuser(request):
    logout(request)
    return redirect('/')# Redirect to home or any other page

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the user's new password
            messages.success(request, 'Password Changed successfully !!')
            return redirect('/login/')  # Redirect to home page or any other page after password change
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'changepassword.html', {'form': form})


@login_required
def account(request):
    return render(request, 'account.html')








#views for quiz 


def quiz_home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            # print(request.POST.get(q.question))
            # print(q.ans)
            # print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz_home.html',context)
       


def addQuestion(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')



# def post_list(request):
#     posts = BlogPost.objects.all()
#     return render(request, 'post_list.html', {'posts': posts})

# def post_detail(request, post_number):
#     post = get_object_or_404(BlogPost, post_number=post_number)
#     return render(request, 'post_detail.html', {'post': post})

# def create_post(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')
#     else:
#         form = BlogPostForm()
#     return render(request, 'create_post.html', {'form': form})



def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})
