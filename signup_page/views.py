from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages


# Create your views here.

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hi Your Account Created Successfully!!")
            return redirect("signin")
    else:
        form = SignupForm()

    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    return render(request, 'sign_in.html')
