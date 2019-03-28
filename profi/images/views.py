from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponse
from .forms import ProfileForm,ImageForm,CommentsForm
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url='/accounts/login/')
def home(request):
    # images = Image.objects.all()
    profile = Profile.objects.all()
    return render(request,'welcome.html',{"profile":profile,"images":images})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request,'profile.html', {"form": form})        

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    
    return render(request,"welcome.html", {"image":image})

#   return redirect('Welcome')    

@login_required(login_url='/accounts/login/')
def profil(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
    images = Image.objects.filter(user = user).all()
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user,"images":images})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return redirect(home)

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(home)

    else:
        form = CommentsForm()
    return render(request, 'comment.html', {"form": form})


def like(request):
    current_user = request.user
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()

            return redirect(home)

    else:
        form = LikeForm()
    return render(request, 'like.html', {"form": form})


