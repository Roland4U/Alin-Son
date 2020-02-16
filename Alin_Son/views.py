from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserRegForm
from django.contrib.auth.forms import UserCreationForm

class UserReg(UserRegForm, UserCreationForm, View):
    def get(self, request):
        form = UserRegForm()

        return render(request, 'base/user_reg.html', context={'form': form})

    def post(self, request):
        if request.method == "POST":
            form = UserRegForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('reg')

