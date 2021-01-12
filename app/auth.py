from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def user_register(request):
    curent_user = request.user
    if curent_user.is_authenticated:
        return redirect('app:dashboard')
    form = user_form_create()
    if request.method == 'POST':
        form = user_form_create(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('app:signin')
    context = {
        'form': form
    }
    return render(request, 'account/sign_up.html', context)


def user_login(request):
    user_active = request.user
    if user_active.is_authenticated:
        return redirect('app:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=username).username
        except:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:dashboard')
        else:
            messages.error(
                request, "Username or password is invalid. Please try again.")
    return render(request, 'account/sign_in.html')


@login_required(login_url='app:signin')
def user_profile(request, username):
    if request.method == 'POST':
        user_form = form_user_update(request.POST, instance=request.user)
        image_form = form_user_update_avatar(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and image_form.is_valid():
            user_form.save()
            image_form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Your profile was updated successfully!')
            return redirect('app:profile', username=username)
    else:
        user_form = form_user_update(instance=request.user)
        image_form = form_user_update_avatar(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'image_form': image_form
    }

    return render(request, 'account/profile.html', context)


@login_required(login_url='app:signin')
def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('app:signin')
