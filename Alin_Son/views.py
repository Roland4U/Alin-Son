from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserRegForm, UserLogForm
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.views import AuthenticationForm as Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

class UserReg(UserRegForm, UserCreationForm, View):
    def get(self, request):
        
        reg_form = UserRegForm()

        return render(request, 'base/user_reg.html', context={'reg_form': reg_form})

    def post(self, request):
        if request.method == "POST":
            reg_form = UserRegForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                return redirect('main')
@login_required
def profile(request):
    return render(request, 'base/profile.html')


class main(View):
    def get(self, request):
        login_form = UserLogForm()
        reg_form = UserRegForm()
        return render(request, 'index.html', context={'login_form': login_form, 'reg_form': reg_form})

    # def post(self, request):
    #     if request.method == "POST":
    #         reg_form = UserRegForm(request.POST)
    #         if reg_form.is_valid():
    #             reg_form.save()
    #             return redirect('main')
