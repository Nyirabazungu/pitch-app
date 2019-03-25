from django.shortcuts import render
from django.http  import HttpResponse,HttpResponse
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('Welcome')

    else:
        form = ProfileForm()
    return render(request,'profile.html', {"form": form})        