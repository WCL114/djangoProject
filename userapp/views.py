from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, UserProfileEdit
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # 不要立即保存用户，先处理密码哈希
            password = form.cleaned_data['password']  # 从表单中获取密码
            user.password = make_password(password)  # 对密码进行哈希
            user.save()  # 保存用户到数据库
            return redirect('userapp:login')  # 重定向到登录页面
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # 登录成功后可以重定向到某个页面
                return redirect('/')
            else:
                # 登录失败，返回错误消息
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def user_center(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserChangeForm(instance=user)
    return render(request, 'center/user_center.html', {
        'user_form': user_form,
        'user': user
    })


def edit_profile(request, pk):
    if request.method == 'POST':
        form = UserProfileEdit(request.POST, request.FILES, instance=request.user)  # 包括 request.FILES
        if form.is_valid():
            form.save()
            return redirect('userapp:user_center', pk=pk)  # 重定向到用户个人资料页面
    else:
        form = UserProfileEdit(instance=request.user)
    return render(request, 'center/edit_profile.html', {'form': form})

