from django.shortcuts import render
from second_app.forms import UserForm, UserProfileInfoForm
#from django.http import HttpResponse
#from second_app.models import User
#from second_app.forms import NewUserForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    #context_dict = {'text':'hello', 'number':1000 }
    return render(request, 'second_app/index.html')#,context_dict)

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'second_app/registration.html',
                                {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered':registered})

def relative(request):
    return render(request, 'second_app/relative_url_template.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")


def user_login(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed")
            print("Username:{}, pass: {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'second_app/login.html',{})
