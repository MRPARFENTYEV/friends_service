from django.contrib import messages
from django.http import request, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate, login, logout
from sweet_friends_app.forms import UserRegistrationForm, UserLoginForm, EditProfileForm
from sweet_friends_app.models import Friends, User

def paginat(request, list_objects):  # https://docs.djangoproject.com/en/5.0/topics/pagination/

    p = Paginator(list_objects, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj

def return_friends_list(user):
    friends_id = User.return_friends(user) # v

    listus =[]
    for friend_id in friends_id:#v
        us = User.objects.filter(id=friend_id)
        for obj in us:
            listus.append(obj)
    return listus

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(
                request, email=data['email'], password=data['password']
            )

            if user is not None:
                login(request, user)

                return redirect('sweet_friends_app:home_page')
            else:
                messages.error(
                    request, 'Имя или пароль неверны', 'danger'
                )
                return redirect('sweet_friends_app:user_login')
    else:
        form = UserLoginForm()
    context = {'title': 'Login', 'form': form}
    return render(request, 'login.html', context)


def home_page(request):
    user = User.objects.get(id=request.user.id)
    user_name = user.full_name

    fr = return_friends_list(user)

    for frie in fr:
        print('Image',type(frie.image))

    return render(request, 'home.html', context={'user': paginat(request, return_friends_list(user)),
                                                 'user_name':user_name,
                                                 })
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['email'], data['full_name'], data['password'],
            )
            login(request, user)
            return redirect('sweet_friends_app:home_page')

    else:
        form = UserRegistrationForm()
    context = {'title': 'Signup', 'form': form}
    return render(request, 'register.html', context)

def user_logout(request):
    logout(request)
    return redirect('sweet_friends_app:user_login')

def potential_friends(request):
    user = request.user
    print(User.return_friends(user))
    objects = User.objects.all()
    potencial_friends_list =[]
    for potential_friend in objects:
        if potential_friend != user and potential_friend not in User.return_friends(user):
            potencial_friends_list.append(potential_friend)


    context = {'potential_friends': potencial_friends_list}
    return render(request, 'potential_friends.html', context)



def friend_detail(request, user_id):

    friend = get_object_or_404(User, id=user_id)
    print(friend)

    context = {
        'user': friend,
        'full_name': friend.full_name,
        'friends': paginat(request, return_friends_list(friend)),
    }

    return render(request, 'friend_detail.html', context)

def edit_profile(request):

    form = EditProfileForm(request.POST, instance=request.user)
    print(form)
    if form.is_valid():
        form.save()
        messages.success(request, 'Ваш профиль был изменен', 'success')
        return redirect('sweet_friends_app:edit_profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'title':'Edit Profile', 'form':form}
    return render(request, 'edit_profile.html', context)