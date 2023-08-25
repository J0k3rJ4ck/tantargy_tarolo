from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LoginView
from accounts.models import Tantargy
from .forms import TantargyForm
from .forms import KovetelmenyForm
from accounts.models import Tantargy


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def main(request):
    subjects = []
    return render(request, 'main.html', {'subjects': subjects})


class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse('main')




def main(request):
    return render(request, 'main.html')

'''
def main_view(request):
    return render(request, 'main.html')
'''

def create_tantargy(request):
    if request.method == 'POST':
        form = TantargyForm(request.POST)
        if form.is_valid():
            tantargy = form.save(commit=False)  # Először ne mentsd el a modellt
            tantargy.felhasznalo = request.user  # Hozzáadjuk a bejelentkezett felhasználót
            tantargy.save()  # Most már elmentjük a modellt
            return redirect('main')
    else:
        form = TantargyForm()
    return render(request, 'create_tantargy.html', {'form': form})


def create_kovetelmeny(request):
    if request.method == 'POST':
        form = KovetelmenyForm(request.POST, user=request.user)
        if form.is_valid():
            kovetelmeny = form.save(commit=False)
            kovetelmeny.felhasznalo = request.user
            kovetelmeny.save()
            return redirect('main')
    else:
        form = KovetelmenyForm(user=request.user)
    return render(request, 'create_kovetelmeny.html', {'form': form})



def main_view(request):
    # test
    print("A main_view fut!")
    tantargyak = Tantargy.objects.filter(felhasznalo=request.user)
    return render(request, 'main.html', {'tantargyak': tantargyak})





