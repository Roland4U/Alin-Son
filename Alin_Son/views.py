from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import UserRegForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
@login_required
def profile(request):
    return render(request, 'base/profile.html')


def main(request):
    return render(request, 'index.html')