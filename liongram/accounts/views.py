from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm , SignUpForm

from users.models import User
# Create your views here.
def signup_view(request):
    #GET 요청 시 html 응답 
    if request.method =='GET':
        form = SignUpForm
        context ={'form':form}
        return render(request,'accounts/signup.html',context)
    #post 요청 시 데이터 확인 후 회원 생성
    else: 
        form = SignUpForm(request.POST)
 
        if form.is_valid():
            #회원가입 처리
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            instance= form.save()
            return redirect('index')

        else:
            #리다이렉트 
            return redirect('accounts:signup')

def login_view(request):
    #GET, POST 분리 
    if request.method == 'GET':
        #로그인 HTML 응답
        return render(request,'accounts/login.html',{'form':AuthenticationForm()})
        pass
    else: #로그인 요청시 (POST)
        form = AuthenticationForm(request,request.POST)
        #데이터 유효성 검사
        if form.is_valid():
        # 비즈니스 로직 처리 --로그인처리
            login(request, form.user_cache)
        #응답
            return redirect('index')
        else:
        # 비즈니스 로직 처리 -- 로그인 실패
        #응답
            
            return render(request,'accounts/login.html',{'form':form})



###     # username = request.POST.get['username']
        # if username == '' or username == None:
        #     pass
        # user= User.objects.get(username=username)
        # if user == None:
        #     pass
        # password = request.POST.get['password']

def logout_view(request):
    #데이터 유효성 검사
    if request.user.is_authenticated:
        # 비즈니스 로직 처리 -- 로그아웃
        logout(request)
        #응답
        return redirect('index')
